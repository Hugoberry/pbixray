from setuptools import setup, find_packages

setup(
    name='pbixray',
    version='0.1.16',
    packages=find_packages(),
    install_requires=[
        'kaitaistruct',
        'pandas',
        'apsw'
    ],
    include_package_data=True,
    package_data={
        'pbixray': ['lib/*.dll', 'lib/*.so', 'lib/*.dylib'],
    },
    author="Igor Cotruta",
    description="A Python library to parse and analyze PBIX files used with Microsoft Power BI.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Hugoberry/pbixray",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
