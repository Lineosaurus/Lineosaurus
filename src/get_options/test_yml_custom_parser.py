import unittest

from src.get_options.yml_custom_parser import parse_dict, parse_list, parse_dict_advance


class Test__yml_custom_parser(unittest.TestCase):

    def test_parse_dict(self):

        ## Passes

        result = parse_dict('{"x": "foo", "y": "bar"}')
        expected = {"x": "foo", "y": "bar"}
        self.assertEqual(result, expected)

        result = parse_dict('- x: foo\n- y: bar\n')
        expected = {"x": "foo", "y": "bar"}
        self.assertEqual(result, expected)

        result = parse_dict('- x: foo\n')
        expected = {"x": "foo"}
        self.assertEqual(result, expected)

        result = parse_dict('-  x:  foo\n')
        expected = {"x": "foo"}
        self.assertEqual(result, expected)

        result = parse_dict('-x:foo\n')
        expected = {"x": "foo"}
        self.assertEqual(result, expected)

        result = parse_dict('x:foo\n')
        expected = {"x": "foo"}
        self.assertEqual(result, expected)

        ## Fails

        with self.assertRaises(SyntaxError) as ctx: parse_dict('x\n')
        self.assertEqual(str(ctx.exception), r"Failed to parse 'x\n'.")

    def test_parse_list(self):

        ## Passes

        result = parse_list('["x", "y"]')
        expected = ['x', 'y']
        self.assertEqual(result, expected)

        result = parse_list('- x\n- y\n')
        expected = ['x', 'y']
        self.assertEqual(result, expected)

        result = parse_list('- x\n')
        expected = ['x']
        self.assertEqual(result, expected)

        result = parse_list('-  x\n')
        expected = ['x']
        self.assertEqual(result, expected)

        result = parse_list('-x\n')
        expected = ['x']
        self.assertEqual(result, expected)

        result = parse_list('x\n')
        expected = ['x']
        self.assertEqual(result, expected)

        ## Fails

        with self.assertRaises(SyntaxError) as ctx: parse_list("['x', 'y']")  # JSON uses double quotes
        self.assertEqual(str(ctx.exception), """Invalid syntax for "['x', 'y']".""")


class Test__parse_dict_advance(unittest.TestCase):

    def test(self):

        ## Passes

        result = parse_dict_advance('- foobar-bazqux: https://foo.com/bar/baz.png\n- abc-xyz: foo bar baz')
        expected = {'foobar-bazqux': 'https://foo.com/bar/baz.png', 'abc-xyz': 'foo bar baz'}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()