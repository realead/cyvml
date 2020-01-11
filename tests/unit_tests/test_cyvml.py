
import unittest

import cyvml.cyvml as t


class cyvmlTester(unittest.TestCase): 

   def test_test_me(self):
      self.assertEqual(t.test_me(), 42)
