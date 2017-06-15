---
layout: post
title: A functional type of linear algebra?
category: notes
---

A quick overview of what is going on at [this](https://github.com/act65/FAT) repository.

# Functional linear algebra

So (I think we would agree) that matrix multiplication looks something like this.

$$
\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix}
\cdot
\begin{bmatrix}
e & f\\
g & h\\
\end{bmatrix}
=
\begin{bmatrix}
ae+bg & af+bh\\
ce+dg & cf+dh\\
\end{bmatrix}
$$


**What happens if we did this?**


$$
\textbf{F}(\textbf{V}) =
\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix}
\begin{pmatrix}
e & f\\
g & h\\
\end{pmatrix}=
\begin{bmatrix}
a(e)+b(g) & a(f)+b(h)\\
c(e)+d(g) & c(f)+d(h)\\
\end{bmatrix}
$$


Elements in $\textbf{F}$ are functions (that take one argument - although I would like to allow for more). And elements in $\textbf{V}$ are variables. (I started calling the functional matrix, $\textbf{F}$, a fatrix, as a placeholder for something better, but I havent come up with anything better... any ideas?)

**Why would we bother?** Well;

* linear algebra with non-linearities (although this sounds somewhat silly).
* Traditional linear algebra is a special case of this framework
    * e.g. set $a(e)$ to be the function $a(e) = const\times e$.
* Allows us to recursively build higher level functions.
    * Since $\textbf{F}$ is just a function, we can use it as an element in another 'higher level' fatrix.
* Can be used to represent a computational graph.

# Application(s)

These are some examples of using this functional matrix algebra to represent the computational graph of some recent neural network architectures.
![Fatrix]({{ site.baseurl }}/images/Fatrix.png)
See [this folder](https://github.com/act65/FAT/tree/master/Examples) for derivations of these pictures.
