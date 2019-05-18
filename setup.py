import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calorie_tracker",
    version="0.0.1",
    author="Anna Pynda",
    author_email="pynda@ucu.edu.ua",
    description="A program to count calories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/annapynda/Cursova",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)