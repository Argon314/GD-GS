from setuptools import setup, find_packages

setup(
    name="evags",
    version="1.0.0",
    author="Wentao Chen et al.",
    description="EVA-GS",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Argon314/EVA-GS",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
