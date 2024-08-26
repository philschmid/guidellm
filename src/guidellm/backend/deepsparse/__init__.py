"""
This package encapsulates the "Deepsparse Backend" implementation.
ref: https://github.com/neuralmagic/deepsparse

The `deepsparse` package supports Python3.6..Python3.11,
when the `guidellm` start from Python3.8.

Safe range of versions is Python3.8..Python3.11
for the Deepsparse Backend implementation.
"""

from guidellm.utils import check_python_version, module_is_available

# Ensure that python is in valid range
check_python_version(min_version="3.8", max_version="3.11")

# Ensure that deepsparse is installed
module_is_available(
    module="deepsparse",
    helper=(
        "`deepsparse` package is not available. "
        "Please try `pip install -e '.[deepsparse]'`"
    ),
)

from .backend import DeepsparseBackend

__all__ = ["DeepsparseBackend"]
