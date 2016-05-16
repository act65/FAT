# FAT
Functional Arrays and Tensors. Fatrix - a functional matrix.
An extension of numpy libraries with matrices to allow a functional type of matrix algebra. 
Can be used to build computational graphs ..
Also, an excuse for me to learn about functional programming and some higher order math.

    Traditional dot
    a, b  .  e,  f   =  a.e + b.g, a.f + b.h
    c, d     g,  h   =  c.e + d.g, c.f + d.h
    Fdot
    a, b  .  e,  f   =  a(e) + b(g), a(f) + b(h)
    c, d     g,  h   =  c(e) + d(g), c(f) + d(h)
    
The motivation being that when you look at the fatrixes of common neural network structures, like CNNs, RNNs, ResNets, … etc you start to see some interesting patterns in the structure of the fatrices. See [this](https://github.com/act65/FAT/blob/master/Modular%20nets.ipynb) for more details and motivation.


# To-do
### Need
* Decide on and define algebra on fatrixes
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
