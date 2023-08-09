import os
import re

from src.constants import CARDS
from src.get_options.yml_custom_parser import parse_dict, parse_list


r"""
Notes:

In both of these cases, the value field is empty:
foo: |

bar: |-


`foo` and `bar` values will be evaluated as an empty string.


Extra note: for custom-title, "|-" is recommended because it doesn't include the ending '\n'.
Extra note: `foo: '[.txt, .md, .json]'` is invalid.
"""


## The default values are given for testing purposes
def get_options(
    ONLY_TYPE='',
    IGNORE_TYPE='',
    HEADER='',
    FOOTER='',
    CUSTOM_TITLE='',
    NUM_SHOWN='5',
    SHOW_APPROX='true',
    CARD_TITLES='',
    CARD_ORDER='',
    PREFER_EXTENSION='true',
    AUTO_LINE_BREAK='true',
    SHOW_CREDIT='true',
):
    
    REPO_ROOT_DIR = os.environ['GITHUB_WORKSPACE']

    class OPTIONS: ...

    ## only-type
    if ONLY_TYPE == '':  # If `null` in YAML
        OPTIONS.ONLY_TYPE = None
    else:
        try:
            only_type = parse_list(ONLY_TYPE)
        except SyntaxError:
            raise AssertionError('Invalid only-type value.')
        if (type(only_type) is not list) or (len(only_type) == 0):
            raise AssertionError('Invalid only-type value.')
        for i in only_type:
            if type(i) is not str:
                raise AssertionError('Invalid only-type value.')
            if not re.match(r'^\.\w+$', i):
                raise AssertionError('Invalid only-type value.')
        OPTIONS.ONLY_TYPE = only_type

    ## ignore-type
    if IGNORE_TYPE == '':
        OPTIONS.IGNORE_TYPE = None
    else:
        try:
            ignore_type = parse_list(IGNORE_TYPE)
        except SyntaxError:
            raise AssertionError('Invalid ignore-type value.')
        if (type(ignore_type) is not list) or (len(ignore_type) == 0):
            raise AssertionError('Invalid ignore-type value.')
        for i in ignore_type:
            if type(i) is not str:
                raise AssertionError('Invalid ignore-type value.')
            if not re.match(r'^\.\w+$', i):
                raise AssertionError('Invalid ignore-type value.')
        OPTIONS.IGNORE_TYPE = ignore_type
    
    ## header
    OPTIONS.HEADER = HEADER
    ## Use 'normpath' for Windows (converts '/' to '\'),
    ## and for Linux (case-sensitive paths), prefer 'normpath' over 'normcase'.
    header = os.path.join(REPO_ROOT_DIR, os.path.normpath(HEADER))
    if os.path.isfile(header):
        with open(header, 'r') as f:
            OPTIONS.HEADER = f.read()

    ## footer
    OPTIONS.FOOTER = FOOTER
    footer = os.path.join(REPO_ROOT_DIR, os.path.normpath(FOOTER))
    if os.path.isfile(footer):
        with open(footer, 'r') as f:
            OPTIONS.FOOTER = f.read()

    ## custom-title
    OPTIONS.CUSTOM_TITLE = CUSTOM_TITLE

    ## num-shown
    try:
        num_shown = int(NUM_SHOWN)
        if num_shown < 1:
            raise AssertionError('Invalid num-shown value.')
        OPTIONS.NUM_SHOWN = num_shown
    except ValueError:
        raise AssertionError('Invalid num-shown value.')

    ## show-approx
    if SHOW_APPROX == 'true': OPTIONS.SHOW_APPROX = True
    elif SHOW_APPROX == 'false': OPTIONS.SHOW_APPROX = False
    else: raise AssertionError('Invalid show-approx value.')

    ## card-titles
    OPTIONS.CARD_TITLES = {c: '' for c in CARDS}
    if CARD_TITLES == '': pass
    else:
        try:
            card_titles = parse_dict(CARD_TITLES)
        except SyntaxError:
            raise AssertionError('Invalid card-titles value.')
        if (type(card_titles) is not dict) or (len(card_titles) == 0):
            raise AssertionError('Invalid card-titles value.')
        for k, v in card_titles.items():
            if (k not in CARDS) or (type(v) is not str):
                raise AssertionError('Invalid card-titles value.')
        OPTIONS.CARD_TITLES.update(card_titles)

    ## card-order
    if CARD_ORDER == '':
        OPTIONS.CARD_ORDER = []
    else:
        try:
            card_order = parse_list(CARD_ORDER)
        except SyntaxError:
            raise AssertionError('Invalid card-order value.')
        if (type(card_order) is not list) or (len(card_order) == 0):
            raise AssertionError('Invalid card-order value.')
        for i in card_order:
            if i not in CARDS:
                raise AssertionError('Invalid card-order value.')
        if len(card_order) != len(set(card_order)):
            raise AssertionError('Invalid card-order value.')  # Has duplicates
        OPTIONS.CARD_ORDER = card_order

    ## prefer-extension
    if PREFER_EXTENSION == 'true': OPTIONS.PREFER_EXTENSION = True
    elif PREFER_EXTENSION == 'false': OPTIONS.PREFER_EXTENSION = False
    else: raise AssertionError('Invalid prefer-extension value.')

    ## auto-line-break
    if AUTO_LINE_BREAK == 'true': OPTIONS.AUTO_LINE_BREAK = True
    elif AUTO_LINE_BREAK == 'false': OPTIONS.AUTO_LINE_BREAK = False
    else: raise AssertionError('Invalid auto-line-break value.')

    ## show-credit
    if SHOW_CREDIT == 'true': OPTIONS.SHOW_CREDIT = True
    elif SHOW_CREDIT == 'false': OPTIONS.SHOW_CREDIT = False
    else: raise AssertionError('Invalid show-credit value.')

    return OPTIONS