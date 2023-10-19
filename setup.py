from setuptools import setup, find_packages

setup(
    name='pbixray',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        kaitai,
        apsw
    ],
    include_package_data=True,
    package_data={
        '': ['*.dll', '*.so', '*.dylib']
    }
    # ... Other metadata
)
