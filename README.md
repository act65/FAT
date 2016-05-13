# FAT
An extension of numpy libraries with matricies to allow a functional type of algebra. 
Can be used to build computational graphs 

The goal is to make matricies work with functions. Something like

    Traditional dot
    a, b  .  e,  f   =  a.e + b.g, a.f + b.h
    c, d     g,  h   =  c.e + d.g, c.f + d.h
    
    Fdot
    a, b  .  e,  f   =  a(e) + b(g), a(f) + b(h)
    c, d     g,  h   =  c(e) + d(g), c(f) + d(h)
    
The motivation being that when you look at 
