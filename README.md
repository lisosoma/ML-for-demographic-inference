# Application of machine learning methods for approximate prediction of demographic history parameters by the allele-frequency spectrum

Bioinformatics Institute, 2022

Author: E. E. Gorelkina

Supervisor: E. E. Noskova

## Goals

Full-fledged genetic data are not used to output demographic history parameters, as they require a lot of computing resources. Therefore, they use various statistics based on these data. One of these statistics is the allele-frequency spectrum. In the simplest case, it can be represented as a multidimensional tensor (matrix). Existing methods for deriving demographic history parameters (dadi, moments) use local optimization algorithms that work faster for given initial approximations of parameters close to optimal. In this project, it is proposed to apply the simplest machine learning methods for approximate prediction of the parameters of the demographic history of two populations. As machine learning algorithms, a choice is offered: random forest or convolutional neural networks. It is required to generate data, train and validate the selected method on them.

![pred1](ML-for-demographic-inference/pred1.jpeg)
