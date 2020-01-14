cdef extern from *:
    """
    // MKL_INT is 64bit integer for mkl-ilp64
    // see https://software.intel.com/en-us/mkl-developer-reference-c-c-datatypes-specific-to-intel-mkl
    #define MKL_INT long long int
    void  vdExp(MKL_INT n, const double *x, double *y);
    void  vdLn(MKL_INT n, const double *x, double *y);
    void  vdCos(MKL_INT n, const double *x, double *y);
    void  vdSin(MKL_INT n, const double *x, double *y);
    """
    void vdExp(long long int n, const double *x, double *y)
    void vdLn(long long int n, const double *x, double *y)
    void vdSin(long long int n, const double *x, double *y)
    void vdCos(long long int n, const double *x, double *y)


cdef void cy_vdExp(long long int n, const double *x, double *y):
    vdExp(n, x, y)
def py_vdExp(const double[::1] x, double[::1] y):
    if len(x) != len(y):
        raise BufferError("Different buffer lengths")
    cy_vdExp(len(x), &x[0], &y[0])

cdef void cy_vdLn(long long int n, const double *x, double *y):
    vdLn(n, x, y)
def py_vdLn(const double[::1] x, double[::1] y):
    if len(x) != len(y):
        raise BufferError("Different buffer lengths")
    cy_vdLn(len(x), &x[0], &y[0])

cdef void cy_vdCos(long long int n, const double *x, double *y):
    vdCos(n,x,y)
def py_vdCos(const double[::1] x, double[::1] y):
    if len(x) != len(y):
        raise BufferError("Different buffer lengths")
    cy_vdCos(len(x), &x[0], &y[0])

cdef void cy_vdSin(long long int n, const double *x, double *y):
    vdSin(n,x,y)
def py_vdSin(const double[::1] x, double[::1] y):
    if len(x) != len(y):
        raise BufferError("Different buffer lengths")
    cy_vdSin(len(x), &x[0], &y[0])

