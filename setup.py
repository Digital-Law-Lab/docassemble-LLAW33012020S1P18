import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012020S1P18',
      version='1.0',
      description=('NDIS Planning Meeting Assistance'),
      long_description='# P18\r\n\r\nThis application is designed to aid CBS clients who have intellectual disabilities to complete *Booklet 2* for their NDIS planning meeting. \r\n\r\nPreparing for a planning meeting can be an overwhelming and difficult process. It is important to be adequately prepared for a planning meeting as it plays a large role in determing how much financial support an individual will be granted as part of their plan. \r\n\r\nThis application has been designed to make the process easier and more accessible. CBS clients are encouraged to answer questions honestly and in a manner that will best serve the purpose of the planning meeting. It has been designed with AAT decisions and NDIS expections in mind in order to best prepare CBS clients to get the most out of their meeting. \r\n',
      long_description_content_type='text/markdown',
      author='Ashleigh McNichol',
      author_email='ferr0182@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012020S1P18/', package='docassemble.LLAW33012020S1P18'),
     )

