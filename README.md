# Application of machine learning methods to approximate demographic history parameters from allele frequency spectrum

*Bioinformatics Institute, 2022*

*Author: E. E. Gorelkina*

*Supervisor: E. E. Noskova*

## Goals

Сhoose a model of the demographic history of two populations on which the effectiveness of the methods will be explored;

Generate data using dadi library;

Train a machine learning Multi-Output Regression model that assumes all parameters are independent (model I);

Train a machine learning Multi-Output Regression model that assumes all parameters correlate (model II);

Validate models by R2 metric;

Reveal the number of iterations required for the random search to archive the same likelihood as ML model.

## Methods

To implement the pipeline was used Dadi package, in which there are methods that allow generating an allele-frequency spectrum according to the parameters of demographic history and counting the likelihood. 

Selected [demographic history model](https://github.com/noscode/demographic_inference_data/tree/master/2_DivMig_5_Sim) has five parameters that we want to predict. 

As a machine learning model, a random forest was taken as the simplest model.
## Results

### 1. Predicted vs true (independent parameters)

#### True: 
Size of subpopulation 1 after split: 1.0

Size of subpopulation 2 after split: 0.1

Migration rate from subpopulation 2 to subpopulation 1: 5.0

Migration rate from subpopulation 1 to subpopulation 2: 4.19419419

Time of split: 0.05

allele-frequency spectrum
![true1](/spectrums/true1.png)


#### Predict: 

Size of subpopulation 1 after split: 0.99994725

Size of subpopulation 2 after split: 0.1

Migration rate from subpopulation 2 to subpopulation 1: 4.99998889

Migration rate from subpopulation 1 to subpopulation 2: 4.19488176

Time of split: 0.05

allele-frequency spectrum
![pred11](/spectrums/pred11.png)

### 2. Predicted vs true (chained multioutput regression)

#### Predict: 

Size of subpopulation 1 after split: 0.99994725

Size of subpopulation 2 after split: 0.1

Migration rate from subpopulation 2 to subpopulation 1: 4.99998889

Migration rate from subpopulation 1 to subpopulation 2: 4.19393344

Time of split: 0.05

allele-frequency spectrum
![pred12](/spectrums/pred12.png)

## Conclusions

For the selected demographic history model and the selected machine learning model, the predictions turned out to be quite accurate.
The random search metric is interpreted as follows: if it is greater than 50 (such a number of random points is used in classical optimization), then we get acceleration. For all the models obtained, this metric was about 1000, that is, there is an acceleration of predictions.
For future research and development, this approach can be made more universal by training machine learning models on different demographic history models.
As an alternative possible machine learning model, you can use a convolutional network, for example, when there are three or more populations in the demographic history.

## References

Ekaterina Noskova's repository where the demographic history model was taken from: https://github.com/noscode/demographic_inference_data

Documentation for the Random Forest machine learning model: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor

Multiclass and multioutput algorithms: https://scikit-learn.org/stable/modules/multiclass.html#

Dadi package for generate allele-frequency spectrums: https://dadi.readthedocs.io/en/latest/api/dadi/
