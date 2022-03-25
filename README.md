# gameoflife
A basic Python implementation of the classic game of life

# Usage
This repository is intended to be used as an example of how to properly document and package Python code. See the [undocumented](https://github.com/jvita/gameoflife/tree/undocumented) branch to switch to the version that doesn't have any documentation or packaging.

# Resources
* [“A practical guide to using setup.py”](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/)
* [Sphinx + ReadTheDocs](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
* [Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* [Github Pages tutorial (with fixes for common errors)](https://python.plainenglish.io/how-to-host-your-sphinx-documentation-on-github-550254f325ae)
* [Python unit testing in VSCode](https://code.visualstudio.com/docs/python/testing#_tests-in-unittest)
* [argparse](https://docs.python.org/3/library/argparse.html)
* [typing](https://docs.python.org/3/library/typing.html)

# Other packages you may need
```
pip install sphinx_rtd_theme
```

# Other minor amendments

1. When setting up github pages, change your Sphinx [Makefile](https://github.com/jvita/gameoflife/blob/master/docs/Makefile) to have the line `BUILDDIR      = .` instead of `BUILDDIR      = docs` as specified in the linked tutorial. This will also affect the contents of [docs/index.html](<meta http-equiv="refresh" content="0; url=./html/index.html" />).
