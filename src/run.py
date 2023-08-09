import os
import re

from mykit.ghactions.eLog import eL

from src.constants import __version__
from src.get_options.get_options import get_options
from src.engine import engine


def get_readme(REPO_ROOT_DIR):
    eL.group('Search README')
    for i, j in enumerate(os.listdir(REPO_ROOT_DIR), 1):
        eL.debug(f'Searching for README attempt#{str(i).zfill(2)}: {repr(j)}')
        if re.match(r'^readme\.md$', j, re.IGNORECASE):
            eL.endgroup()
            return os.path.join(REPO_ROOT_DIR, j)
    raise FileNotFoundError('README.md not found.')


def run():
    eL.info(f'Lineosaurus v{__version__} is running.')

    REPO_ROOT_DIR = os.environ['GITHUB_WORKSPACE']
    WORKSPACE_DIR = os.path.abspath(os.path.join(REPO_ROOT_DIR, '..', 'lineosaurus-workspace'))

    ## Debugging purposes
    eL.group('Debug I')
    eL.debug(f'REPO_ROOT_DIR: {repr(REPO_ROOT_DIR)}.')
    eL.debug(f'OWNER: {repr(os.environ["GITHUB_ACTOR"])}.')

    ## Debugging purposes
    eL.group('Debug II')
    eL.debug(f'ONLY_TYPE . . . : {repr(os.environ["ONLY_TYPE"])}.')
    eL.debug(f'IGNORE_TYPE . . : {repr(os.environ["IGNORE_TYPE"])}.')
    eL.debug(f'HEADER  . . . . : {repr(os.environ["HEADER"])}.')
    eL.debug(f'FOOTER  . . . . : {repr(os.environ["FOOTER"])}.')
    eL.debug(f'CUSTOM_TITLE    : {repr(os.environ["CUSTOM_TITLE"])}.')
    eL.debug(f'NUM_SHOWN . . . : {repr(os.environ["NUM_SHOWN"])}.')
    eL.debug(f'SHOW_APPROX . . : {repr(os.environ["SHOW_APPROX"])}.')
    eL.debug(f'CARD_TITLES . . : {repr(os.environ["CARD_TITLES"])}.')
    eL.debug(f'CARD_ORDER  . . : {repr(os.environ["CARD_ORDER"])}.')
    eL.debug(f'PREFER_EXTENSION: {repr(os.environ["PREFER_EXTENSION"])}.')
    eL.debug(f'AUTO_LINE_BREAK : {repr(os.environ["AUTO_LINE_BREAK"])}.')
    eL.debug(f'SHOW_CREDIT . . : {repr(os.environ["SHOW_CREDIT"])}.')

    OPTIONS = get_options(
        os.environ['ONLY_TYPE'],
        os.environ['IGNORE_TYPE'],
        os.environ['HEADER'],
        os.environ['FOOTER'],
        os.environ['CUSTOM_TITLE'],
        os.environ['NUM_SHOWN'],
        os.environ['SHOW_APPROX'],
        os.environ['CARD_TITLES'],
        os.environ['CARD_ORDER'],
        os.environ['PREFER_EXTENSION'],
        os.environ['AUTO_LINE_BREAK'],
        os.environ['SHOW_CREDIT'],
    )

    ## Debugging purposes
    eL.group('Debug III')
    eL.debug(f'OPTIONS.ONLY_TYPE . . . : {repr(OPTIONS.ONLY_TYPE)}.')
    eL.debug(f'OPTIONS.IGNORE_TYPE . . : {repr(OPTIONS.IGNORE_TYPE)}.')
    eL.debug(f'OPTIONS.HEADER  . . . . : {repr(OPTIONS.HEADER)}.')
    eL.debug(f'OPTIONS.FOOTER  . . . . : {repr(OPTIONS.FOOTER)}.')
    eL.debug(f'OPTIONS.CUSTOM_TITLE    : {repr(OPTIONS.CUSTOM_TITLE)}.')
    eL.debug(f'OPTIONS.NUM_SHOWN . . . : {repr(OPTIONS.NUM_SHOWN)}.')
    eL.debug(f'OPTIONS.SHOW_APPROX . . : {repr(OPTIONS.SHOW_APPROX)}.')
    eL.debug(f'OPTIONS.CARD_TITLES . . : {repr(OPTIONS.CARD_TITLES)}.')
    eL.debug(f'OPTIONS.CARD_ORDER  . . : {repr(OPTIONS.CARD_ORDER)}.')
    eL.debug(f'OPTIONS.PREFER_EXTENSION: {repr(OPTIONS.PREFER_EXTENSION)}.')
    eL.debug(f'OPTIONS.AUTO_LINE_BREAK : {repr(OPTIONS.AUTO_LINE_BREAK)}.')
    eL.debug(f'OPTIONS.SHOW_CREDIT . . : {repr(OPTIONS.SHOW_CREDIT)}.')

    README = get_readme(REPO_ROOT_DIR)
    TEXT = engine(WORKSPACE_DIR, OPTIONS)

    with open(README, 'w') as f:
        f.write(TEXT)

    eL.info('README updated.')