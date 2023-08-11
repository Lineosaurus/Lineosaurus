import argparse
import os
import sys

from mykit.ghactions.eLog import eL

## Make all dirs under the project's root dir importable
try:
    sys.path.append(os.environ['GITHUB_ACTION_PATH'])
except KeyError:  # During emulation
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.get_clone_urls import get_clone_urls
from src.run import run
from src.emulator import emulator


def main():

    p = argparse.ArgumentParser()
    p.add_argument('--log-level', choices=['quiet', 'debug'], default='debug')

    s = p.add_subparsers(dest='cmd')

    x = s.add_parser('get-clone-urls')
    x.add_argument('raw')

    x = s.add_parser('run')

    x = s.add_parser('emulate')
    x.add_argument('setup')

    args = p.parse_args()

    eL.set_level(args.log_level)

    if args.cmd == 'get-clone-urls':
        print(' '.join(get_clone_urls(args.raw)))  # Output the result to the shell
    elif args.cmd == 'run':
        run()
    elif args.cmd == 'emulate':
        emulator(args.setup)


if __name__ == '__main__':
    main()