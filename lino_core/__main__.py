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


import os, sys, subprocess


def main():
    
    ## Inputs
    # IPT__nickname = os.environ['IPT__nickname']
    # IPT__banner = os.environ['IPT__banner']
    # IPT__include_last_activity = os.environ['IPT__include_last_activity']
    # IPT__credit = os.environ['IPT__credit']
    ## vvv better data encapsulation
    ipts = {
        'nickname': os.environ['IPT__nickname'],
        'banner': os.environ['IPT__banner'],
        'include_last_activity': os.environ['IPT__include_last_activity'],
        'credit': os.environ['IPT__credit'],
    }
    for k,v in ipts.items(): print(f"DEBUG: (inputs) {k}: {repr(v)}")


    import json

    GITHUB_ACTOR = os.environ['GITHUB_ACTOR']

    command = f"gh repo list {GITHUB_ACTOR} --visibility public --json url"
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)

    if result.returncode == 0:
        repo_list = json.loads(result.stdout)
        for repo in repo_list:
            print("Repository URL:", repo['url'])
    else:
        print("Error running the command:", result.stderr)



if __name__ == '__main__':
    main()



"""
credit-versioning style
Lino-1.0 lino-v2 lino-main
Lino(1.0) Lino(main) Lino(v2)
"""
