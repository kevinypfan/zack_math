import setuptools
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setuptools.setup(
    name="zack-math",                     # This is the name of the package
    version="0.0.2",                        # The initial release version
    author="Zack Fan",                     # Full name of the author
    description="Quicksample Test Package for Math Demo",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.7',                # Minimum version requirement of the package
    py_modules=["zack-math"],             # Name of the python package
    package_dir={'':'zack_math'},     # Directory of the source code of the package
    install_requires=[]                 # Install other dependencies if any
)