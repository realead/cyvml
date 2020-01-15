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

#main:
#service_function_costs()
noerror_impact()




