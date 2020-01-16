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
        vml.py_vdAcos(x,x)
    def cos(x):
        vml.py_vdCos(x,x)

    def sin(x):
        vml.py_vdSin(x,x)
    def asin(x):
        vml.py_vdAsin(x,x)

    def exp(x):
        vml.py_vdExp(x,x)
    def ln(x):
        vml.py_vdLn(x,x)

    def mul(x):
        vml.py_vdMul(x,x,x)

    def tan(x):
        vml.py_vdTan(x,x)
    def atan(x):
        vml.py_vdAtan(x,x)

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


#main:
#service_function_costs()
#noerror_impact()
#parallelization_impact()
sincos()




