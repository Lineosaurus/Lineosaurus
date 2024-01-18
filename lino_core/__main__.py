# import random
# from datetime import datetime


# def get_random_hello(day):
#     l = [
#         f"Wish you an awesome {day}! 🌼",
#         f"Smile, it's {day}! ☀️",
#         f"Hey there! Have a great {day}! 🌈",
#         f"Wishing you an amazing {day}! 🎉",
#         f"May your {day} be wonderful! 🌸",
#         f"Have a fantastic {day}! 🌹",
#         f"Smile, it's a beautiful {day}! 🌺",
#         f"Keep shining on this {day}! 🌷",
#     ]
#     return random.choice(l)


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


def main():
    
    ## Inputs
    ipts = {
        'nickname': os.environ['IPT__nickname'],
        'banner': os.environ['IPT__banner'],
        'include_last_activity': os.environ['IPT__include_last_activity'],
        'credit': os.environ['IPT__credit'],
    }
    for k,v in ipts.items(): print(f"DEBUG: (inputs) {k}: {repr(v)}")

    ## various constants
    misc = {
        'root_user': os.environ['GITHUB_WORKSPACE'],
        'root_action': os.environ['GITHUB_ACTION_PATH'],
        'gh_actor': os.environ['GITHUB_ACTOR'],
        'act_ver': os.environ['GITHUB_REF'],  # the Action version
    }
    for k,v in misc.items(): print(f"DEBUG: (misc constants) {k}: {repr(v)}")

    result = subprocess.run(f"gh repo list {misc['gh_actor']} --visibility public --json url", stdout=subprocess.PIPE, shell=True, text=True)
    repo_list = json.loads(result.stdout)
    print(repo_list)
    clone_urls = [i['url']+'.git' for i in repo_list]
    print(len(clone_urls), clone_urls)




if __name__ == '__main__':
    main()



"""
credit-versioning style
Lino-1.0 lino-v2 lino-main
Lino(1.0) Lino(main) Lino(v2)
"""



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