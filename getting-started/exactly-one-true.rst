.. _One:

=======================================================
Using QUBOs to Represent Constraints
=======================================================

We can use QUBOs to define simple *constraints* that are important building blocks for larger, more complex problems.
The *exactly-one-true* constraint is a Boolean *satisfiability* problem in which we want to know, given a set of variables,
when exactly one variable equals 1 (is TRUE).

For example, when optimizing a traveling salesperson's route through a series of cities,
we need a constraint forcing the salesperson to be in exactly one city at each stage
of the trip: a solution that puts the salesperson in two or more places at once is invalid.

.. figure:: images/salesman.png
  :name: salesman
  :scale: 50 %
  :alt: Traveling salesman problem

  The traveling salesperson problem is an optimization problem that can be solved using exactly-one-true constraints.
  Map data |copy| 2017 GeoBasis-DE/BKG (|copy| 2009), Google.

..
  .. note::
    Contact |support| for access to a database of constraints like this one that you can use to construct QUBOs.

This chapter describes how to construct a simple exactly-one-true constraint in a form that the D-Wave system can solve.
It covers the following steps:

1. Start with the objective: in this case, start with an exactly-one-true constraint with 3 variables
   and build a truth table that satisfies this objective.
2. Develop a QUBO that favors the desired states and penalizes other states.
3. Convert the QUBO into a graph.

Build a Truth Table for the Objective Function
======================================================================

Consider a simple example: Given three variables :math:`a`, :math:`b`, and :math:`c`, we want to know when exactly one
variable is 1. (That is, when only one of :math:`a`, :math:`b`, and :math:`c` equals 1; the other two are 0.)
This translates into the following truth table:

========== ========== ========== ==========
:math:`a`  :math:`b`  :math:`c`  Exactly 1
========== ========== ========== ==========
0          0          0          FALSE
1          0          0          TRUE
0          1          0          TRUE
1          1          0          FALSE
0          0          1          TRUE
1          0          1          FALSE
0          1          1          FALSE
1          1          1          FALSE
========== ========== ========== ==========


Develop a QUBO Favoring States with One True
======================================================================

We want to find a function :math:`E(a,b,c)` that is at a minimum when this objective is true.
We can express this as

.. math::
  :nowrap:

  \begin{equation}
    a + b + c = 1
  \end{equation}

or as

.. math::
  :nowrap:

  \begin{equation}
    a + b + c -1 = 0.
  \end{equation}

The problem with the second expression above is that when :math:`a`, :math:`b`, and :math:`c` are all 0,
we get a result of :math:`-1`, which is a lower energy than the TRUE states. The
solution is to square the original equation:

.. math::
  :nowrap:

  \begin{equation}
    (a + b + c - 1)^2.
  \end{equation}

Taking a closer look at the squared expression,

.. math::
  :nowrap:

  \begin{equation}
    E(a,b,c)=(a+b+c-1)^2
  \end{equation}

we can see that because the variables are binary (0 or 1),


.. math::
  :nowrap:

  \begin{equation}
    a^2 = a
  \end{equation}

our objective function becomes the quadratic equation

.. math::
  :nowrap:

  \begin{equation}
    E(a,b,c) = 2ab + 2ac + 2bc - a - b - c + 1
  \end{equation}

where the energy of the function :math:`E(a,b,c)` is the value of the objective function.

Let's look at the truth table again, this time adding a column to show the
energy. Note that the lowest energy states are those that match
our exactly-one-true constraint. Remember that the better the solution,
the lower the energy.

========== ========== ========== ================= ==============
:math:`a`  :math:`b`  :math:`c`  Exactly 1         Energy
========== ========== ========== ================= ==============
0          0          0          FALSE             1
1          0          0          TRUE              0
0          1          0          TRUE              0
1          1          0          FALSE             1
0          0          1          TRUE              0
1          0          1          FALSE             1
0          1          1          FALSE             1
1          1          1          FALSE             4
========== ========== ========== ================= ==============

..
  This equation can be further simplified if we ignore the :math:`+1` offset:


  .. math::
    :nowrap:

    \begin{equation}
      E(a,b,c) = 2ab + 2ac + 2bc - a - b - c,
    \end{equation}

  which lowers the ground state energy from 0 to -1.

When expressed as a QUBO, we obtain


.. math::
  :nowrap:

  \begin{equation}
    E(x_0, x_1, x_2) = 2 x_0 x_1 + 2 x_0 x_2 + 2 x_1 x_2 - x_0 - x_1 - x_2 + 1.
  \end{equation}



Convert the QUBO into a Graph
======================================================================

The QUBO energy function can be represented by the triangular graph shown in :numref:`Figure %s <triangle>`.
Each binary variable becomes a node biased with its linear coefficient. Each quadratic term becomes an edge between the nodes.

.. figure:: images/triangle.png
  :name: triangle
  :scale: 50 %
  :alt: Triangular graph

  Triangular graph showing biased nodes and edges.
