import unittest

from mykit.ghactions.eLog import eL


## Created just to silence the logger during testing.
## TODO: To silence the logger, don't do it this way as it lacks clarity and flexibility.
class Test__do_silent(unittest.TestCase):

    def test_nothing(self):

        eL.set_level('quiet')


if __name__ == '__main__':
    unittest.main()