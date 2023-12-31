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
MAP = {  # MAP is required because src/get_options/get_options.py args must be in string (currently)
    None: '',
    True: 'true',
    False: 'false',
}


"""
Human interaction may be needed for integration testing in the case of final rendered text.

The process involves:
1. First, we perform emulation to get the emulated result from the current engine state.
2. Next, we approve or disapprove the emulation result.
3. Once approved, we add the emulation result to the integration tests.
   We use the `emulation_engine` to check the emulated result and make sure it stays the same.
"""


def emulator_engine(setup):
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
            val = setup_json['options'][option_name]
            if val in MAP: val = MAP[val]
            setup_options.append(str(val))
        else:
            setup_options.append(option_default)
    eL.info(f'setup_options: {setup_options}')
    eL.endgroup()

    try:
        eL.group('Cloning')
        for url in setup_json['workspace']['urls']:
            clone(url, workspace_dir)

        eL.group('Emulate')
        options = get_options(*setup_options)
        text = engine(workspace_dir, options)
        eL.endgroup()
    finally:
        eL.debug('Cleaning up.')
        shutil.rmtree(workspace_dir)

    return text


def emulator(setup):
    """Display the emulated result in the terminal (used in GitHub Actions VM)"""
    eL.info(f'Running emulator v{__version__}.')

    text = emulator_engine(setup)

    eL.group('text')
    eL.info(text)
    eL.group('repr(text)')
    eL.info(repr(text))