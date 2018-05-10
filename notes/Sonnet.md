---
layout: post
title: Functional algebra
category: notes
---

Inspired by [Sonnet's](https://github.com/deepmind/sonnet) abstractions for
parameterised functions I want to revisit  [FAT](https://github.com/act65/FAT).


In Sonnet each function has a forward pass, typical the only real part is written out.
And implicity has a backward gradient function that is build from each op having
its gradient defined. (thus they are kind of like duals, forward - backward)
Sonnet seems to extend this idea to the inverse function (or transpose as they call it).


<!-- Relationship between;
nilpotent duals, automatic differentiation, functional programming, sonnet, FAT, linear algebra. -->

Let $\mathcal F$ be the set of ???.
Define $f \in \mathcal F$ such that;

<side>It seems important have a weaker notion of identity/equality/inversion here?
One that is approximately true, this makes it possible to satisfy the inverse condition.
And can be true when these functions are learned.
So the invserse exists if there is an approximation that can achieve error within $\epsilon$</side>
$$
\begin{align}
\exists & f^{-1}: f^{-1} \circ f \approx identity \approx f \circ f^{-1} \\
\exists & \nabla f: \nabla \cdot f^T \\
\exists & \nabla f^{-1}: ??? \\
\end{align}
$$

So to define an algebra (field? group? ???) over the (reals?) we need;
identity, inverse, closure, ?!?, ...
What sets could it work on? What about different datastructures?
Instead of arrays, graphs?

<side>this is true for reverse mode AD, but not necessarily true in general.
need to work with chain rule</side>
$$
\begin{align}
y = B(A(x)) \equiv ?? \\
f = A \circ B =
\begin{bmatrix}
I & 0 & 0 \\
A & 0 & 0 \\
0 & B & 0 \\
\end{bmatrix} \\
\nabla f = \nabla B \circ \nabla A =
\begin{bmatrix}
I & A & 0 \\
0 & 0 & B \\
0 & 0 & I \\
\end{bmatrix} \\
\end{align}
$$


<side>If we can impose some structure on C, such as being the non-linear
equivalent of diagonal - diagonalisation!?? Then we can find the invariants (B)
under the transform A.</side>
$$
\begin{align}
\text{Let } A, B, C \in \mathcal F \\
\text{Let } B \circ A = A \circ C \\
B = A \circ C \circ A^{-1} \\
\end{align}
$$


Would like to be able to do more algebra with these functionals. However, their
non-linearity stops us from doing much. How can we impose a minimal amount of
structure (like types) to different functionals that will allow us more room to
play with? For example if we knew that A was an orthgogonal transform, only using
relus as its non-linearily then we could ... ???

So what `types` of structured function could we have?
- orthogonal transform?
- what nuances/distinctions/structure are there within different non-linear transforms?
  - one that warps space in a 'convex' manner? ( i am thinking of something like x**3. which stretches away from linear, but doesnt map back onto itself, or rotate)
  - periodic non-linearities
  - if it doesnt map back onto itself, then the transform will have a perfect inverse

Hmm. How do loss functions fit into this framework? So we have the composition of non-linear functions, but
what these functions end up learning/doing is determined by how they are trained, on what loss!
Does this need to be added as part of the structure, or is it somehow separate?
After all, loss functions are non-linear functions themselves, but with no parameters.

<!-- how could group theory come into this? symmetry, parameter sharing, ...? -->
<!-- functional quarternions -->
