from setuptools import setup, find_packages

setup(
	name="ms-powerpy",
	version="0.1.1",
	description="Librería para comunicación de Power BI REST API y cliente",
    url="https://github.com/4ssef/powerpy_package",
    author="4ssef (Fernando Assef)",
    author_email="fernandoassef@hotmail.com",
    license="MIT License",
    packages=find_packages(),
    install_requires=[],
	keywords=['python', 'power bi', 'power bi rest api', 'powerbi'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
		'Operating System :: OS Independent',
		'Intended Audience :: Information Technology',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)