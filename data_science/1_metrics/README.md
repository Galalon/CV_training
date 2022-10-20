### Metrics

#### Theory
 - Read the enclosed article: 20 Popular Machine Learning Metrics. Part 1: Classification & Regression 
   Evaluation Metrics
#### Exercise
  - In this folder there is a file called "CANCER_TABLE"   ,  This file has 1000 records.
  - Each record represents a biopsy taken from a test subject. The first column in the table represents the diameter of the biopsy, and the second column represents whether the subject was tested for cancer during a period of up to a year after the biopsy was performed. 
  - The "Marvel-Sabres" company offered a model that said: "If the tumor diameter is more than 7 cm, then the subject will be sick in the coming year and otherwise not". In this exercise we will analyze this model's performance.
	- Compute and display confusion matrix
    - Calculate the TP,TN,FP,FN metrics. What is their business meaning? 
    - Give business meaning to the TPR and FPR.
    - Calculate recall, accuracy and precision.
    - Calculate F1 score.

 - After analyzing your model, "Marvel-Sabres" offered an upgrade to the model: instead of a classified model, the company will provide a model that ranks the biopsies by their chances to represent a cancer patient (in the coming year). A higher ranking biopsy represents a higher likelihood that it is taken from a person who gets cancer in the coming year.
    - Why would such a model be good? Market it to a customer.
    - Draw a ROC  curve without using scikit-Learn  or any other structured function of python that does so.
    - Calculate the AUC. Is the model good in terms of this criterion? Give business meaning to the client.
    - Turn the rating model into a classification model using the ROC curve. Explain your answer well.
    - Again calculate confusion matrix.
    - Again calculate accuracy, precision, recall, TP, FP, TN, FN, TPR, FPR for the new model.
    - Compare the measures figured out in the previous section to those of the initial model. What model would you recommend?
    - Draw ROC curve again with scikit-Learn library functions while writing a minimum code on your part.
    