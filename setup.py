from setuptools import setup
setup(
    name='Similar',
    version='0.1',
#    install_requires=['opencv', 'matplotlib', 'numpy'], (error when installed by pypi repositories)
    scripts=['bin/similar'],
    packages={'similar'},
    package_dir={'similar': 'similar'}
)