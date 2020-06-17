import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='python_module_test',
    version='0.1',
    scripts=['python_module_test'],
    author="John Miller",
    author_email="m1llj0hnst3r@gmail.com",
    description="A test module to learn how it is done",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/milljohn/python_module_test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
