import unittest
import numpy as np
import cyvml.cyvml as vml


class cyvmlTester(unittest.TestCase): 

   def test_vdCos(self):
      x = np.array([np.pi*2], dtype=np.float64)
      y = np.array([42.42], dtype=np.float64)
      vml.py_vdCos(x,y)
      self.assertAlmostEqual(y[0], 1.0)

   def test_vdSin(self):
      x = np.array([np.pi/2.0], dtype=np.float64)
      y = np.array([42.42], dtype=np.float64)
      vml.py_vdSin(x,y)
      self.assertAlmostEqual(y[0], 1.0)


   def test_vdExp(self):
      x = np.array([1.0], dtype=np.float64)
      y = np.array([42.42], dtype=np.float64)
      vml.py_vdExp(x,y)
      self.assertAlmostEqual(y[0], np.e)

   def test_vdLn(self):
      x = np.array([1.0], dtype=np.float64)
      y = np.array([42.42], dtype=np.float64)
      vml.py_vdLn(x,y)
      self.assertAlmostEqual(y[0], 0.0)



# should be last...
   def test_get_set_threads(self):
      self.assertEqual(vml.py_set_vml_num_threads(1), 1)
      self.assertEqual(vml.py_get_vml_max_num_threads(), 1)
      self.assertEqual(vml.py_set_vml_num_threads(2), 1)
      self.assertEqual(vml.py_get_vml_max_num_threads(), 2)

