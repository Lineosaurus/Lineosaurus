import os, subprocess, json


def clone(gh_actor, CLONE_DIR):
    # result = subprocess.run(f"gh repo list {gh_actor} --visibility public --json url", stdout=subprocess.PIPE, shell=True, text=True)
    # repo_list = json.loads(result.stdout)
    # print(repo_list)
    # clone_urls = [i['url']+'.git' for i in repo_list]
    # print(len(clone_urls), clone_urls)
    ## vvvvvvvvvvv
    urls = [
        i['url']+'.git'
        for i in json.loads(
            subprocess.run(f"gh repo list {gh_actor} --visibility public --json url", stdout=subprocess.PIPE, shell=True, text=True).stdout
        )
    ]
    print(f"INFO: #urls: {len(urls)}")
    print(f"DEBUG: urls: {urls}")

    for u in urls:
        print(f"DEBUG: Cloning: {repr(u)}.")
        subprocess.run(['git', 'clone', u], cwd=CLONE_DIR)

def gather_stuff(root_user, gh_actor):
    out = {}

    # CLONE_DIR = os.path.join(ROOT_USER, '..', '__clone_dir')
    CLONE_DIR = os.path.abspath(os.path.join(root_user, '..', '__clone_dir'))
    print(f"DEBUG: repr(CLONE_DIR): {repr(CLONE_DIR)}")
    
    print(f"DEBUG: os.path.isdir(CLONE_DIR): {os.path.isdir(CLONE_DIR)}")
    os.mkdir(CLONE_DIR)
    print(f"DEBUG: os.path.isdir(CLONE_DIR): {os.path.isdir(CLONE_DIR)}")

    print(f"DEBUG: os.listdir(CLONE_DIR): {os.listdir(CLONE_DIR)}")
    clone(gh_actor, CLONE_DIR)
    print(f"DEBUG: os.listdir(CLONE_DIR): {os.listdir(CLONE_DIR)}")

    return out
