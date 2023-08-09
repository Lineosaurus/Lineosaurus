import unittest

import json
import os

from pyggc.git.simple import clone

from src.engine import engine


## Don't be confused with $GITHUB_WORKSPACE: when users run the action.yml,
## $GITHUB_WORKSPACE will become the root directory of the users' repo.
## However, when the workflow runs the run-tests.yml,
## $GITHUB_WORKSPACE becomes the root directory of the Lineosaurus repo.
##
## Extra note: we can get the path to Lineosaurus repo root dir (when users run action.yml) using $GITHUB_ACTION_PATH
DIR = os.path.join(os.environ['GITHUB_WORKSPACE'])


class Clone:
    workspace = None
    cloned = False
    def clone():
        if not Clone.cloned:
            Clone.cloned = True


class Test__engine(unittest.TestCase):

    def test_20230809_1(self):
        return
        class OPTIONS:
            pass
        result = engine(Clone.workspace, OPTIONS)
        expected = """
ascc
ac
sc
sa
c
s
"""
        self.assertEqual(result, expected.strip())


if __name__ == '__main__':
    unittest.main()