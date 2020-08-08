
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='cyberlib',  
     version='0.1',
     packages=setuptools.find_packages(),
     include_package_data=True,
     scripts=['bin/cy'],
     entry_points= {
        "console_scripts": ['cy = cy.cli.cli:main']
     },
     author="Sagnik Modak",
     author_email="sagnikmodak1118@gmail.com",
     description="Create a pandora's box from raw file.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mind-matrix/cyberlib",
     classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
     zip_safe=False,
)