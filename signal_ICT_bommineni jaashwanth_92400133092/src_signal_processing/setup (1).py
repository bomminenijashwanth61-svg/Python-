import setuptools

# Read the contents of the README.md file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Call the setup function with the package details
setuptools.setup(
    name="signal-processing-utils",
    version="0.1.0",
    author="Shiva Prasad",
    author_email="jashwanth.bommineni128903@marwadiuniversity.ac.in" ,
    description="A Python package for generating and manipulating fundamental signals.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bomminenijashwanth61-svg/Python-",
    project_urls={
        "Bug Tracker": "https://github.com/bomminenijashwanth61-svg/Python-",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Tell setuptools to look for packages in the 'src' directory
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    # Specify the package dependencies
    install_requires=[
        "numpy>=1.22.0",
        "matplotlib>=3.5.0",
    ],
)