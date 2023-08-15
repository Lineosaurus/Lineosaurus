import random
from datetime import datetime


def get_random_hello(day):
    l = [
        f"Wish you an awesome {day}! 🌼",
        f"Smile, it's {day}! ☀️",
        f"Hey there! Have a great {day}! 🌈",
        f"Wishing you an amazing {day}! 🎉",
        f"May your {day} be wonderful! 🌸",
        f"Have a fantastic {day}! 🌹",
        f"Smile, it's a beautiful {day}! 🌺",
        f"Keep shining on this {day}! 🌷",
    ]
    return random.choice(l)


def main(banner_path, banner_alt):

    day = datetime.now().strftime('%A')
    
    header = get_random_hello(day) + '\n\n'

    if banner_path != '':
        header += f'![{banner_alt}]({banner_path})\n\n'
    else:
        header += ''
    header += "_OWNER_'s repos (_LINESFMT_ lines of code, _CMITFMT_ commits, _CHARSFMT_ chars)"

    OPTIONS = {
        'HEADER': header,
        'FOOTER': '<sub>last update: _DATE_ - _CREDIT_</sub>',
        'CARD_ORDER': 'cmit\n',
        'SHOW_CREDIT': 'false',
    }

    return OPTIONS