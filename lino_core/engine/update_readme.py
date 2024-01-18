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
    ]
    return random.choice(l)

def update_readme(
    banner_pth:str|None,
    gh_actor:str,
    lines_of_code:int, nCommits:int, nChars:int,
    include_last_activity:bool, last_acts:dict,  # last_acts is {repo-name: last-commit-timestamp, ...}
    nickname:str,
    nCommits_last_week:int,
    lino_ver:str,
    readme_pth:str,
    include_credit:bool
):
    
#     text = """
# Hey there! Have a great Thursday! 🌈

# ![banner](https://github.com/nvfp/nvfp/raw/main/assets/banner.jpg)

# nvfp's repos (73,099 lines of code, 3,990 commits, 18,470,386 chars)

# ```python
# Repos I was working on lately: nvfp/nvfp.github.io (on Monday, Mar 3, 2024, 2:31PM utc+0), nvfp/nvfp.github.io (on Monday, Mar 3, 2024, 2:31PM utc+0), nvfp/nvfp.github.io (on Monday, Mar 3, 2024, 2:31PM utc+0)
# ```

# NVfp made 3 commits in the last week, what an awesome!

# <sub>last update: 2024 Jan 18 - Counted by [Lineosaurus(1.1)](https://github.com/Lineosaurus/Lineosaurus)</sub>
# """

    text = get_header(datetime.now().astimezone().strftime('%A')) + '\n\n'

    if banner_pth is not None:
        text += f"![banner]({banner_pth})\n\n"

    text += f"{gh_actor}'s repos ({lines_of_code:,} lines of code, {nCommits:,} commits, {nChars:,} chars)\n\n"

    if include_last_activity:
        act_list = []
        for name, ts in last_acts:
            d1 = datetime.fromtimestamp(ts).astimezone().strftime(random.choice(['%A, %b %-d, %Y, ', '%A, ', '%B %-d, ']))
            d2 = datetime.fromtimestamp(ts).astimezone().strftime(f"%I:%M%p{random.choice([' utc%z', ''])}").lstrip('0')
            # act_list.append(f"{name} ({datetime.fromtimestamp(ts).astimezone().strftime('%A, %b %d, %Y, %I:%M%p utc%z')})")
            act_list.append(f"{name} ({d1+d2})")
        text += (
            "```python\n"
            f"Repos I was working on lately: {', '.join(act_list)}"
            "```\n\n"
        )
    
    text += (
        f"{nickname} made {nCommits_last_week} commits in the last week, "
        # f"{random.choice(['what an awesome!', 'really great!', 'simply amazing!'])}"
        + random.choice(['what an awesome!', 'really great!', 'simply amazing!', 'incredibly impressive!'])
        + '\n\n'
    )

    # text += (
    #     f"<sub>last update: {datetime.now().astimezone().strftime(random.choice(['%Y %b %-d', '%Y %B %-d', '%b %-d, %Y']))} - "
    #     f"Counted by [Lineosaurus({lino_ver})](https://github.com/Lineosaurus/Lineosaurus)</sub>"
    # )
    ## vvvvv
    if include_credit:
        text += (
            f"<sub>last update: {datetime.now().astimezone().strftime(random.choice(['%Y %b %-d', '%Y %B %-d', '%b %-d, %Y']))} - "
            f"Counted by [Lineosaurus({lino_ver})](https://github.com/Lineosaurus/Lineosaurus)</sub>"
        )
    else:
        text += f"<sub>last update: {datetime.now().astimezone().strftime(random.choice(['%Y %b %-d', '%Y %B %-d', '%b %-d, %Y']))}</sub>"

    print('─'*100)
    print(text)
    print('─'*100)

    ## save
    print(f"INFO: Rewriting: >> {repr(readme_pth)} <<.")
    with open(readme_pth, 'w') as f:
        f.write(text)
