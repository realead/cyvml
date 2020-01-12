from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

from numpy.distutils.system_info import get_info
info_dict = get_info('mkl')

extensions = Extension(
            name='cyvml.cyvml',
            sources = ["src/cyvml/cyvml.pyx"],
            libraries = info_dict['libraries'],
            include_dirs = info_dict['include_dirs'],
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
