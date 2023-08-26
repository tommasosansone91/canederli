
from setuptools import setup, find_packages

VERSION = '0.0.13' 

DESCRIPTION = 'Simple tools to quickly get the names of multiple variables out of the lines of code where they are defined.'

from .long_description import LONG_DESCRIPTION

setup(
        name="canederli", 
        version=VERSION,
        author="tms1991",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',  # added to avoid any special character in LONG_DESCRIPTION raises errors in PyPi server
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['multiline', 'strings', 'list', 'variables', 'names', 'labels'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)

