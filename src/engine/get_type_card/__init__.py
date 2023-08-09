import os

from mykit.kit.text import num_approx
from mykit.kit.utils import sort_dict_by_val, get_first_n_dict_items

from src.constants import PB_CHAR, PB_LEN, TYPE_TO_NAME
from src.engine.card_maker import card_maker
from src.engine.counter import counter

"""
prefer-extension: true
----------------

124,211  lines of .py files   33%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
5124     lines of .txt files  11%  ▆▆▆▆▆▆▆▆▆▆▆▆▆
221      lines of .js files    8%  ▆▆▆▆▆▆▆▆
21       lines of .md files    3%  ▆▆


prefer-extension: false
----------------

124,211  lines of Python      33%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
5124     lines of Plain Text  11%  ▆▆▆▆▆▆▆▆▆▆▆▆▆
221      lines of JavaScript   8%  ▆▆▆▆▆▆▆▆
21       lines of Markdown     3%  ▆▆
"""


LANG = 'txt'


def get_entries(SHOW_APPROX, PREFER_EXTENSION, total, line_per_ext):

    entries = []

    for ext, num_lines in line_per_ext.items():

        if SHOW_APPROX:
            nline = num_approx(num_lines)
        else:
            nline = f'{num_lines:,}'

        if PREFER_EXTENSION:
            TYPE = f'{ext} files'
        else:
            TYPE = TYPE_TO_NAME[ext]

        entries.append([
            nline,
            f'lines of {TYPE}',
            f'{round(100*num_lines/total)}%',
            PB_CHAR*round(PB_LEN*num_lines/total)
        ])
    
    return entries


def writer(NUM_SHOWN, SHOW_APPROX, PREFER_EXTENSION, card_title, line_per_ext):

    ## Total lines of code across owner's repositories
    total = sum(line_per_ext.values())
    
    ## Sort and cut
    line_per_ext = sort_dict_by_val(line_per_ext, reverse=True)
    line_per_ext = get_first_n_dict_items(line_per_ext, NUM_SHOWN)

    ## Make the card
    entries = get_entries(SHOW_APPROX, PREFER_EXTENSION, total, line_per_ext)
    align = [-1, -1, 1, -1]
    card = card_maker(card_title, entries, align, LANG)

    return card


def get_type_card(WORKSPACE_DIR, ONLY_TYPE, IGNORE_TYPE, NUM_SHOWN, SHOW_APPROX, PREFER_EXTENSION, card_title):

    line_per_ext, _, _, _ = counter(ONLY_TYPE, IGNORE_TYPE, WORKSPACE_DIR)

    card = writer(NUM_SHOWN, SHOW_APPROX, PREFER_EXTENSION, card_title, line_per_ext)
    return card