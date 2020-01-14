# cyvml

cython-wrapper for intel's vml

## About

A cython wrapper to experiment with Intel's VML. It works out of the box for Anaconda-Distribution with MKL on Linux. On Windows one needs to provide path to *.lib-files even for Anaconda-Distribution, as it doesn't ship them. One also has to take care of dlls being on the PATH.

Not yet all functions are wrapped - they will be added as needed.

## Instalation:

To install the module using pip run:

    pip install https://github.com/realead/cyvml/zipball/master

It is possible to uninstall it afterwards via

    pip uninstall cyvml

You can also install using the setup.py file from the root directory of the project:

    python setup.py install

or 

    pip install -e .

to install in development mode.

In order to provide/use a different mkl-distribution, rename `site.cfg.example` to `site.cfg` and adjust the needed values. Then use the installation commands from above.

## Usage


The functions for `cimport` have prefix `cy_`, for example:


    %%cython
    cimport cyvml.cyvml as vml

    cdef double x = 1.0
    vml.cy_vdExp(1, &x, &x)

The functionality can be used also from pure Python with anything supporting buffer protocol - the functions have prefix `py_`:

    import numpy as np
    import cyvml.cyvml as vml

    x = np.array([np.pi*2], dtype=np.float64)
    y = np.array([42.42], dtype=np.float64)
    vml.py_vdCos(x,y)

## Testing

For testing of the local version run:

    `sh test_in_active_env.sh`

in the `tests` subfolder.



