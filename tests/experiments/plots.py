import cyvml.cyvml as vml
import numpy as np


import perfplot


def service_function_costs():
    perfplot.show(
            setup= lambda n : n,
            n_range=[1e3, 1e4, 1e5],
            kernels=[
                vml.onoff_multithreading,
                vml.onoff_multithreading_local,
                vml.onoff_mode        
                ],
            labels=["(2*set+1*get) thread number", "2*set local thread number", "2*set_mode"],
            logx=True,
            logy=True,
            title = "service functions",
            xlabel='number of times',
            equality_check = None,
            )

def noerror_impact():
    def acos_with_errorhandling(x):
        vml.py_vmlSetMode(vml.PY_VML_ERRMODE_DEFAULT)
        vml.py_vdAcos(x[1],x[1])

    def acos_without_error_errorhandling(x):
        vml.py_vmlSetMode(vml.PY_VML_ERRMODE_ERRNO)
        vml.py_vdAcos(x[1],x[1])

    def acos_without_error(x):
        vml.py_vmlSetMode(vml.PY_VML_ERRMODE_DEFAULT)
        vml.py_vdAcos(x[0],x[0])
        
    perfplot.show(
            setup= lambda n : [np.zeros(int(n), dtype=np.float64)+0.25, np.zeros(int(n), dtype=np.float64)+2.0],
            n_range=[1e4, 1e5, 1e6, 1e7, 1e8],
            kernels=[
                acos_without_error,
                acos_with_errorhandling,
                acos_without_error_errorhandling     
                ],
            logx=True,
            logy=True,
            title = "acos with errors",
            xlabel='len(vec)',
            equality_check = None,
            )

def parallelization_impact():
    def acos(x):
        vml.py_vdAcos(x[0],x[1])
    def cos(x):
        vml.py_vdCos(x[0],x[1])

    def sin(x):
        vml.py_vdSin(x[0],x[1])
    def asin(x):
        vml.py_vdAsin(x[0],x[1])

    def exp(x):
        vml.py_vdExp(x[0],x[1])
    def ln(x):
        vml.py_vdLn(x[0],x[1])

    def mul(x):
        vml.py_vdMul(x[0],x[1],x)

    def tan(x):
        vml.py_vdTan(x[0],x[1])
    def atan(x):
        vml.py_vdAtan(x[0],x[1])

    perfplot.show(
            setup= lambda n : np.zeros(n, dtype=np.float64)+0.25,
            n_range=list(range(1000, 10000, 1000)),
            kernels=[
                tan, atan 
                ],
            logx=False,
            logy=False,
            title = "tan vs atan",
            xlabel='len(vec)',
            equality_check = None,
            )

    perfplot.show(
            setup= lambda n : np.zeros(n, dtype=np.float64)+0.25,
            n_range=list(range(1000, 10000, 1000)),
            kernels=[
                exp, ln, mul  
                ],
            logx=False,
            logy=False,
            title = "exp, ln, mul",
            xlabel='len(vec)',
            equality_check = None,
            )    

    perfplot.show(
            setup= lambda n : np.zeros(n, dtype=np.float64)+0.25,
            n_range=list(range(1000, 10000, 1000)),
            kernels=[
                sin, cos,
                ],
            logx=False,
            logy=False,
            title = "sin, cos",
            xlabel='len(vec)',
            equality_check = None,
            )

    perfplot.show(
            setup= lambda n : np.zeros(n, dtype=np.float64)+0.25,
            n_range=list(range(1000, 10000, 1000)),
            kernels=[
                asin, acos,
                ],
            logx=False,
            logy=False,
            title = "asin, acos",
            xlabel='len(vec)',
            equality_check = None,
            )

def sincos():
    def sincos(x):
        vml.py_vdSinCos(x[0],x[1],x[2])
    def sin_and_cos(x):
        vml.py_vdCos(x[0],x[1])
        vml.py_vdSin(x[0],x[2])

    perfplot.show(
            setup= lambda n : [np.zeros(n, dtype=np.float64)+0.25, np.zeros(n, dtype=np.float64)+0.25, np.zeros(n, dtype=np.float64)+0.25],
            n_range=list(range(1000, 10000, 1000)),
            kernels=[
                sincos, sin_and_cos 
                ],
            logx=False,
            logy=False,
            title = "sincos vs sin+cos",
            xlabel='len(vec)',
            equality_check = None,
            )

def complex_cos():
    def real_cos(x):
        vml.py_vdCos(x[0],x[5])
    def complex_cos(x):
        vml.py_vzCos(x[1],x[4])
    def complex_noimag_cos(x):
        vml.py_vzCos(x[2],x[4])
    def complex_noreal_cos(x):
        vml.py_vzCos(x[3],x[4])

    perfplot.show(
            setup= lambda n : [np.zeros(n, dtype=np.float64)+0.25, 
                               np.zeros(n, dtype=np.complex128)+(0.25+.25j),                        
                               np.zeros(n, dtype=np.complex128)+0.25,
                               np.zeros(n, dtype=np.complex128)+0.25j,
                               np.zeros(n, dtype=np.complex128)+0.25j,
                               np.zeros(n, dtype=np.float64)+0.25],
            n_range=list(range(1000, 10000, 1000)),
            kernels=[
                real_cos, complex_cos, complex_noimag_cos, complex_noreal_cos
                ],
            logx=True,
            logy=True,
            title = "real vs. complex cos",
            xlabel='len(vec)',
            equality_check = None,
            )

def parallelization_impact_complex():
    def acos(x):
        vml.py_vzAcos(x[0],x[1])
    def cos(x):
        vml.py_vzCos(x[0],x[1])

    def sin(x):
        vml.py_vzSin(x[0],x[1])
    def asin(x):
        vml.py_vzAsin(x[0],x[1])

    def exp(x):
        vml.py_vzExp(x[0],x[1])
    def ln(x):
        vml.py_vzLn(x[0],x[1])

    def mul(x):
        vml.py_vzMul(x[0],x[0],x[1])

    def tan(x):
        vml.py_vzTan(x[0],x[1])
    def atan(x):
        vml.py_vzAtan(x[0],x[1])


    perfplot.show(
            setup= lambda n : [np.zeros(n, dtype=np.complex128)+0.25+0.25j, np.zeros(n, dtype=np.complex128)+0.25+0.25j],
            n_range=list(range(10, 200, 10)),
            kernels=[
                tan, atan
                ],
            logx=False,
            logy=False,
            title = "tan, atan",
            xlabel='len(vec)',
            equality_check = None,
            )  
    perfplot.show(
            setup= lambda n : [np.zeros(n, dtype=np.complex128)+0.25+0.25j,np.zeros(n, dtype=np.complex128)+0.25+0.25j],
            n_range=list(range(100, 3000, 300)),
            kernels=[
                exp, ln, mul
                ],
            logx=False,
            logy=False,
            title = "exp, ln, mul",
            xlabel='len(vec)',
            equality_check = None,
            )    
    perfplot.show(
            setup= lambda n : [np.zeros(n, dtype=np.complex128)+0.25+0.25j, np.zeros(n, dtype=np.complex128)+0.25+0.25j],
            n_range=list(range(10, 200, 10)),
            kernels=[
                sin, cos, asin, acos
                ],
            logx=False,
            logy=False,
            title = "sin, cos, asin, acos",
            xlabel='len(vec)',
            equality_check = None,
            )  



def expimag_sincos():
    def expimag(x):
        vml.py_vzExp(x[0],x[1])
    def sincos(x):
        vml.py_vdSinCos(x[2],x[3],x[4])
    
    perfplot.show(
            setup= lambda n : [np.zeros(n, dtype=np.complex128)+0.25j, np.zeros(n, dtype=np.complex128)+0.25, 
                               np.zeros(n, dtype=np.float64)+0.25, np.zeros(n, dtype=np.float64)+0.25, np.zeros(n, dtype=np.float64)+0.25],
            n_range=list(range(1000, 10000, 1000)),
            kernels=[
                expimag, sincos
                ],
            logx=False,
            logy=False,
            title = "sincos vs expimag",
            xlabel='len(vec)',
            equality_check = None,
            ) 


#main:
#service_function_costs()
#noerror_impact()
#parallelization_impact()
#sincos()
#complex_cos()
#parallelization_impact_complex()
expimag_sincos()




