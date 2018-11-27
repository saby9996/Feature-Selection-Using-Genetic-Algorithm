# Feature Selection Using-Genetic Algorithm 
The Feature Selection Technique depicted in the project utilizes Evolutionary Genetic Algorithms to leverage the selection of features on the best performing model.
Moreover the project uses, DEAP Framework for mutating round the Genetic Population of the Feature Subsets.

####Usage of the Algorithm:
```
from FeatureGA import FeatureSelectionGA 
model=Estimator() #### Can be Any Supervised Model of Choice
FeatureSelectionGA(model, features.values, labels.values)
```
####Parameters
```
model : sci-kit-learn supported model,
features :  {array-like}, shape = (n_samples, n_features)
labels  : {array-like}, shape = (n_samples)
cv_split: (int) Number of splits for cross_validation to calculate fitness.
Random State: As Specified
n_pop: It will be Identified to determine the Population Size
n_gen: It would be Identified to determine the Number of Generation
```