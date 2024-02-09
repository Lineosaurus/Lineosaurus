import os, subprocess, json
from datetime import datetime

CANT_COUNT = [  # cant count lines of code for these files' types. cases dont matter (use lowercase).  TODO: add more types if needed

    ## Images
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.ico',

    ## Videos
    '.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.mpeg', '.3gp', '.m4v', '.ogg',

    ## Audios
    '.mp3', '.wav', '.ogg', '.aac', '.flac', '.wma', '.m4a', '.aiff', '.opus', '.mid',

    ## .git/
    '.idx', '.pack', '.rev',
]
CANT_COUNT_NAME = [  # skip files with names (cases do matter):

    ## .git/
    'index',
]

def clone(gh_actor, CLONE_DIR):
    urls = [
        i['url']+'.git'
        for i in json.loads(
            subprocess.run(f"gh repo list {gh_actor} --visibility public --json url --limit 99999", stdout=subprocess.PIPE, shell=True, text=True).stdout
        )
    ]
    print(f"INFO: #urls: {len(urls)}")
    print(f"DEBUG: urls: {urls}")

    for u in urls:
        print(f"DEBUG: Cloning: {repr(u)}.")
        subprocess.run(['git', 'clone', u], cwd=CLONE_DIR)

def get_lines_of_code(CLONE_DIR):
    k = 0
    def the_recursive(dir_pth):
        n = 0
        for i in os.listdir(dir_pth):
            ipth = os.path.join(dir_pth, i)
            if os.path.isfile(ipth):
                if i.lower().endswith(tuple(CANT_COUNT)) or (i in CANT_COUNT_NAME): continue
                with open(ipth, 'r') as f: n += len(f.read().split('\n'))  # TODO: not really accurate, should exclude some files from ".git/" folder, but for now, it's okay...
            elif os.path.isdir(ipth): n += the_recursive(ipth)
            else: raise AssertionError(f"Unknown: {repr(ipth)}.")
        return n
    for repo in os.listdir(CLONE_DIR):
        pth = os.path.join(CLONE_DIR, repo)
        k2 = the_recursive(pth)
        k += k2
        print(f"DEBUG: lines of code ({repo}): {k2}")
    return k

def get_nCommits(CLONE_DIR):
    k = 0
    for repo in os.listdir(CLONE_DIR):
        pth = os.path.join(CLONE_DIR, repo)
        k2 = int(subprocess.run(['git', 'rev-list', '--count', 'HEAD'], cwd=pth, stdout=subprocess.PIPE, text=True, check=True).stdout.strip())
        k += k2
        print(f"DEBUG: nCommits ({repo}): {k2}")
    return k

def get_nChars(CLONE_DIR):
    k = 0
    def the_recursive(dir_pth):
        n = 0
        for i in os.listdir(dir_pth):
            ipth = os.path.join(dir_pth, i)
            if os.path.isfile(ipth):
                if i.lower().endswith(tuple(CANT_COUNT)) or (i in CANT_COUNT_NAME): continue
                with open(ipth, 'r') as f: n += len(f.read())
            elif os.path.isdir(ipth): n += the_recursive(ipth)
            else: raise AssertionError(f"Unknown: {repr(ipth)}.")
        return n
    for repo in os.listdir(CLONE_DIR):
        pth = os.path.join(CLONE_DIR, repo)
        k2 = the_recursive(pth)
        k += k2
        print(f"DEBUG: nChars ({repo}): {k2}")
    return k

def get_nCommits_last_week(CLONE_DIR, ghActor):
    k = 0
    for repo in os.listdir(CLONE_DIR):
        if repo == ghActor: print(f"DEBUG: Skip the github.com/name/name repo: {repr(repo)}.");continue
        pth = os.path.join(CLONE_DIR, repo)
        k2 = int(subprocess.run(['git', 'rev-list', '--count', '--since="1 week ago"', 'HEAD'], stdout=subprocess.PIPE, text=True, check=True, cwd=pth).stdout.strip())
        k += k2
        print(f"DEBUG: nCommits_last_week ({repo}): {k2}")
    return k

def get_last_acts(CLONE_DIR, gh_actor):  # get last 3 activities
    out = {}
    for repo in os.listdir(CLONE_DIR):
        pth = os.path.join(CLONE_DIR, repo)
        result = subprocess.check_output(['git', 'log', '-1', '--format=%cd'], stderr=subprocess.STDOUT, text=True, cwd=pth)
        print(f"DEBUG: last commit at ({repo}): {repr(result)}")
        in_utc_timestamp = int(datetime.strptime(result.strip('\n'), "%a %b %d %H:%M:%S %Y %z").timestamp())
        if repo == gh_actor: continue  # exclude the github.com/NAME/NAME repo
        out[f"{gh_actor}/{repo}"] = in_utc_timestamp
    out = dict(sorted(out.items(), key=lambda x: x[1], reverse=True)[:3])  # pick latest 3
    return out

def gather_stuff(root_user, gh_actor):
    out = {}

    CLONE_DIR = os.path.abspath(os.path.join(root_user, '..', '__clone_dir'))
    print(f"DEBUG: repr(CLONE_DIR): {repr(CLONE_DIR)}")
    
    print(f"DEBUG: os.path.isdir(CLONE_DIR): {os.path.isdir(CLONE_DIR)}")
    os.mkdir(CLONE_DIR)
    print(f"DEBUG: os.path.isdir(CLONE_DIR): {os.path.isdir(CLONE_DIR)}")

    print(f"DEBUG: os.listdir(CLONE_DIR): {os.listdir(CLONE_DIR)}")
    clone(gh_actor, CLONE_DIR)
    print(f"DEBUG: os.listdir(CLONE_DIR): {os.listdir(CLONE_DIR)}")

    out['lines_of_code'] = get_lines_of_code(CLONE_DIR)
    out['nCommits'] = get_nCommits(CLONE_DIR)
    out['nChars'] = get_nChars(CLONE_DIR)
    out['nCommits_last_week'] = get_nCommits_last_week(CLONE_DIR, gh_actor)
    out['last_acts'] = get_last_acts(CLONE_DIR, gh_actor)

    return out
