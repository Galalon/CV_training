### Classification
#### Theory
 - **Introduction** - Read in ISLR pages 127-130.
 - **Logistic regression** - Read 130-138 in ISLR.
 - **Naïve Bayes** - Read attached file:  Naïve Bayes Explained.
 - **LDA** - Read 138-150 in ISLR.
#### Exercise

##### Basic classification - KNN:
 - Implement vectorized KNN and compare your solution to the sklearn method.
 - Do the exercise in the attached notebook - it is taken from C231 exercises which you will do in the later parts of the trainning.
 - You can read the Knn extension in the preamble in the [following link](https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/)
  (be careful not to read  the answers).
 - Additional files and functions for the notebook can be found [here](https://cs231n.github.io/assignments2022/assignment1/#q1-k-nearest-neighbor-classifier)
 - Read Read 151-154 in ISLR and compare different classification methods.  

##### Classification methods:

 - In this exercise, we will use Iris dataset (attached) which classifies flower into 3 classes (SetosaSilky, Versicolour, Virginica) according to biological measurements.
 - Each example has four properties:
    - Sepal Length.
    - Sepal Width.
    - Petal Length.
    - Petal Width.
 - Your task is to build a classifier that has maximum precision for an engagement classification for the three categories above.
    - Explore the data and show your findings.
    - Test different models (use sklearn) and compare them.
    - Show your best model and draw conclusions.
    - If you find the dataset too easy to classify, you are welcome to challenge yourself with more advanced datasets, for example the wine dataset (sklearn.datasets.load_wine)
