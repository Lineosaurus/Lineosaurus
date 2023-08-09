import os

from mykit.kit.text import num_approx
from mykit.kit.utils import sort_dict_by_val, get_first_n_dict_items

from src.constants import PB_CHAR, PB_LEN
from src.engine.card_maker import card_maker
from src.engine.counter import counter
from src.engine.pb_maker import progress_bars


# foo-bar-baz  124,211 lines  33%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
# foo-bar         5124 lines  11%  ▆▆▆▆▆▆▆▆▆▆▆▆▆
# foo              221 lines   8%  ▆▆▆▆▆▆▆▆
# foo-bar-baz       21 lines   3%  ▆▆


LANG = 'txt'


def get_entries(SHOW_APPROX, total, line_per_repo):

    entries = []
    
    for repo, num_lines in line_per_repo.items():

        if SHOW_APPROX:
            nline = num_approx(num_lines)
        else:
            nline = f'{num_lines:,}'

        entries.append([
            repo,
            f'{nline} lines',
            f'{round(100*num_lines/total)}%',
            progress_bars(num_lines, total, PB_CHAR, PB_LEN)
        ])
    
    return entries


def writer(NUM_SHOWN, SHOW_APPROX, card_title, line_per_repo):

    ## Total lines of code across owner's repositories
    total = sum(line_per_repo.values())
    
    ## Sort and cut
    line_per_repo = sort_dict_by_val(line_per_repo, reverse=True)
    line_per_repo = get_first_n_dict_items(line_per_repo, NUM_SHOWN)

    ## Make the card
    entries = get_entries(SHOW_APPROX, total, line_per_repo)
    align = [-1, 1, 1, -1]
    card = card_maker(card_title, entries, align, LANG)

    return card


def get_line_card(WORKSPACE_DIR, ONLY_TYPE, IGNORE_TYPE, NUM_SHOWN, SHOW_APPROX, card_title):

    line_per_repo = {}
    for repo in os.listdir(WORKSPACE_DIR):
        pth = os.path.join(WORKSPACE_DIR, repo)
        line_per_ext, _, _, _ = counter(ONLY_TYPE, IGNORE_TYPE, pth)
        line_per_repo[repo] = sum(line_per_ext.values())

    card = writer(NUM_SHOWN, SHOW_APPROX, card_title, line_per_repo)
    return card