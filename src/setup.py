from setuptools import setup, find_packages
from thunno2 import version

long_description = "Thunno is a golfing language written in Python. Learn more at https://github.com/Thunno/Thunno2"

setup(
    name="thunno2",
    version=version.THUNNO_VERSION,
    license="MIT",
    description="A golfing language",
    author="Rujul Nayak",
    author_email="rujulnayak@outlook.com",
    url="https://github.com/Thunno/Thunno2",
    download_url=f"https://github.com/Thunno/Thunno2/archive/refs/tags/v{version.THUNNO_VERSION}.tar.gz",
    keywords=["golfing", "code-golf", "language"],
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    entry_points={"console_scripts": ["thunno2 = thunno2.run:from_cmdline"]},
)
