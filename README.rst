********************************
Building a Custom Python Module
********************************

Sources
#######
- `Executable Python Module <https://dzone.com/articles/executable-package-pip-install>`_

- `Packaging Python Projects <https://packaging.python.org/tutorials/packaging-projects/>`_

How to setup a custom module
############################
1. `Register with PyPi <https://pypi.org/account/register/>`_
2. Setup virtual environment in Pycharm
    - ``python -m pip install --upgrade pip setuptools wheel``
    - ``python -m pip install tqdm``
    - ``python -m pip install --upgrade twine``
3. Create a file
4. setup.py
5. ``python setup.py bdist_wheel``
6. wheel file in dist/
7. python -m twine upload dist/*
    - Be careful here, it looks like there is a testing repo before posting publicly
