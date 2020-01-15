
# service functions:

cdef int cy_mkl_set_num_threads_local(int nth)
cdef int cy_set_vml_num_threads(int nth)
cdef int cy_get_vml_max_num_threads()

cdef int cy_vmlSetMode(unsigned int newmode)
cdef int cy_vmlGetMode()



#other functions:

cdef void cy_vdExp(long long int n, const double *x, double *y)
cdef void cy_vdLn(long long int n, const double *x, double *y)
cdef void cy_vdCos(long long int n, const double *x, double *y)
cdef void cy_vdSin(long long int n, const double *x, double *y)
cdef void cy_vdTan(long long int n, const double *x, double *y)
cdef void cy_vdAcos(long long int n, const double *x, double *y)
cdef void cy_vdAsin(long long int n, const double *x, double *y)
cdef void cy_vdAtan(long long int n, const double *x, double *y)
