import unittest
#python -m unittest discover -t topdir -s test dir -p test*.py -v

from filters import nameFilter
from argparse import Namespace

class TestNameFilter(unittest.TestCase):

    
    #test name filter
    def test_regex_false(self):
        args = Namespace(name = "test.js",regex=False)
        ffname = "test.js"
        self.assertTrue(nameFilter(args=args,ffname=ffname))


    def test_regex_true(self):
        args = Namespace(name = "^test",regex=True)
        ffname = "test.js"
        self.assertTrue(nameFilter(args=args,ffname=ffname))