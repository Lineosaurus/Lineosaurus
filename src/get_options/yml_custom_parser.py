import json
import re


r"""
Note:

USE
foo: |
  - x

NOT
foo: |-
  - x

Since the extra "\n" at the end is useful for the parser.
"""


def parse_dict(raw_str):
    
    """
    When users use:
    foo: '{"x": "foo", "y": "bar"}'
    """
    if '\n' not in raw_str:
        try:
            return json.loads(raw_str)
        except json.decoder.JSONDecodeError:
            raise SyntaxError(f'Invalid syntax for {repr(raw_str)}.')

    """
    When users use:

    with_spaces: |
      - x: foo
      - y: bar
    without_spaces: |
      -x: foo
      -y: bar
    without_hyphen: |
      x: foo
      y: bar
    """
    d = {}
    for line in raw_str.split('\n'):
        if line == '': continue  # Handle the ending '\n'
        res = re.search(r'^-?[ ]*(?P<key>\w+):[ ]*(?P<val>.+)$', line)
        if res is None: raise SyntaxError(f'Failed to parse {repr(raw_str)}.')
        d[res.group('key')] = res.group('val')
    return d


def parse_list(raw_str):

    """
    When users use:
    foo: '["x", "y", "z"]'
    """
    if '\n' not in raw_str:
        try:
            return json.loads(raw_str)
        except json.decoder.JSONDecodeError:
            raise SyntaxError(f'Invalid syntax for {repr(raw_str)}.')

    """
    When users use:

    with_spaces: |
      - x
      - y
      - z
    without_spaces: |
      -x
      -y
      -z
    without_hyphen: |
      x
      y
      z
    """
    l = []
    for line in raw_str.split('\n'):
        if line == '': continue  # Handle the ending '\n'
        res = re.search(r'^-?[ ]*(?P<val>.+)$', line)
        if res is None: raise SyntaxError(f'Failed to parse {repr(raw_str)}.')
        l.append(res.group('val'))
    return l