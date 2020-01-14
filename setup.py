import os
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

# heuristic for finding mkl-distribution:
if os.path.exists('site.cfg'):
    info_dict = {}
    try:
        import configparser
        config = configparser.ConfigParser()
        config.read('site.cfg')
        info_dict = {'libraries' : [x.strip() for x in config['mkl']['libraries'].split(",")],
                     'library_dirs' : [x.strip() for x in config['mkl']['library_dirs'].split(os.path.pathsep)]}
    finally:
        pass
else: # try numpy's installation (default)
    from numpy.distutils.system_info import get_info
    info_dict = get_info('mkl')

if not info_dict:
    raise ValueError("mkl info isn't found:  please provide right information in site.cfg (see README.md)")

extensions = Extension(
            name='cyvml.cyvml',
            sources = ["src/cyvml/cyvml.pyx"],
            libraries = info_dict['libraries'],
            library_dirs = info_dict['library_dirs'],
    )
extensions = cythonize(extensions, compiler_directives={'language_level' : 3})

kwargs = {
      'name':'cyvml',
      'version':'0.1.0',
      'description':'a project',
      'author':'Egor Dranischnikow',
      'url':'https://github.com/realead/cyvml',
      'packages':find_packages(where='src'),
      'package_dir':{"": "src"},
      'license': 'MIT',
      'ext_modules':  extensions,

       #ensure pxd-files:
      'package_data' : { 'cyvml': ['*.pxd','*.pxi']},
      'include_package_data' : True,
      'zip_safe' : False  #needed because setuptools are used
}
setup(**kwargs)
