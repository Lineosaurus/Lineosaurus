import json
import os
import shutil
import tempfile

from mykit.ghactions.eLog import eL
from pyggc.git.simple import clone

from src.constants import __version__
from src.get_options.get_options import get_options
from src.engine import engine


DEFAULT = {
    'only-type': '',
    'ignore-type': '',
    'header': '',
    'footer': '',
    'custom-title': '',
    'num-shown': '3',
    'show-approx': 'true',
    'card-titles': '',
    'card-order': '',
    'prefer-extension': 'true',
    'auto-line-break': 'true',
    'show-credit': 'true',
}


def emulator(setup):
    eL.info(f'Running emulator v{__version__}.')
    eL.debug(f'setup: {repr(setup)}.')

    ## Check and read
    setup_pth = os.path.join(os.environ['GITHUB_WORKSPACE'], os.path.normpath(setup))
    if not (os.path.isfile(setup_pth) and setup.endswith('.json')): raise AssertionError(f'Invalid setup path: {repr(setup)}.')
    with open(setup_pth, 'r') as f: setup_json = json.load(f)

    workspace_dir = tempfile.mkdtemp()

    eL.group('Parsing setup options')
    setup_options = []
    for option_name, option_default in DEFAULT.items():
        if option_name in setup_json['options']:
            setup_options.append(setup_json['options'][option_name])
        else:
            setup_options.append(option_default)
    eL.info(f'setup_options: {setup_options}')
    eL.endgroup()

    try:
        eL.group('Cloning')
        for url in setup_json['workspace']['urls']:
            clone(url, workspace_dir)
        eL.endgroup()

        eL.group('Emulate')
        options = get_options(*setup_options)
        text = engine(workspace_dir, options)
        eL.endgroup()
    finally:
        eL.error('Something went wrong.')
        shutil.rmtree(workspace_dir)

    print(text)
    print