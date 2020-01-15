import cyvml.cyvml as vml


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



#main:
service_function_costs()
    
