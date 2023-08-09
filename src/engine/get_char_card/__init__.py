from mykit.kit.text import num_approx
from mykit.kit.utils import sort_dict_by_val, get_first_n_dict_items

from src.constants import PB_CHAR, PB_LEN, TYPE_TO_NAME
from src.engine.card_maker import card_maker
from src.engine.counter import counter


"""
prefer-extension: true
----------------

15.3K  characters of .py files   33%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
5.3K   characters of .txt files  11%  ▆▆▆▆▆▆▆▆▆▆▆▆▆
221    characters of .js files    8%  ▆▆▆▆▆▆▆▆
21     characters of .md files    3%  ▆▆


prefer-extension: false
----------------

15.3K  characters of Python      33%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
5.3K   characters of Plain Text  11%  ▆▆▆▆▆▆▆▆▆▆▆▆▆
221    characters of JavaScript   8%  ▆▆▆▆▆▆▆▆
21     characters of Markdown     3%  ▆▆
"""


LANG = 'txt'


def get_entries(SHOW_APPROX, PREFER_EXTENSION, total, char_per_ext):

    entries = []

    for ext, num_chars in char_per_ext.items():

        if SHOW_APPROX:
            nline = num_approx(num_chars)
        else:
            nline = f'{num_chars:,}'

        if PREFER_EXTENSION:
            TYPE = f'{ext} files'
        else:
            TYPE = TYPE_TO_NAME[ext]

        entries.append([
            nline,
            f'characters of {TYPE}',
            f'{round(100*num_chars/total)}%',
            PB_CHAR*round(PB_LEN*num_chars/total)
        ])

    return entries


def writer(NUM_SHOWN, SHOW_APPROX, PREFER_EXTENSION, card_title, char_per_ext):

    ## Total characters per file extension across owner's repositories
    total = sum(char_per_ext.values())
    
    ## Sort and cut
    char_per_ext = sort_dict_by_val(char_per_ext, reverse=True)
    char_per_ext = get_first_n_dict_items(char_per_ext, NUM_SHOWN)

    ## Make the card
    entries = get_entries(SHOW_APPROX, PREFER_EXTENSION, total, char_per_ext)
    align = [-1, -1, 1, -1]
    card = card_maker(card_title, entries, align, LANG)

    return card


def get_char_card(WORKSPACE_DIR, ONLY_TYPE, IGNORE_TYPE, NUM_SHOWN, SHOW_APPROX, PREFER_EXTENSION, card_title):

    _, _, char_per_ext, _ = counter(ONLY_TYPE, IGNORE_TYPE, WORKSPACE_DIR)

    card = writer(NUM_SHOWN, SHOW_APPROX, PREFER_EXTENSION, card_title, char_per_ext)
    return card