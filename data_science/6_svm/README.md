### SVM

#### Theory
 - Read about SVM from ISLR pages 337-359
 - Answer questions 3,6 in exercise section (pages 368,370)
#### Exercise
  - **Part 1**
    - In this exercise we assume the hypothesis we want to learn is classification by y=1-x:
      Class = 1 if y>1-x, otherwise 0
    - Create a train dataset by generating 1000 labeled points
    - Create a test dataset by generating 1000 unlabeled points
    - Classify each point using svm with different kernels, try at least 3 kernels (use native sklearn for the svm)
    - For each kernel create a plot with these features:
        - Correctly classified points in blue
        - Incorrectly classified points in red
        - Separating line 
     - What is the difference in total train and test time between different kernels?
     - Choose the most suitable kernel in your opinion (of course - justify it) and use it in the following parts.
    - **Part 2** 
         - Extend the hypothesis for higher dimension while keeping the training and test sets balanced. Classify each point according to your chosen kernel. How are the training and test times depend upon the dimension? (what is the relation)
         - Denote the number of train samples N, and the dimension P. Test samples number is fixed. For every region N<<P, N=P, N>>P show the test error. Plot all results one informative graph.
     - **Part 3** - 
        - Repeat the exercise 1 with hypothesis boundary of a circle located at (0.5,0.5) with radius of size 0.25. No need to plot separating line.
        - Try this using linear kernel and using polynomial kernel of deg 2.

