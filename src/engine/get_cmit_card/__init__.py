import os

from mykit.kit.text import num_approx
from mykit.kit.utils import sort_dict_by_val, get_first_n_dict_items
from pyggc.git.simple import get_num_commits

from src.constants import PB_LEN, PB_CHAR
from src.engine.card_maker import card_maker


"""
foo-bar-baz  124,211 commits  33%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
foo-bar         5124 commits  11%  ▆▆▆▆▆▆▆▆
foo              221 commits   8%  ▆▆▆▆▆▆
foo-bar-baz       21 commits   3%  ▆
"""


LANG = 'txt'


def get_entries(SHOW_APPROX, total, cmit_per_repo):
    
    entries = []
    
    for repo, num_commits in cmit_per_repo.items():
        
        if SHOW_APPROX:
            ncommit = num_approx(num_commits)
        else:
            ncommit = f'{num_commits:,}'

        entries.append([
            repo,
            f'{ncommit} commits',
            f'{round(100*num_commits/total)}%',
            PB_CHAR*round(PB_LEN*num_commits/total)
        ])

    return entries


## A unit test will be created for this function
def writer(NUM_SHOWN, SHOW_APPROX, card_title, cmit_per_repo):

    ## Total commits across owner's repositories
    total = sum(cmit_per_repo.values())
    
    ## Sort and cut
    cmit_per_repo = sort_dict_by_val(cmit_per_repo, reverse=True)
    cmit_per_repo = get_first_n_dict_items(cmit_per_repo, NUM_SHOWN)

    ## Make the card
    entries = get_entries(SHOW_APPROX, total, cmit_per_repo)
    align = [-1, 1, 1, -1]
    card = card_maker(card_title, entries, align, LANG)

    return card


def get_cmit_card(WORKSPACE_DIR, NUM_SHOWN, SHOW_APPROX, card_title):

    cmit_per_repo = {}
    for repo in os.listdir(WORKSPACE_DIR):
        repo_path = os.path.join(WORKSPACE_DIR, repo)
        cmit_per_repo[repo] = get_num_commits(repo_path)

    card = writer(NUM_SHOWN, SHOW_APPROX, card_title, cmit_per_repo)
    return card