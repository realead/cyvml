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

   def test_vdSinCos(self):
      x = np.array([0.0], dtype=np.float64)
      r1 = np.array([42.0], dtype=np.float64)
      r2 = np.array([42.0], dtype=np.float64)
      vml.py_vdSinCos(x,r1,r2)
      self.assertAlmostEqual(r1[0], 0.0)
      self.assertAlmostEqual(r2[0], 1.0)

   def test_vdMul(self):
      x = np.array([2.0], dtype=np.float64)
      y = np.array([2.0], dtype=np.float64)
      r = np.array([42.0], dtype=np.float64)
      vml.py_vdMul(x,y,r)
      self.assertAlmostEqual(r[0], 4.0)

   def test_vzCos(self):
      x = np.array([1+1j], dtype=np.complex128)
      y = np.array([42.42], dtype=np.complex128)
      vml.py_vzCos(x,y)
      self.assertAlmostEqual(y[0], 0.83373003-0.98889771j)

   def test_vzSin(self):
      x = np.array([1+1j], dtype=np.complex128)
      y = np.array([42.42], dtype=np.complex128)
      vml.py_vzSin(x,y)
      self.assertAlmostEqual(y[0], 1.29845758+0.63496391j)

   def test_vzTan(self):
      x = np.array([1+1j], dtype=np.complex128)
      y = np.array([42.42], dtype=np.complex128)
      vml.py_vzTan(x,y)
      self.assertAlmostEqual(y[0], 0.27175259+1.08392333j)

   def test_vzAcos(self):
      x = np.array([1+1j], dtype=np.complex128)
      y = np.array([42.42], dtype=np.complex128)
      vml.py_vzAcos(x,y)
      self.assertAlmostEqual(y[0], 0.90455689-1.06127506j)

   def test_vzAsin(self):
      x = np.array([1+1j], dtype=np.complex128)
      y = np.array([42.42], dtype=np.complex128)
      vml.py_vzAsin(x,y)
      self.assertAlmostEqual(y[0], 0.66623943+1.06127506j)

   def test_vzAtan(self):
      x = np.array([1+1j], dtype=np.complex128)
      y = np.array([42.42], dtype=np.complex128)
      vml.py_vzAtan(x,y)
      self.assertAlmostEqual(y[0], 1.01722197+0.40235948j)


   def test_vzExp(self):
      x = np.array([1+1j], dtype=np.complex128)
      y = np.array([42.42], dtype=np.complex128)
      vml.py_vzExp(x,y)
      self.assertAlmostEqual(y[0], 1.46869394+2.28735529j)

   def test_vzLn(self):
      x = np.array([1+1j], dtype=np.complex128)
      y = np.array([42.42], dtype=np.complex128)
      vml.py_vzLn(x,y)
      self.assertAlmostEqual(y[0], 0.34657359+0.78539816j)

   def test_vzMul(self):
      x = np.array([2.0+1j], dtype=np.complex128)
      y = np.array([2.0+1j], dtype=np.complex128)
      r = np.array([42.0], dtype=np.complex128)
      vml.py_vzMul(x,y,r)
      self.assertAlmostEqual(r[0], 3+4j)



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


