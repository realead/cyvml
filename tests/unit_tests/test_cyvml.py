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

   def test_vdTan(self):
      x = np.array([np.pi/4.0], dtype=np.float64)
      y = np.array([42.42], dtype=np.float64)
      vml.py_vdTan(x,y)
      self.assertAlmostEqual(y[0], 1.0)

   def test_vdAcos(self):
      x = np.array([1.0], dtype=np.float64)
      y = np.array([42.42], dtype=np.float64)
      vml.py_vdAcos(x,y)
      self.assertAlmostEqual(y[0], 0.0)

   def test_vdAsin(self):
      x = np.array([1.0], dtype=np.float64)
      y = np.array([42.42], dtype=np.float64)
      vml.py_vdAsin(x,y)
      self.assertAlmostEqual(y[0], np.pi/2.0)

   def test_vdAtan(self):
      x = np.array([1.0], dtype=np.float64)
      y = np.array([42.42], dtype=np.float64)
      vml.py_vdAtan(x,y)
      self.assertAlmostEqual(y[0], np.pi/4)


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

   def test_get_set_threads_local(self):
      old = vml.py_mkl_set_num_threads_local(3)
      self.assertEqual(vml.py_mkl_set_num_threads_local(old), 3)
      self.assertEqual(vml.py_mkl_set_num_threads_local(old), old)

   def test_get_set_mode(self):
      vml.py_vmlSetMode(vml.PY_VML_EP)
      self.assertEqual(vml.py_vmlGetMode()&3, 3)
      vml.py_vmlSetMode(vml.PY_VML_LA)
      self.assertEqual(vml.py_vmlGetMode()&3, 1)


