
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

extensions = Extension(
            name='cyvml.cyvml',
            sources = ["src/cyvml/cyvml.pyx"]
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
