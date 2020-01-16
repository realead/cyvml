## service functions:

## threading controll:
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
   
    int MKL_Set_Num_Threads_Local(int nth);

    """
    int set_vml_num_threads(int nth)
    int get_vml_max_num_threads()
    int MKL_Set_Num_Threads_Local(int nth)


cdef int cy_set_vml_num_threads(int nth):
    return set_vml_num_threads(nth)
def py_set_vml_num_threads(int nth):
    return cy_set_vml_num_threads(nth)

cdef int cy_get_vml_max_num_threads():
    return get_vml_max_num_threads()
def py_get_vml_max_num_threads():
    return cy_get_vml_max_num_threads()

cdef int cy_mkl_set_num_threads_local(int nth):
    return MKL_Set_Num_Threads_Local(nth)
def py_mkl_set_num_threads_local(int nth):
    return cy_mkl_set_num_threads_local(nth)

#testing overhead:
def onoff_multithreading(int n, int nthreads=5):
    cdef int orig = cy_get_vml_max_num_threads()
    cdef int i, old
    for i in range(n):
        old = cy_get_vml_max_num_threads();
        cy_set_vml_num_threads(nthreads);
        cy_set_vml_num_threads(old);
    cy_set_vml_num_threads(orig);


#testing overhead:
def onoff_multithreading_local(int n, int nthreads=5):
    cdef int orig = cy_mkl_set_num_threads_local(3)
    cdef int i, old
    for i in range(n):
        old = cy_mkl_set_num_threads_local(1);
        cy_mkl_set_num_threads_local(old);
    cy_mkl_set_num_threads_local(orig);


#
cdef extern from *:
    """
    #define VML_LA 0x00000001
    #define VML_HA 0x00000002
    #define VML_EP 0x00000003
    #define VML_ERRMODE_IGNORE   0x00000100
    #define VML_ERRMODE_ERRNO    0x00000200
    #define VML_ERRMODE_STDERR   0x00000400
    #define VML_ERRMODE_EXCEPT   0x00000800
    #define VML_ERRMODE_CALLBACK 0x00001000
    #define VML_ERRMODE_DEFAULT  \
    VML_ERRMODE_ERRNO | VML_ERRMODE_CALLBACK | VML_ERRMODE_EXCEPT

    unsigned int vmlSetMode(unsigned int);
    unsigned int vmlGetMode(void);
    """
    unsigned int vmlSetMode(unsigned int newMode)
    unsigned int vmlGetMode()
    const unsigned int VML_LA
    const unsigned int VML_HA
    const unsigned int VML_EP
    const unsigned int VML_ERRMODE_IGNORE 
    const unsigned int VML_ERRMODE_ERRNO 
    const unsigned int VML_ERRMODE_STDERR
    const unsigned int VML_ERRMODE_EXCEPT 
    const unsigned int VML_ERRMODE_CALLBACK
    const unsigned int VML_ERRMODE_DEFAULT

PY_VML_LA = VML_LA
PY_VML_HA = VML_HA
PY_VML_EP = VML_EP
PY_VML_ERRMODE_IGNORE  = VML_ERRMODE_IGNORE
PY_VML_ERRMODE_ERRNO  =  VML_ERRMODE_ERRNO
PY_VML_ERRMODE_STDERR = VML_ERRMODE_STDERR
PY_VML_ERRMODE_EXCEPT = VML_ERRMODE_EXCEPT
PY_VML_ERRMODE_CALLBACK = VML_ERRMODE_CALLBACK
PY_VML_ERRMODE_DEFAULT = VML_ERRMODE_DEFAULT

cdef int cy_vmlSetMode(unsigned int newmode):
    return vmlSetMode(newmode)
def py_vmlSetMode(unsigned int newmode):
    return cy_vmlSetMode(newmode)

cdef int cy_vmlGetMode():
    return vmlGetMode()
def py_vmlGetMode():
    return cy_vmlGetMode()

#testing overhead:
def onoff_mode(int n):
    cdef int i
    for i in range(n):
        old = cy_vmlSetMode(2);
        cy_vmlSetMode(old);
    

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
    void  vdTan(MKL_INT n, const double *x, double *y);
    void  vdAcos(MKL_INT n, const double *x, double *y);
    void  vdAsin(MKL_INT n, const double *x, double *y);
    void  vdAtan(MKL_INT n, const double *x, double *y);
    void  vdSinCos(MKL_INT n, const double *a, double *r1, double* r2);
    void  vdMul(MKL_INT n, const double *a, const double *b, double* r);
    """
    void vdExp(long long int n, const double *x, double *y)
    void vdLn(long long int n, const double *x, double *y)
    void vdSin(long long int n, const double *x, double *y)
    void vdCos(long long int n, const double *x, double *y)
    void vdTan(long long int n, const double *x, double *y)
    void vdAsin(long long int n, const double *x, double *y)
    void vdAcos(long long int n, const double *x, double *y)
    void vdAtan(long long int n, const double *x, double *y)
    void vdSinCos(long long int n, const double *a, double *r1, double* r2)
    void vdMul(long long int n, const double *a, const double *b, double* r)


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

cdef void cy_vdTan(long long int n, const double *x, double *y):
    vdTan(n,x,y)
def py_vdTan(const double[::1] x, double[::1] y):
    if len(x) != len(y):
        raise BufferError("Different buffer lengths")
    cy_vdTan(len(x), &x[0], &y[0])

cdef void cy_vdAcos(long long int n, const double *x, double *y):
    vdAcos(n,x,y)
def py_vdAcos(const double[::1] x, double[::1] y):
    if len(x) != len(y):
        raise BufferError("Different buffer lengths")
    cy_vdAcos(len(x), &x[0], &y[0])

cdef void cy_vdAsin(long long int n, const double *x, double *y):
    vdAsin(n,x,y)
def py_vdAsin(const double[::1] x, double[::1] y):
    if len(x) != len(y):
        raise BufferError("Different buffer lengths")
    cy_vdAsin(len(x), &x[0], &y[0])

cdef void cy_vdAtan(long long int n, const double *x, double *y):
    vdAtan(n,x,y)
def py_vdAtan(const double[::1] x, double[::1] y):
    if len(x) != len(y):
        raise BufferError("Different buffer lengths")
    cy_vdAtan(len(x), &x[0], &y[0])

cdef void cy_vdMul(long long int n, const double *a, const double *b, double* r):
    vdMul(n,a,b,r)
def py_vdMul(const double[::1] a, const double[::1] b, double[::1] r):
    if len(a) != len(r) or len(b)!=len(r):
        raise BufferError("Different buffer lengths")
    cy_vdMul(len(a), &a[0], &b[0], &r[0])

cdef void cy_vdSinCos(long long int n, const double *a, double *r1, double* r2):
    vdSinCos(n,a,r1,r2)
def py_vdSinCos(const double[::1] a, double[::1] r1, double[::1] r2):
    if len(a) != len(r1) or len(a)!=len(r2):
        raise BufferError("Different buffer lengths")
    cy_vdSinCos(len(a), &a[0], &r1[0], &r2[0])


### complex functions:

cdef extern from *:
    """
    /* Intel(R) MKL Complex type for double precision */
    #ifndef MKL_Complex16
    typedef
    struct _MKL_Complex16 {
        double real;
        double imag;
    } MKL_Complex16;
    #endif
    void vzCos(const MKL_INT n, const MKL_Complex16* a, MKL_Complex16* r);
    """
    struct MKL_Complex16:
        pass
    void vzCos(long long int n, const MKL_Complex16* a, MKL_Complex16* r)

cdef void cy_vzCos(long long int n, const double complex* a, double complex* r):
    vzCos(n,<const MKL_Complex16*>a, <MKL_Complex16*>r)
def py_vzCos(const double complex[::1] x, double complex[::1] y):
    if len(x) != len(y):
        raise BufferError("Different buffer lengths")
    cy_vzCos(len(x), &x[0], &y[0])
