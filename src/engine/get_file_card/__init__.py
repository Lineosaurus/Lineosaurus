import os

from mykit.kit.text import num_approx
from mykit.kit.utils import sort_dict_by_val, get_first_n_dict_items

from src.constants import PB_CHAR, PB_LEN, TYPE_TO_NAME
from src.engine.card_maker import card_maker
from src.engine.counter import counter


"""
foo-bar       324 files  33%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
foo             2 files  11%  ▆▆▆▆▆▆▆▆▆▆▆▆▆
fooo           11 files   8%  ▆▆▆▆▆▆▆▆
foo-bar-baz  3.5K files   3%  ▆▆
"""


LANG = 'txt'


def get_entries(SHOW_APPROX, total, file_per_repo):

    entries = []

    for repo, num_files in file_per_repo.items():

        if SHOW_APPROX:
            nfile = num_approx(num_files)
        else:
            nfile = f'{num_files:,}'

        entries.append([
            repo,
            f'{nfile} files',
            f'{round(100*num_files/total)}%',
            PB_CHAR*round(PB_LEN*num_files/total)
        ])

    return entries


def writer(NUM_SHOWN, SHOW_APPROX, card_title, file_per_repo):

    ## Total lines of code across owner's repositories
    total = sum(file_per_repo.values())

    ## Sort and cut
    file_per_repo = sort_dict_by_val(file_per_repo, reverse=True)
    file_per_repo = get_first_n_dict_items(file_per_repo, NUM_SHOWN)

    ## Make the card
    entries = get_entries(SHOW_APPROX, total, file_per_repo)
    align = [-1, 1, 1, -1]
    card = card_maker(card_title, entries, align, LANG)

    return card


def get_file_card(WORKSPACE_DIR, ONLY_TYPE, IGNORE_TYPE, NUM_SHOWN, SHOW_APPROX, card_title):

    file_per_repo = {}
    for repo in os.listdir(WORKSPACE_DIR):
        pth = os.path.join(WORKSPACE_DIR, repo)
        _, _, _, file_per_ext = counter(ONLY_TYPE, IGNORE_TYPE, pth)
        file_per_repo[repo] = sum(file_per_ext.values())

    card = writer(NUM_SHOWN, SHOW_APPROX, card_title, file_per_repo)
    return card