#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

# Not pinning tensorflow package versions might lead to incompatibilities
requirements = ["tensorflow==2.2.0",
                "tensorflow_text==2.2.0",
                "tensorflow_hub==0.8.0",
                "numpy",
                "dataclasses; python_version<='3.6'"]

extras_require = {"plot": ["matplotlib", "seaborn"]}

setup_requirements = ["pytest-runner", ]

test_requirements = ["pytest>=3", ]

setup(
    author="Fabian Sorn",
    author_email="fabian.sorn@icloud.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Some Project for testing the semantic similarity between two sentences.",
    entry_points={
        "console_scripts": [
            "sts=semtextsim.cli:main",
        ],
    },
    install_requires=requirements,
    extras_require=extras_require,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    license="MIT license",
    include_package_data=True,
    keywords="semtextsim",
    name="semtextsim",
    packages=find_packages(include=["semtextsim", "semtextsim.*"]),
    test_suite="tests",
    url="https://github.com/fabianSorn/semtextsim",
    version="0.1.0",
    zip_safe=False,
)
