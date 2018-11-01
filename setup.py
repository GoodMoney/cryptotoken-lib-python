from setuptools import setup, find_packages
setup(
    name="cryptotoken",
    version="0.1.dev0",
    author="Duke Jones",
    author_email="duke@goodmoney.com",
    description="A library for interacting with cryptographic tokens on blockchains.",
    license="LGPL",
    keywords="blockchain token cryptocurrency",
    url="https://github.com/GoodMoney/cryptotoken-lib-python",   # project home page, if any
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    ],
    install_requires=[
        'web3'
    ]
)
