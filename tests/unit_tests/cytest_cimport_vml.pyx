import unittest
import numpy as np


cimport cyvml.cyvml as vml
import cyvml.cyvml as pyvml


class CimportCyvmlTester(unittest.TestCase): 

    def test_cimport_vdCos(self):
        cdef double x = 2.0*np.pi
        vml.cy_vdCos(1, &x, &x)
        self.assertAlmostEqual(x, 1.0)

    def test_cimport_vdSin(self):
        cdef double x = np.pi / 2.0
        vml.cy_vdSin(1, &x, &x)
        self.assertAlmostEqual(x, 1.0)

    def test_cimport_vdExp(self):
        cdef double x = 1.0
        vml.cy_vdExp(1, &x, &x)
        self.assertAlmostEqual(x, np.e)

    def test_cimport_vdLn(self):
        cdef double x = 1.0
        vml.cy_vdLn(1, &x, &x)
        self.assertAlmostEqual(x, 0.0)

    def test_vdTan(self):
      cdef double x = np.pi/4.0
      vml.cy_vdTan(1, &x, &x)
      self.assertAlmostEqual(x, 1.0)

    def test_vdAcos(self):
      cdef double x = 1.0
      vml.cy_vdAcos(1,&x,&x)
      self.assertAlmostEqual(x, 0.0)

    def test_vdAsin(self):
      cdef double x = 1.0
      vml.cy_vdAsin(1, &x, &x)
      self.assertAlmostEqual(x, np.pi/2.0)

    def test_vdAtan(self):
      cdef double x = 1.0
      vml.cy_vdAtan(1,&x,&x)
      self.assertAlmostEqual(x, np.pi/4)

    def test_vdMul(self):
      cdef double x = 2.0
      vml.cy_vdMul(1,&x,&x,&x)
      self.assertAlmostEqual(x, 4)


# should be last...
    def test_get_set_threads(self):
        self.assertEqual(vml.cy_set_vml_num_threads(1), 1)
        self.assertEqual(vml.cy_get_vml_max_num_threads(), 1)
        self.assertEqual(vml.cy_set_vml_num_threads(2), 1)
        self.assertEqual(vml.cy_get_vml_max_num_threads(), 2)

    def test_get_set_threads_local(self):
        old = vml.cy_mkl_set_num_threads_local(3)
        self.assertEqual(vml.cy_mkl_set_num_threads_local(old), 3)
        self.assertEqual(vml.cy_mkl_set_num_threads_local(old), old)

    def test_get_set_mode(self):
       vml.cy_vmlSetMode(pyvml.PY_VML_EP)
       self.assertEqual(vml.cy_vmlGetMode()&3, 3)
       vml.cy_vmlSetMode(pyvml.PY_VML_LA)
       self.assertEqual(vml.cy_vmlGetMode()&3, 1)
