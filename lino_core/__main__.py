# import random
# from datetime import datetime




# def main(banner_path, banner_alt):

#     day = datetime.now().strftime('%A')
    
#     header = get_random_hello(day) + '\n\n'

#     if banner_path != '':
#         header += f'![{banner_alt}]({banner_path})\n\n'
#     else:
#         header += ''
#     header += "_OWNER_'s repos (_LINESFMT_ lines of code, _CMITFMT_ commits, _CHARSFMT_ chars)"

#     OPTIONS = {
#         'HEADER': header,
#         'FOOTER': '<sub>last update: _DATE_ - _CREDIT_</sub>',
#         'CARD_ORDER': 'cmit\n',
#         'SHOW_CREDIT': 'false',
#     }

#     return OPTIONS


import os, sys, subprocess, json
sys.path.append(os.environ['GITHUB_ACTION_PATH'])  # make the needed folders importable
from lino_core.engine.gather_stuff import gather_stuff
from lino_core.engine.update_readme import update_readme

def main():
    
    ## Inputs
    ipts = {
        'nickname': os.environ['IPT__nickname'],
        'banner': os.environ['IPT__banner'] if (os.environ['IPT__banner'] != '') else None,
        'include_last_activity': True if (os.environ['IPT__include_last_activity'] == 'true') else False,
        'credit': True if (os.environ['IPT__credit'] == 'true') else False,
    }
    for k,v in ipts.items(): print(f"DEBUG: (inputs) {k}: {repr(v)}")

    ## various constants
    misc = {
        'root_user': os.environ['GITHUB_WORKSPACE'],
        'root_action': os.environ['GITHUB_ACTION_PATH'],
        'gh_actor': os.environ['GITHUB_ACTOR'],
        'act_ver': os.environ['GITHUB_WORKFLOW_REF'].split('/')[-1],  # the Action version
    }
    for k,v in misc.items(): print(f"DEBUG: (misc constants) {k}: {repr(v)}")

    # result = subprocess.run(f"gh repo list {misc['gh_actor']} --visibility public --json url", stdout=subprocess.PIPE, shell=True, text=True)
    # repo_list = json.loads(result.stdout)
    # print(repo_list)
    # clone_urls = [i['url']+'.git' for i in repo_list]
    # print(len(clone_urls), clone_urls)

    needed = gather_stuff(
        root_user=misc['root_user'],
        gh_actor=misc['gh_actor'],
    )

    update_readme(
        banner_pth=ipts['banner'],
        gh_actor=misc['gh_actor'],
        lines_of_code=needed['lines_of_code'], nCommits=needed['nCommits'], nChars=needed['nChars'],
        include_last_activity=ipts['include_last_activity'], last_acts=needed['last_acts'],
        nickname=ipts['nickname'],
        nCommits_last_week=needed['nCommits_last_week'],
        lino_ver=misc['act_ver'],
        readme_pth=os.path.join(misc['root_user'], 'README.md'),
        include_credit=ipts['credit'],
    )


if __name__ == '__main__':
    main()




# NON_TEXT_TYPE = [

#     ## Images
#     '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.ico',

#     ## Videos
#     '.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.mpeg', '.3gp', '.m4v', '.ogg',

#     ## Audios
#     '.mp3', '.wav', '.ogg', '.aac', '.flac', '.wma', '.m4a', '.aiff', '.opus', '.mid',

#     ## .git/
#     '.idx', '.pack', '.rev',
# ]
# NON_TEXT_FILENAME = [

#     ## .git/
#     'index',
# ]