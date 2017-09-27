.. _Concepts:

========================================
Problem Formulation: Key Concepts
========================================

This section introduces some key concepts you must understand before you can formulate a problem
for the D-Wave QPU: objective functions, Ising model, quadratic unconstrained binary optimization
problems (QUBOs), and graphs.

Objective Functions
==========================

To understand how to express a problem in a form that the D-Wave system
can solve, we must first develop an *objective function*, which is a mathematical
expression of the energy of a system as a function of binary variables
representing the qubits. In most cases, the lower the energy of the objective function,
the better the solution. Sometimes any low-energy state is an acceptable solution to the original
problem; for other problems, only optimal solutions are acceptable. The best solutions
typically correspond to the *global minimum* energy in the solution space; see :numref:`Figure %s <obj>`.

.. figure:: images/obj.png
  :name: obj
  :scale: 50 %
  :alt: Energy of objective function.

  Energy of objective function.

..  remove per aaron

  The objective functions that can be solved on the D-Wave system are
  discrete rather than continuous; see :numref:`Figure %s <obj-8>`.

  .. figure:: images/obj-8.png
    :name: obj-8
    :scale: 50 %
    :alt: Energy of objective function for 8 solutions.

    Energy of objective function for 8 solutions.

Consider quadratic functions, which have one or two variables per term:

.. math::
  :nowrap:

  \begin{equation}
    D = Ax + By + Cxy
  \end{equation}

where :math:`A`, :math:`B`, and :math:`C` are constants. Single variable terms---:math:`Ax`
and :math:`By`, for example---are linear and act to bias the variable. Two-variable
terms---:math:`Cxy`, for example---are quadratic with a relationship between the variables.

Problem Formulations: Ising and QUBO
================================================================================

Two formulations we look at for objective functions are found in the *Ising model*
and in *QUBO* problems. Conversion between these two formulations is trivial.

Ising Model
-------------

The Ising model is traditionally used in statistical mechanics. Variables are "spin up"
(:math:`\uparrow`) and "spin down" (:math:`\downarrow`), states that correspond to
:math:`+1` and :math:`-1` values. Relationships between the spins, represented by
couplings, are correlations or anti-correlations.
The objective function expressed as an Ising model is as follows:

.. math::
	:nowrap:

	\begin{equation}
	 \text{E}_{ising}(\vc s) = \sum_{i=1}^N h_i s_i + \sum_{i=1}^N \sum_{j=i+1}^N J_{i,j} s_i s_j
	\end{equation}

where the linear coefficients corresponding to qubit biases are :math:`h_i`,
and the quadratic coefficients corresponding to coupling strengths are :math:`J_{i,j}`.

QUBO
------------------

QUBO problems are traditionally used in computer science. Variables are TRUE and FALSE, states that correspond to 1 and 0 values.

A QUBO problem is defined using an upper-diagonal matrix :math:`Q`, which is an :math:`N` x :math:`N` upper-triangular matrix of real weights,
and :math:`x`, a vector of binary variables, as minimizing the function

.. math::
  :nowrap:

  \begin{equation}
    f(x) = \sum_{i} {Q_{i,i}}{x_i} + \sum_{i<j} {Q_{i,j}}{x_i}{x_j}
  \end{equation}

where the diagonal terms :math:`Q_{i,i}` are the linear coefficients and the nonzero off-diagonal terms are
the quadratic coefficients :math:`Q_{i,j}`.

This can be expressed more concisely as

.. math::
  :nowrap:

  \begin{equation}
    \min_{{x} \in {\{0,1\}^n}} {x}^{T} {Q}{x}.
  \end{equation}

In scalar notation, used throughout most of this document, the objective function expressed as a QUBO is as follows:

.. math::
  :nowrap:

	\begin{equation}
		\text{E}_{qubo}(a_i, b_{i,j}; q_i) = \sum_{i} a_i q_i + \sum_{i<j} b_{i,j} q_i q_j.
	\end{equation}

.. note::
  *Unconstrained* means that there are no constraints on the variables other than those expressed in *Q*.



Notation Comparison
-----------------------------------------

The transformation between Ising and QUBO is

.. math::
  :nowrap:

	\begin{equation}
    s = q2 - 1.
  \end{equation}

:numref:`Figure %s <not>` compares Ising and QUBO notation and related terminology.

.. figure:: images/conven.png
  :name: not
  :alt: Notation comparison.

  Notation conventions.


Graphs
==============

Objective functions can be represented by graphs. A graph comprises a collection of nodes (representing variables)
and the connections between them (edges).

..
  For example, this single-variable objective function,

  .. math::
    :nowrap:

    \begin{equation}
      F(a) = 5a,
    \end{equation}

  can be represented by single node (variable) with a bias of 5; see :numref:`Figure %s <obj-5a>`.

  .. figure:: images/obj-5a.png
    :name: obj-5a
    :scale: 50 %
    :alt: single variable objective function

    Single-variable objective function.

For example, to represent two variables in a quadratic equation,

.. math::
  :nowrap:

  \begin{equation}
    H(a,b) = 5a + 7ab - 3b,
  \end{equation}

we need two nodes, :math:`a` and :math:`b`, with biases of :math:`5` and :math:`-3` and a connection between them with a
strength of 7; see :numref:`Figure %s <obj-5a2>`.

.. figure:: images/obj-5a2.png
  :name: obj-5a2
  :scale: 50 %
  :alt: two variable objective function

  Two-variable objective function.

..
  Each variable maps to a node and a linear coefficient (bias).
  The quadratic term is represented by an edge between the variables.

On the D-Wave system, a node is a qubit and an edge is a coupler.
