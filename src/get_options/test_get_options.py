import unittest

import os

from src.constants import CARDS
from src.get_options.get_options import get_options


class Test__get_options(unittest.TestCase):

    def test_only_type(self):
        
        ## Passes

        OPT = get_options(ONLY_TYPE='[".txt"]')
        self.assertEqual(OPT.ONLY_TYPE, ['.txt'])

        OPT = get_options(ONLY_TYPE='[".txt", ".json"]')
        self.assertEqual(OPT.ONLY_TYPE, ['.txt', '.json'])

        OPT = get_options(ONLY_TYPE='[".txt",".json",".py"]')
        self.assertEqual(OPT.ONLY_TYPE, ['.txt', '.json', '.py'])

        OPT = get_options(ONLY_TYPE='- .foo\n')
        self.assertEqual(OPT.ONLY_TYPE, ['.foo'])

        OPT = get_options(ONLY_TYPE='- .foo\n- .bar\n')
        self.assertEqual(OPT.ONLY_TYPE, ['.foo', '.bar'])

        OPT = get_options(ONLY_TYPE='-.foo\n-.bar\n')
        self.assertEqual(OPT.ONLY_TYPE, ['.foo', '.bar'])

        OPT = get_options(ONLY_TYPE='.foo\n')
        self.assertEqual(OPT.ONLY_TYPE, ['.foo'])

        OPT = get_options(ONLY_TYPE='.foo\n.bar\n')
        self.assertEqual(OPT.ONLY_TYPE, ['.foo', '.bar'])
        
        ## Fails

        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE='true')
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')

        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE="['x', 'y']")  # JSON uses double quotes
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')

        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE='{"a": 1}')
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')

        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE='[]')
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')

        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE='[1, 2, 3]')
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')

        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE='["a", "b"]')
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')
    
    def test_ignore_type(self):
        ## The same as only-type
        pass
    
    def test_header(self):
        
        OPT = get_options(HEADER='')
        self.assertEqual(OPT.HEADER, '')
        
        OPT = get_options(HEADER='## This is a header')
        self.assertEqual(OPT.HEADER, '## This is a header')

        OPT = get_options(HEADER='README.md')
        with open(os.path.join(os.environ['GITHUB_WORKSPACE'], 'README.md'), 'r') as f: text = f.read()
        self.assertEqual(OPT.HEADER, text)

        OPT = get_options(HEADER='tests/test_header.md')
        self.assertEqual(OPT.HEADER, '### This header text should be inside tests/test_header.md\n\n')
    
    def test_footer(self):
        ## The same as `header`
        pass
    
    def test_custom_title(self):
        pass

    def test_num_shown(self):
        
        ## Passes
        
        OPT = get_options(NUM_SHOWN='1')
        self.assertEqual(OPT.NUM_SHOWN, 1)

        OPT = get_options(NUM_SHOWN='10')
        self.assertEqual(OPT.NUM_SHOWN, 10)
        
        OPT = get_options(NUM_SHOWN='1000')
        self.assertEqual(OPT.NUM_SHOWN, 1000)
        
        ## Fails

        with self.assertRaises(AssertionError) as ctx: get_options(NUM_SHOWN='0')
        self.assertEqual(str(ctx.exception), 'Invalid num-shown value.')

        with self.assertRaises(AssertionError) as ctx: get_options(NUM_SHOWN='true')
        self.assertEqual(str(ctx.exception), 'Invalid num-shown value.')
    
    def test_show_approx(self):

        ## Passes

        OPT = get_options(SHOW_APPROX='true')
        self.assertEqual(OPT.SHOW_APPROX, True)
        
        OPT = get_options(SHOW_APPROX='false')
        self.assertEqual(OPT.SHOW_APPROX, False)
        
        ## Fails

        with self.assertRaises(AssertionError) as ctx: get_options(SHOW_APPROX='')
        self.assertEqual(str(ctx.exception), 'Invalid show-approx value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(SHOW_APPROX='123')
        self.assertEqual(str(ctx.exception), 'Invalid show-approx value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(SHOW_APPROX='[1, 2, 3]')
        self.assertEqual(str(ctx.exception), 'Invalid show-approx value.')
    
    def test_card_titles(self):

        ## Passes

        def _fn(x):
            d = {c: '' for c in CARDS}
            d.update(x)
            return d

        OPT = get_options(CARD_TITLES='{"line": "foo"}')
        self.assertEqual(OPT.CARD_TITLES, _fn({'line': 'foo'}))

        OPT = get_options(CARD_TITLES='{"line": "foo", "stat": "bar"}')
        self.assertEqual(OPT.CARD_TITLES, _fn({'line': 'foo', 'stat': 'bar'}))

        OPT = get_options(CARD_TITLES='{"size": "foo", "type": "bar"}')
        self.assertEqual(OPT.CARD_TITLES, _fn({'size': 'foo', 'type': 'bar'}))
        
        OPT = get_options(CARD_TITLES='{"line": "foo", "type": "bar", "stat": "# baz", "size": "**boo**"}')
        self.assertEqual(OPT.CARD_TITLES, _fn({'line': 'foo', 'type': 'bar', 'stat': '# baz', 'size': '**boo**'}))
        
        OPT = get_options(CARD_TITLES='{"size": "foo", "char": "bar", "star": "2", "cmit": "3"}')
        self.assertEqual(OPT.CARD_TITLES, _fn({'size': 'foo', 'char': 'bar', 'star': '2', 'cmit': '3'}))
        
        OPT = get_options(CARD_TITLES='- line: foo\n')
        self.assertEqual(OPT.CARD_TITLES, _fn({'line': 'foo'}))

        OPT = get_options(CARD_TITLES='- line: foo\n- stat: bar\n')
        self.assertEqual(OPT.CARD_TITLES, _fn({'line': 'foo', 'stat': 'bar'}))

        OPT = get_options(CARD_TITLES='- line: foo\n-  stat:  bar\n')
        self.assertEqual(OPT.CARD_TITLES, _fn({'line': 'foo', 'stat': 'bar'}))

        OPT = get_options(CARD_TITLES='-line:foo\n')
        self.assertEqual(OPT.CARD_TITLES, _fn({'line': 'foo'}))

        OPT = get_options(CARD_TITLES='line:foo\n')
        self.assertEqual(OPT.CARD_TITLES, _fn({'line': 'foo'}))

        ## Fails

        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='true')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='[1, 2]')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='{}')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='{"foo": "bar"}')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='{"line": "foo", "bar": "baz"}')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='{"line": 1}')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='foo\n')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='- foo: bar\n- baz\n')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='- foo: bar\n')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')

    def test_card_order(self):

        ## Passes

        OPT = get_options(CARD_ORDER='["line"]')
        self.assertEqual(OPT.CARD_ORDER, ['line'])
        
        OPT = get_options(CARD_ORDER='["line", "stat"]')
        self.assertEqual(OPT.CARD_ORDER, ['line', 'stat'])
        
        OPT = get_options(CARD_ORDER='["line", "type", "size", "stat", "char", "star", "cmit"]')
        self.assertEqual(OPT.CARD_ORDER, ['line', 'type', 'size', 'stat', 'char', 'star', 'cmit'])
        
        OPT = get_options(CARD_ORDER='line\n')
        self.assertEqual(OPT.CARD_ORDER, ['line'])
        
        OPT = get_options(CARD_ORDER='line\ntype\n')
        self.assertEqual(OPT.CARD_ORDER, ['line', 'type'])

        ## Fails

        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='true')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='{"a": 1}')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='[]')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='["foo"]')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='["line", "foo"]')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='["line", "type", "line"]')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='- foo\n')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')

        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='- line\n- line\n')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')

    def test_prefer_extension(self):
        ## The same as show-approx
        pass

    def test_auto_line_break(self):
        ## The same as show-approx
        pass

    def test_show_credit(self):
        ## The same as show-approx
        pass


if __name__ == '__main__':
    unittest.main()