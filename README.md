# python-package
Packages of custom modules/sub packages of python

## Setup

In order to build package execute:

```
python3 setup.py sdist bdist_wheel
python3 setup.py build
```

Then install for local purpose:

```
python3 setup.py install
```

If you are in DEV mode the execute the following code : 

```
python3 setup.py develop
```

## Doc : 
https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html


## Test:

Your have to install globally pytest : 

```
pip install -U pytest
```

Then execute tests by 

```
pytest -s
```

Note : Create tests folder in root project before execute tests