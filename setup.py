from distutils.core import setup

long_description = open('README.md').read()

setup(name="python-crunchbaseapi",
      version="1.0",
      py_modules=["crunchbaseapi"],
      description="Lightweight Python wrapper for Crunchbase API",
      author="Christopher Calder <caldercho@gmail.com>",
      author_email = "caldercho@gmail.com",
      license="WTFPL",
      url="http://github.com/caldercho/crunchbaseapi",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
       install_requires=["simplejson >= 1.8"]
      )

