from shared.conf import restrictions
from shared.conf import *

dwave_part = "09-1076A-K"

dwave_overview = "This document introduces the D-Wave quantum computer, provides some key background information on how the system works, and explains how to construct a simple problem that the system can solve."

# General information about the project.
project = u'Getting Started with the D-Wave System'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

version = '2.12'

# The full version, including alpha/beta/rc tags.
release = version

latex_preamble += r"""
\def\dwavepart{%s}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{braket}
\newcommand{\argmin}{\operatornamewithlimits{argmin}}
\newcommand{\argmax}{\operatornamewithlimits{argmax}}
\newcommand{\vc}[1]{{\pmb{#1}}}
\newcommand{\ip}[2]{\langle{#1},{#2}\rangle}
\newcommand{\sign}{\operatorname{sign}}
\def\legalfooter{\small\sf Copyright \textcopyright\ D-Wave Systems Inc.}
""" % dwave_part

# pick one above
# \def\legalfooter{\small\sf Copyright \textcopyright\ D-Wave Systems Inc.}
# \def\legalfooter{\small\sf Proprietary and Confidential, D-Wave Systems Inc.}
# \usepackage{draftwatermark}

latex_preamble += r"""
\def\dwaveoverview{%s}
""" % dwave_overview


# \usepackage{draftwatermark} - incude this for drafts
#add restrictions
#latex_preamble += restrictions

latex_documents = [
    ('index', '%s_GettingStarted.tex' % (dwave_part), project,
     dwave_name, 'manual'),
]

pngmath_latex_preamble = latex_preamble
