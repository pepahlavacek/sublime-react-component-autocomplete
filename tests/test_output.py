import unittest
import os
import re
from ReactComponentAutocomplete.output import *

import sublime
import sys

version = sublime.version()

class TestOutput(unittest.TestCase):

    # test jsx parsing
    def test_string(self):
        # result = get_value_for_type("string", "JSX")
        
        self.assertEqual('""', '""')

if __name__ == '__main__':
  unittest.main()