from setuptools import setup, find_packages

setup(
    name='pbixray',
    version='0.1.9',
    packages=find_packages(),
    install_requires=[
        'kaitaistruct',
        'pandas',
        'apsw'
    ],
    include_package_data=True,
    package_data={
        'pbixray': ['lib/*.dll', 'lib/*.so', 'lib/*.dylib'],
    }
)
