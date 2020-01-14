import unittest
import numpy as np


cimport cyvml.cyvml as vml


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
