## service functions:
cdef extern from *:
    """
    #define MKL_VML  3 
    int MKL_Domain_Set_Num_Threads(int nth, int MKL_DOMAIN);
    int set_vml_num_threads(int nth){
        return MKL_Domain_Set_Num_Threads(nth, MKL_VML);
    }
    int MKL_Domain_Get_Max_Threads(int MKL_DOMAIN);
    int get_vml_max_num_threads(void){
        return MKL_Domain_Get_Max_Threads(MKL_VML);
    }
    """
    int set_vml_num_threads(int nth)
    int get_vml_max_num_threads()


cdef int cy_set_vml_num_threads(int nth):
    return set_vml_num_threads(nth)
def py_set_vml_num_threads(int nth):
    return cy_set_vml_num_threads(nth)

cdef int cy_get_vml_max_num_threads():
    return get_vml_max_num_threads()
def py_get_vml_max_num_threads():
    return cy_get_vml_max_num_threads()

#testing overhead:
def onoff_multithreading(int n, int nthreads):
    cdef int orig = cy_get_vml_max_num_threads()
    cdef int i, old
    for i in range(n):
        old = cy_get_vml_max_num_threads();
        cy_set_vml_num_threads(nthreads);
        cy_set_vml_num_threads(old);
    cy_set_vml_num_threads(orig);
    
        
        


## other functions:
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



