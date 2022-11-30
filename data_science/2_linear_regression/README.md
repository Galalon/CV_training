### My first model (Linear regression)
#### Theory
 - Read chapter 3 in ISLR - Linear Regression.
 - Read chapter 5 in ISLR - Resampling Methods.
 - Read chapter 6, parts 6.1 and 6.2 in ISLR - Linear Model Selection. 
 - Explain to yourself and to your supervisor the following:
    - What is the advantage of using sequential learning for fitting linear model over the analytical solution?
    - What is the geometrical meaning of the least square solution to linear regression?
    - Why does L1 regularization tend to make coefficients vanish exactly, while L2 doesn’t?
    - What is the bias-variance tradeoff?
#### Exercise
 - In the community of the data-scientist there are several known datasets which comprise a benchmark for the community. The data on the neighborhood prices in California is one of them.
 fetch_california_housing
 - The reservoir contains not many records, on neighborhoods in Boston and the average housing prices. Each neighborhood has several information items that can help predict the average price in the neighborhood.
 - The repository is modeled after  the first datasets that were created in the field - the boston dataset. The original dataset was deemed not politically correct as it was written in the 50's and had features the encurage racism.
   Both datasets are not large and therefore the question of the fitting rises more sharply. Use sklearn load the data into your notebook.

 - Then follow the steps of the classical study (of course it's just a template, and you should be making frequent iterations with the tutor at this time, and repeat the steps after the new comments):
     - Explore the data, for example:
         - Test for distributions and correlations
         - Understand the meaning of the columns, values and units of measurements
      - Clean the data, for example:
         - Complete missing values
         - Remove information which constitute anomalies (you can do it manually - this is not an anomaly detection exercise).
     - Split the data for training and testing
  
  - Fit a linear regression model with target as the response and medinc as the predictor. Do this in 3 ways:
     - Analytically.
     - Sequential Learning.
     - Sklearn's build in predictor.
  - Plot the data along the fitted line. What does the model predict for medinc=3?
   - From now use only sklearn predictor.
   - Fit a linear regression model using medinc and a new feature that is equal to two times medinc. What happened?
   - Fit a linear regression model using all features.
   - Fit a linear regression model using all features except population. Did your prediction become better?
   - Using linear regression, compute a parabolic least-squares fit for the target variable using only medinc. Plot your result. Did this improve upon your fit from the linear reggression?
   - Investigate what happens when plotting a polynomial regression of higher order with regularization. Use both L1 and L2 and plot the qualitive behaviour of the coefficients in each case. What combination would you choose for your final model?
   - Extract new features as you see fit to improve your model performance.  
