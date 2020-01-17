
# service functions:

cdef int cy_mkl_set_num_threads_local(int nth)
cdef int cy_set_vml_num_threads(int nth)
cdef int cy_get_vml_max_num_threads()

cdef int cy_vmlSetMode(unsigned int newmode)
cdef int cy_vmlGetMode()

cdef void cy_mkl_set_dynamic(int bool_mkl_dynamic)
cdef int  cy_mkl_get_dynamic()



#other functions:

cdef void cy_vdExp(long long int n, const double *x, double *y)
cdef void cy_vdLn(long long int n, const double *x, double *y)
cdef void cy_vdCos(long long int n, const double *x, double *y)
cdef void cy_vdSin(long long int n, const double *x, double *y)
cdef void cy_vdTan(long long int n, const double *x, double *y)
cdef void cy_vdAcos(long long int n, const double *x, double *y)
cdef void cy_vdAsin(long long int n, const double *x, double *y)
cdef void cy_vdAtan(long long int n, const double *x, double *y)

cdef void cy_vdSinCos(long long int n, const double *a, double *r1, double* r2)

cdef void cy_vdMul(long long int n, const double *a, const double *b, double* r)


#complex functions:

cdef void cy_vzExp(long long int n, const double complex *x, double complex *y)
cdef void cy_vzLn(long long int n, const double complex *x, double complex *y)
cdef void cy_vzCos(long long int n, const double complex *x, double complex *y)
cdef void cy_vzSin(long long int n, const double complex *x, double complex *y)
cdef void cy_vzTan(long long int n, const double complex *x, double complex *y)
cdef void cy_vzAcos(long long int n, const double complex *x, double complex *y)
cdef void cy_vzAsin(long long int n, const double complex *x, double complex *y)
cdef void cy_vzAtan(long long int n, const double complex *x, double complex *y)

# there is no SinCos for complex:
# cdef void cy_vzSinCos(long long int n, const double complex *a, double complex *r1, double complex* r2)

cdef void cy_vzMul(long long int n, const double complex *a, const double complex *b, double complex* r)
