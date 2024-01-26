import random, time
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
    ]
    return random.choice(l)

def update_readme(
    banner_pth:str|None,
    gh_actor:str,
    
    lines_of_code:int,
    nCommits:int,
    nChars:int,
    
    include_last_activity:bool,
    last_acts:dict,  # {owner/repo-name: last-commit-timestamp, ...}
    
    nickname:str,
    nCommits_last_week:int,
    lino_ver:str,
    readme_pth:str,
    include_credit:bool
):    
    text = get_header(datetime.now().astimezone().strftime('%A')) + '\n\n'

    if banner_pth is not None:
        text += f"![banner]({banner_pth})\n\n"

    text += f"{gh_actor}'s repos ({lines_of_code:,} lines of code, {nCommits:,} commits, {nChars:,} chars)\n\n"

    if include_last_activity:
        act_list = []
        for name, ts in last_acts.items():
            # d1 = datetime.fromtimestamp(ts).astimezone().strftime(random.choice(['%a, %b %-d, %Y, ', '%A, ', '%A, ', '%B %-d, ']))  # prioritize the concise one
            ## vvvvv more options but still concise
            d1 = datetime.fromtimestamp(ts).astimezone().strftime(random.choice(['%a, %b %-d, %Y', '%b %-d', '%b %-d', '%A', '%B %-d']))  # prioritize the concise one (note, yes the "'%b %-d'" is doubled)
            # d2 = datetime.fromtimestamp(ts).astimezone().strftime(f", %I:%M%p{random.choice([' utc%z', ''])}").lstrip('0')
            ## vvvvvvv the above one cant do the lstrip(0)
            d2 = ', ' + datetime.fromtimestamp(ts).astimezone().strftime(f"%I:%M%p{random.choice([' utc%z',''])}").lstrip('0')
            act_list.append(f"{random.choice([name, name[len(gh_actor)+1:]])}[{d1+random.choice([d2, ''])}]")
            time.sleep(0.1)  # to make the "randomizer" truly random. idk, if it's really working or not.
        text += (
            "```python\n"
            f"Repos I was working on lately:\n→ {', '.join(act_list)}\n"
            "```\n\n"
        )
    
    ## Commits last week
    text += (
        f"{nickname} made {nCommits_last_week} commits in the last week, "
        + random.choice(['what an awesome!', 'really great!', 'simply amazing!', 'incredibly impressive!', 'wonderful!', 'impressive!'])
        # + '\n\n'  # no need (make the credit inline with this line)
    )

    footer_time = datetime.now().astimezone().strftime(random.choice(['%Y %b %-d', '%Y %B %-d', '%b %-d, %Y']))
    if include_credit:
        text += (
            f"""<sub align="right">last update: {footer_time} - """
            f"Counted by [Lineosaurus({lino_ver})](https://github.com/Lineosaurus/Lineosaurus)</sub>"
        )
    else:
        text += f"<sub>last update: {footer_time}</sub>"

    print('─'*100)
    print(text)
    print('─'*100)

    ## save
    print(f"INFO: Rewriting: >> {repr(readme_pth)} <<.")
    with open(readme_pth, 'w') as f:
        f.write(text)
