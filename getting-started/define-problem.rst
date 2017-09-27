========================================================
Defining a Simple Problem
========================================================

One type of problem that we expect the |dwave_short| system to be good at solving
is an *optimization of binary variables* problem. Binary variables can
only have values 0 (NO, or FALSE) or 1 (YES, or TRUE).
These are problems that answer questions like: "Should a package
be shipped on this truck?"

.. For example, consider an *AND gate*: - removed per cathy

	* We have two binary inputs, :math:`a` and :math:`b`
	* If :math:`a` and :math:`b` are both 1, then output 1
	* Otherwise output 0

Conventional computers---even the biggest supercomputers---can be thought of as
being composed of *logic gates*, simple decision devices that produce outputs
based on their inputs. While the |dwave_short| system is not based on gates, it so
happens that a particular gate forms a good first optimization problem for the
system to solve.  The XOR (Exclusive OR) gate returns TRUE output only
if exactly one of the inputs to the gate is TRUE:

* We have two binary inputs, :math:`a` and :math:`b`
* If :math:`a=1` and :math:`b=0`, output 1
* If :math:`a=0` and :math:`b=1`, output 1
* Otherwise output 0

Define the Objective Function
======================================================================

Consider a simple two-qubit problem, in which we want the qubits to have the same value after annealing.
There are four possible final states of the qubits, as is apparent in the following table

============= ===================
:math:`q_0`   :math:`q_1`
============= ===================
0             0
0             1
1             0
1             1
============= ===================

and we want the D-Wave system to favor the states (0,0) and (1,1) and penalize the states (0,1) and (1,0).
We need to define an objective function that will do so.

In an objective function, the qubits are the variables. The biases and strengths are the coefficients on
the linear and quadratic terms. The objective function for a two-qubit problem has three terms, two linear and one
quadratic. The linear coefficients correspond to qubit biases, and the quadratic coefficients to coupler
strengths.

The objective function we need is written as follows:

.. math::
	:nowrap:

	\begin{equation}
		f(\vc{s}) = a_1 q_1 + a_2 q_2 + b_{1,2} q_1 q_2
	\end{equation}

where :math:`\vc{s}` is a vector of the variables :math:`q = [q_i, q_2]`, :math:`a_1` and :math:`a_2`
are the qubit biases, :math:`q_1` and :math:`q_2` are the binary variables representing qubits 1 and 2,
and :math:`b_{1,2}` is the strength of the coupler.

We now set :math:`a_1` and :math:`a_2` and :math:`b_{1,2}` to satisfy our original goal.
First, notice that when :math:`q_1` and :math:`q_2` both equal 0---state 1, written as (0,0)---the value of the objective
function is 0, and we have no other adjustable parameters. Since we want to favor this state, the minimum energy,
corresponding to the ground state, should equal 0.

We also want to penalize states 2 and 3, (0,1) and (1,0), relative to state 1 (0,0). One way to do this is
to assign a bias of 0.1 to qubits 1 and 2 by setting both :math:`a_1` and :math:`a_2` to 0.1:

============= =================== =======================
:math:`q_0`   :math:`q_1`         Objective Value
============= =================== =======================
0             0                   0
0             1                   0.1
1             0                   0.1
1             1                   0.2 + :math:`b_{1,2}`
============= =================== =======================

Remember we also want to favor state 4 (1,1) along with state 1 (0,0). One way to do this is to set the coupler
strength to :math:`b_{1,2} = -0.2`. The resulting objective function is

.. math::
	:nowrap:

	\begin{equation}
		f(\vc{s}) = 0.1 q_1 + 0.1 q_2 - 0.2 q_1 q_2,
	\end{equation}

and the table of possible outcomes is now as shown below.

============= =================== =======================
:math:`q_0`   :math:`q_1`         Objective Value
============= =================== =======================
0             0                   0
0             1                   0.1
1             0                   0.1
1             1                   0
============= =================== =======================

Thus, when we run many anneals---also known as *samples* or *reads*---of this problem on the D-Wave system,
we expect the ground states (0,0) and (1,1) to be strongly favored over the excited states (0,1) and (1,0)
in the returned results.

Here are the results from running this problem on a D-Wave 2000Q system 1000 times, to obtain a sample of
1000 solutions:

======= ====== ================
Energy  State  Occurrences
======= ====== ================
0       (0,0)  555
0       (1,1)  443
0.1     (0,1)  1
0.1     (1,0)  1
======= ====== ================

If we run this problem again, we expect the numbers associated with energy 0 to vary, but to stay near the number 500
(50% of the samples). In a perfect system, we do not expect either of the ground states to be dominant over the other,
in a statistical sense; however, each run will yield different numbers.

Notice that---although the vast majority of the results are (0,0) and (1,1)---if we call the QPU enough times,
we occasionally see some (0,1) and (1,0) solutions. For more complex QUBOs, this process of repeatedly solving
the same problem to get a range of answers is called sampling and has powerful applications in many areas
including machine learning.

Problem Scaling
===================================

Consider another 2-qubit problem, this time with different values assigned to the qubit biases (0.5)
and coupler strength (-1). Notice that this problem is scaled uniformly from the previous (multiplied by 5):

.. math::
	:nowrap:

	\begin{equation}
		f(\vc{s}) = 0.5 q_1 + 0.5 q_2 - q_1 q_2
	\end{equation}

This problem, too, favors the states (0,0) and (1,1), but the objective value for the excited states is now 0.5
as opposed to 0.1 in the first problem; see below.

============= =================== =======================
:math:`q_0`   :math:`q_1`         Objective Value
============= =================== =======================
 0             0                  0
 0             1                  0.5
 1             0                  0.5
 1             1                  0
============= =================== =======================

Because the values for the excited states are different from those in the previous problem, resulting in a larger energy
gap between the ground state and the excited states (0.5 versus 0.1), we might expect to see different results this time.
In other words, when there is a larger gap between the ground state and the excited states, we expect that the excited
states are harder to reach and therefore less favored.

Recall that in the first problem, we saw a tiny fraction of excited states in the returned results. Contrary to what
we might expect, if we run both problems many times, we generally observe the same results despite the
(apparent) larger gap in the second problem.

This result is caused by a feature of the D-Wave system known as *auto-scaling*. Each QPU has an allowed
range of values for the biases and strengths of :math:`a` and :math:`b`. Unless we explicitly disable auto-scaling,
the D-Wave software adjusts the :math:`a` and :math:`b` values of a problem to take the entire (:math:`a,b`) range available before
sending it to the QPU. As a result, by the time these two problems are run, they present the same (:math:`a,b`) values to the QPU,
and therefore the returned solutions are effectively the same. When the energies and objective values are reported at the end
of the runs, we are using the pre-scaling values.

To test this, let's run 1000 reads of the first problem (in which the objective value for the excited states is 0.1)
with auto-scaling disabled. This time, we see results like those shown below.

======= ====== ================
Energy  State  Occurrences
======= ====== ================
0       (0,0)  272
0       (1,1)  536
0.1     (0,1)  124
0.1     (1,0)  68
======= ====== ================

When we run 1000 reads of the second problem (in which the objective value for the excited states is 0.5)
with auto-scaling disabled, we see results such as those shown below.

======= ===== ================
Energy  State Occurrences
======= ===== ================
0       (0,0) 436
0       (1,1) 563
0.5     (0,1) 1
0.5     (1,0) 0
======= ===== ================

These results illustrate that without scaling, the first problem has a smaller gap than the second,
and returns more samples of the excited states.
