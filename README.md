# FAT

Functional Arrays and Tensors. 
Fatrix: a matrix of functions.
Fensor: a tensor of functions.

Goal: To design a framework for thinking about networks/graphs as structured arrays.
Why: To have a formal toolset for understanding structure in networks. To help answer the question of how structure and function are related.
What: An extension of numpy libraries (ndarrays) to allow a functional type of linear algebra on matricies/tensors. 

    Traditional dot
    a, b  .  e,  f   =  a.e + b.g, a.f + b.h
    c, d     g,  h   =  c.e + d.g, c.f + d.h
    Fdot
    a, b  .  e,  f   =  a(e) + b(g), a(f) + b(h)
    c, d     g,  h   =  c(e) + d(g), c(f) + d(h)
    
Potential applications
* Engineering: Can be used to easily build computational graphs (e.g. in tensorflow).
* Science: The structure of common neural network, like CNNs, RNNs, ResNets, show some interesting patterns when represented with FAT. See [this](https://github.com/act65/FAT/blob/master/Modular%20nets.ipynb) for some examples.
* Math: ?? how does this contribute to math literature? See [this]() for a formal definition of the langauge.


# To-do
### Need
* Decide on and define algebra on fatrixes
    * Composition
    * ??
* Generalise to tensors
* Formulate the problem it is solving, make sure this is well motivated
* Make working examples for well known/interesting architectures
    * CNNs
    * RNNs
    * Resnets
    * Ladder nets
    * ???

### Want
* Implementation in other languages? (Haskell, ??)
* Make some pretty pics to help people understand
* A nice way to work with derivatives??