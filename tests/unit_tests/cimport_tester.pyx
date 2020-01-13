import unittest
cimport cyvml.cyvml as vml

import numpy as np


class MockMemNanny:
    def __init__(self, lst):
        self.lst=lst

    def __del__(self):
        self.lst.append("Deallocated")


#makes sure there are no references to MockMemNanny-object around
cdef create_with_nanny(void * ptr, lst):
    mem = IndirectMemory2D.from_ptr_with_memory_nanny(ptr,1,1,'i',0, MockMemNanny(lst))
    return mem

class CimportCyvmlTester(unittest.TestCase): 
    def test_cimport_vdCos(self):
        cdef double x = 2*np.pi
        vml.cy_vdCos(1, &x, &x)
        self.assertAlmostEqual(x, 1.0)
