import sys
from pathlib import Path


# Make value_at_risk importable as a top-level package.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "package" / "samplers"))

project = "value_at_risk"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.mathjax",
]

html_theme = "sphinx_rtd_theme"

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# autodoc settings
autodoc_member_order = "bysource"
