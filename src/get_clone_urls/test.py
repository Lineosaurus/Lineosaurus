import unittest

from src.get_clone_urls import get_clone_urls


class Test__get_clone_urls(unittest.TestCase):

    def test_normal(self):
        raw = '[{"url":"https://github.com/foo/bar"},{"url":"https://github.com/foo/baz"}]'
        result = get_clone_urls(raw)
        expected = ['https://github.com/foo/bar.git', 'https://github.com/foo/baz.git']
        self.assertEqual(result, expected)

    def test_empty(self):
        raw = '[]'
        result = get_clone_urls(raw)
        expected = []
        self.assertEqual(result, expected)

    def test_formatted(self):
        raw = '[{"url": "https://github.com/foo/bar"}, {"url": "https://github.com/foo/baz"}]'
        result = get_clone_urls(raw)
        expected = ['https://github.com/foo/bar.git', 'https://github.com/foo/baz.git']
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()