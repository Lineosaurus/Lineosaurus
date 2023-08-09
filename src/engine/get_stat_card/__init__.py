import os

from mykit.kit.text import num_approx, in_byte
from mykit.kit.utils import sort_dict_by_val, get_first_n_dict_items
from pyggc.ghcli.simple import total_stargazers
from pyggc.git.simple import get_num_commits

from src.constants import TYPE_TO_NAME
from src.engine.card_maker import card_maker
from src.engine.counter import counter


"""
number of repo     132
top language       Python, JavaScript, and Shell
lines of code      213,231
total size         141 MiB
number of chars    231K
number of stars    32
number of commits  141,241
number of files    231K
"""


LANG = 'txt'


def get_top3_lang(char_per_ext):
    """Using the number of characters as an indicator of the top used language"""
    
    ## Sort
    char_per_ext = sort_dict_by_val(char_per_ext, reverse=True)

    ## Exclude the non-languages
    char_per_ext = {k:v for k,v in char_per_ext.items() if k in TYPE_TO_NAME}

    ## Cut
    char_per_ext = get_first_n_dict_items(char_per_ext, 3)

    exts = list(char_per_ext.keys())
    lang1 = TYPE_TO_NAME[exts[0]]
    lang2 = TYPE_TO_NAME[exts[1]]
    lang3 = TYPE_TO_NAME[exts[2]]
    return f'{lang1}, {lang2}, and {lang3}'


def get_total_commits(WORKSPACE_DIR):
    
    n = 0

    for repo in os.listdir(WORKSPACE_DIR):
        repo_path = os.path.join(WORKSPACE_DIR, repo)
        n += get_num_commits(repo_path)

    return f'{n:,}'


def get_stat_card(WORKSPACE_DIR, ONLY_TYPE, IGNORE_TYPE, card_title):

    OWNER = os.environ['GITHUB_ACTOR']

    line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(ONLY_TYPE, IGNORE_TYPE, WORKSPACE_DIR)

    ## Make the card
    entries = [
        ['number of repo', f'{len(os.listdir(WORKSPACE_DIR)):,}'],
        ['top language', get_top3_lang(char_per_ext)],
        ['lines of code', f'{sum(line_per_ext.values()):,}'],
        ['total size', in_byte(sum(size_per_ext.values()))],
        ['number of chars', f'{sum(char_per_ext.values()):,}'],
        ['number of stars', f'{total_stargazers(OWNER):,} 🌟'],
        ['number of commits', get_total_commits(WORKSPACE_DIR)],
        ['number of files', f'{sum(file_per_ext.values()):,}'],
    ]
    align = [-1, -1]
    card = card_maker(card_title, entries, align, LANG)

    return card