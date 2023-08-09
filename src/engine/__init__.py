import os

from mykit.kit.text import num_round, num_approx
from mykit.kit.utils import sort_dict_by_val
from pyggc.git.simple import get_num_commits

from src.engine.get_line_card import get_line_card
from src.engine.get_type_card import get_type_card
from src.engine.get_size_card import get_size_card
from src.engine.get_stat_card import get_stat_card
from src.engine.get_char_card import get_char_card
from src.engine.get_star_card import get_star_card
from src.engine.get_cmit_card import get_cmit_card
from src.engine.get_file_card import get_file_card
from src.engine.variables_pool import Vars, replace_vars
from src.engine.counter import counter
from src.engine.assembler import assembler


def set_variables(WORKSPACE_DIR, OPTIONS):

    line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(None, None, WORKSPACE_DIR)

    TOTAL_LINES = sum(line_per_ext.values())
    Vars._LINES_ = TOTAL_LINES
    Vars._LINESFMT_ = f'{TOTAL_LINES:,}'
    Vars._LINESROUND_ = num_round(TOTAL_LINES)
    Vars._LINESAPPROX_ = num_approx(TOTAL_LINES)

    TOTAL_CHARS = sum(char_per_ext.values())
    Vars._CHARS_ = TOTAL_CHARS
    Vars._CHARSFMT_ = f'{TOTAL_CHARS:,}'
    Vars._CHARSROUND_ = num_round(TOTAL_CHARS)
    Vars._CHARSAPPROX_ = num_approx(TOTAL_CHARS)


    line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE, WORKSPACE_DIR)

    TOTAL_LINE = sum(line_per_ext.values())
    Vars._LINE_ = TOTAL_LINE
    Vars._LINEFMT_ = f'{TOTAL_LINE:,}'
    Vars._LINEROUND_ = num_round(TOTAL_LINE)
    Vars._LINEAPPROX_ = num_approx(TOTAL_LINE)


    commits = sort_dict_by_val(
        {
            repo: get_num_commits(os.path.join(WORKSPACE_DIR, repo))
            for repo in os.listdir(WORKSPACE_DIR)
        },
        reverse=True
    )
    TOTAL_COMMITS = sum(commits.values())
    Vars._CMIT_ = TOTAL_COMMITS
    Vars._CMITFMT_ = f'{TOTAL_COMMITS:,}'
    Vars._CMITROUND_ = num_round(TOTAL_COMMITS)
    Vars._CMITAPPROX_ = num_approx(TOTAL_COMMITS)


def card_factory(WORKSPACE_DIR, OPTIONS):

    cards = []

    for card in OPTIONS.CARD_ORDER:

        if card == 'line': cards.append(get_line_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.CARD_TITLES['line']
        ))

        if card == 'type': cards.append(get_type_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.PREFER_EXTENSION, OPTIONS.CARD_TITLES['type']
        ))

        if card == 'size': cards.append(get_size_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.NUM_SHOWN, OPTIONS.CARD_TITLES['size']
        ))

        if card == 'stat': cards.append(get_stat_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.CARD_TITLES['stat']
        ))

        if card == 'char': cards.append(get_char_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.PREFER_EXTENSION, OPTIONS.CARD_TITLES['char']
        ))

        if card == 'star': cards.append(get_star_card(
            OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.CARD_TITLES['star']
        ))

        if card == 'cmit': cards.append(get_cmit_card(
            WORKSPACE_DIR, OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.CARD_TITLES['cmit']
        ))

        if card == 'file': cards.append(get_file_card(
            WORKSPACE_DIR, OPTIONS.ONLY_TYPE, OPTIONS.IGNORE_TYPE,
            OPTIONS.NUM_SHOWN, OPTIONS.SHOW_APPROX, OPTIONS.CARD_TITLES['file']
        ))

    return '\n\n'.join(cards)


def engine(WORKSPACE_DIR, OPTIONS):

    set_variables(WORKSPACE_DIR, OPTIONS)

    header = replace_vars(OPTIONS.HEADER)
    custom_title = replace_vars(OPTIONS.CUSTOM_TITLE)
    OPTIONS.CARD_TITLES = {k: replace_vars(v) for k, v in OPTIONS.CARD_TITLES.items()}
    footer = replace_vars(OPTIONS.FOOTER)

    cards = card_factory(WORKSPACE_DIR, OPTIONS)

    return assembler(header, custom_title, cards, footer, OPTIONS.SHOW_CREDIT, OPTIONS.AUTO_LINE_BREAK)