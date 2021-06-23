from setuptools import setup

setup(
    name='functestpy',
    version='0.1.0',    
    description='Testing Python package',
    url='https://github.com/SherylA/functestpy',
    author='Sheryl Avenaño',
    author_email='sheryl.avendano@udea.edu.co',
    license='BSD 2-clause',
    packages=['functestpy'],
    install_requires=['numpy', 'pandas',
                      'inspect', 'IPython'        
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.8',
    ],
)