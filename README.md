
# Statistical Data Analysis on Meteorological Data

This project is done in the context of the course *Statistical Computation and Visualization*, taught by [Mehdi Gholam](https://people.epfl.ch/mehdi.gholam?lang=fr) at EPFL.

## Tools and Languages

<img align="left" alt="Visual Studio Code" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png" />

<img align="left" alt="Python" width="26px" src="https://camo.githubusercontent.com/0fd2667849df9f18b863a2fc9fdf275d28c0e69bae657009213dbbba08295d02/68747470733a2f2f7261772e6769746875622e636f6d2f436972636c6543492d5075626c69632f63696d672d707974686f6e2f6d61737465722f696d672f636972636c652d707974686f6e2e7376673f73616e6974697a653d74727565" />

<img align="left" alt="C++" width="26px" 
src="https://raw.githubusercontent.com/isocpp/logos/master/cpp_logo.png" />

<img align="left" alt="Overleaf" width="26px" 
src="https://pbs.twimg.com/profile_images/551035690234834945/JhdUiOPP.png" />

<br />
<br />

## Table of Content

* [People](#people)
* [Description](#description)
* [Project Organization](#project-organization)
* [Related Articles and Useful References](#refs)
* [Interesting Material 🔍](#material)

## People

[Luca Bracone](https://people.epfl.ch/luca.bracone)
[Luca Nyckees](https://people.epfl.ch/luca.nyckees)
[Blerton Rashiti](https://people.epfl.ch/blerton.rashiti)
[Kieran Vaudaux](https://people.epfl.ch/kieran.vaudaux)

## Description

Zigzag persistence, as introduced by Carlsson and De Silva [[1]](https://arxiv.org/abs/0812.0197), offers a way to better understand the persistence of topological features observed in a family of spaces or pointclouds by generalizing the setting of persistent homology. In this project, we aim at providing a tool to compute levelset zigzag persistence. The idea is to deduce the results from computations on extended persistence, which are already implemented in C++. To this end, we make use of Python bindings.

<img width="450" alt="figure" src="https://github.com/LucaNyckees/zigzag/blob/main/figures/11-Figure2-1.png">

A bijection between the extended persistence barcode and the zigzag barcode can be established via so-called "diamond moves", involving the presence of relative Mayer-Vietoris diamonds, illustrated in the animation below. The precise statement is formulated as the *Strong Diamond Principle* - sometimes called the *Pyramid Theorem* - in [[1]](https://arxiv.org/abs/0812.0197). The whole process relies on consecutive transformations between two sequences of spaces that differ only at one point, so that the difference can be expressed by a relative Mayer-Vietoris diamond.

<img width="550" alt="figure" src="https://github.com/LucaNyckees/zigzag/blob/main/figures/pyramid_zigzag.gif">

## Project Organization
------------

    ├── README.md          -- Top-level README.
    │
    ├── notebooks          -- Jupyter notebooks.
    │
    ├── articles           -- Related articles and useful references.
    │
    ├── reports            -- Notes and report (Latex, pdf).
    │ 
    ├── figures            -- Optional graphics and figures to be included in the report.
    │
    ├── requirements.txt   -- Requirements file for reproducibility.
    └── src                -- Project source code.
   
--------

## Related Articles and Useful References

[[1]](https://arxiv.org/abs/0812.0197) - Zigzag Persistence\
[[2]](https://arxiv.org/abs/2105.00518) - Computing Optimal Persitent Cycles for Levelset Zigzag on Manifold-like Complexes\
[[3]](https://arxiv.org/abs/0911.2142) - Quantifying Transversality by Measuring the Robustness of Intersections\
[[4]](https://www.mrzv.org/publications/robustness-levelsets/esa/) - The Robustness of Level Sets

## Interesting Material 🔍

+ Tutorial on Python bindings [[click here]](https://realpython.com/python-bindings-overview/)
+ Video lectures on topological data analysis by Henry Adams [[click here]](https://www.math.colostate.edu/~adams/teaching/dsci475spr2021/)

