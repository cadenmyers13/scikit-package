#!/usr/bin/env python
##############################################################################
#
# Copyright (c) 2024-2025, The Trustees of Columbia University in the City of
# New York. All rights reserved.
#
# Copyright (c) 2026-present, The scikit-package developers. All rights
# reserved.
#
# File coded by: Billinge Group members and community contributors.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/scikit-package/scikit-package/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################
"""A Python package standard and generator for scientific code.

Use scikit-package to launch a new project or migrate existing ones to
support the latest Python versions and streamline the process of
distributing and maintaining your software package.
"""

# package version
from scikit_package.version import __version__

# silence the pyflakes syntax checker
assert __version__ or True

# End of file
