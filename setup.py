from setuptools import setup
from setuptools import find_namespace_packages
from os import path

project_path = path.dirname(path.realpath(__file__))
long_description = open(f"{project_path}\README.md", encoding = 'utf-8').str

setup(
	#name="ms-powerpy",
	#version="0.1.4",
	#description="Easier communication between Microsoft Power BI REST API and a client",
	#long_description=long_description,
    #url="https://github.com/4ssef/powerpy_package",
    #author="4ssef (Fernando Assef)",
    #author_email="fernandoassef@hotmail.com",
    #license="MIT License",
    # packages=find_namespace_packages(),
    # install_requires=['msal', 'requests'],
	# keywords=['python', 'power bi', 'power bi rest api', 'powerbi'],
    # classifiers=[
    #     'Development Status :: 3 - Alpha',
    #     'Intended Audience :: Developers',
    #     'Programming Language :: Python :: 3.9',
	# 	'Operating System :: OS Independent',
	# 	'Intended Audience :: Information Technology',
	# 	'License :: OSI Approved :: MIT License',
	# 	'Natural Language :: English',
	# 	'Topic :: Software Development :: Libraries :: Python Modules'
    # ]
)