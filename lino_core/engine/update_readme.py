import random
from datetime import datetime

def get_header(day):
    l = [
        f"Wish you an awesome {day}! 🌼",
        f"Smile, it's {day}! ☀️",
        f"Hey there! Have a great {day}! 🌈",
        f"Wishing you an amazing {day}! 🎉",
        f"May your {day} be wonderful! 🌸",
        f"Have a fantastic {day}! 🌹",
        f"Smile, it's a beautiful {day}! 🌺",
        f"Keep shining on this {day}! 🌷",
        f"Have a great {day}!",
        f"This {day} is awesome!",
        f"Happy {day}!",
        f"What a cool {day}!",
        f"Great {day}! You are awesome 💐",
    ]
    if len(l) != len(set(l)): raise AssertionError  # just in case there are duplicates
    return random.choice(l)

def update_readme(
    banner_pth:str|None,
    gh_actor:str,
    
    lines_of_code:int,
    nChars:int,
    
    include_last_activity:bool,
    last_act:list,  # [repo-name, its-last-commit-timestamp, progLanguage-info]
    
    nickname:str,
    nCommits_last_week:int,
    lino_ver:str,
    readme_pth:str,
    include_credit:bool,

    nRepos:int,  # number of repos
):    
    text = get_header(datetime.now().strftime('%A')) + '\n\n'

    if banner_pth is not None:
        text += f"![banner]({banner_pth})\n\n"

    text += f"There are {lines_of_code:,} lines of code and {nChars:,} characters across {nRepos:,} {gh_actor}'s repositories.\n\n"

    if include_last_activity:
        text += f"*Last repo I worked on is `{last_act[0]}` ({datetime.fromtimestamp(last_act[1]).strftime(random.choice(['%b %-d, %Y', '%A, %b %-d', '%a, %B %-d']))}), and it's {last_act[2]}!*\n\n"
    
    ## Commits last week
    text += (
        f"{nickname} made {nCommits_last_week} commits in the last week, "
        + random.choice(['what an awesome!', 'really great!', 'simply amazing!', 'incredibly cool!', 'wonderful!', 'awesome!'])
    )
    footer_time = datetime.now().astimezone().strftime(random.choice(['%Y %b %-d', '%Y %B %-d', '%b %-d, %Y']))
    if include_credit:
        text += (
            f"<sub> ~ last update: {footer_time} - "
            f"{random.choice(['Counted by', 'By', '❤️'])} [Lineosaurus({lino_ver})](https://github.com/Lineosaurus/Lineosaurus)</sub>"
        )
    else:
        text += f"<sub> ~ last update: {footer_time}</sub>"

    print('─'*100 + '\n' + text + '\n' + '─'*100)

    ## save
    print(f"INFO: Rewriting: {repr(readme_pth)}.")
    with open(readme_pth, 'w') as f:
        f.write(text)
