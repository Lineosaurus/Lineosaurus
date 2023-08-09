import os

from mykit.kit.text import in_byte
from mykit.kit.utils import sort_dict_by_val, get_first_n_dict_items

from src.constants import PB_CHAR, PB_LEN
from src.engine.card_maker import card_maker
from src.engine.counter import counter


"""
foo-bar-baz  124 MiB  33%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
foo-bar        5 MiB  11%  ▆▆▆▆▆▆▆▆▆▆▆▆▆
foo          221 KiB   8%  ▆▆▆▆▆▆▆▆
foobaz          21 B   3%  ▆▆
"""


LANG = 'txt'


def get_entries(total, size_per_repo):

    entries = []

    for repo, size in size_per_repo.items():

        entries.append([
            repo,
            in_byte(size, precision=0),
            f'{round(100*size/total)}%',
            PB_CHAR*round(PB_LEN*size/total)
        ])

    return entries


def writer(NUM_SHOWN, card_title, size_per_repo):

    ## Total lines of code across owner's repositories
    total = sum(size_per_repo.values())
    
    ## Sort and cut
    size_per_repo = sort_dict_by_val(size_per_repo, reverse=True)
    size_per_repo = get_first_n_dict_items(size_per_repo, NUM_SHOWN)

    ## Make the card
    entries = get_entries(total, size_per_repo)
    align = [-1, 1, 1, -1]
    card = card_maker(card_title, entries, align, LANG)

    return card


def get_size_card(WORKSPACE_DIR, ONLY_TYPE, IGNORE_TYPE, NUM_SHOWN, card_title):

    size_per_repo = {}
    for repo in os.listdir(WORKSPACE_DIR):
        pth = os.path.join(WORKSPACE_DIR, repo)
        _, size_per_ext, _, _ = counter(ONLY_TYPE, IGNORE_TYPE, pth)
        size_per_repo[repo] = sum(size_per_ext.values())

    card = writer(NUM_SHOWN, card_title, size_per_repo)
    return card