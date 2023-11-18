# Datasets-with-Numpy-and-Sklearn
Use numpy and sklearn libraries in python to find correlations in datasets. Consider first the dataset file dataset-one.csv, which consists of 600 examples, each corresponding to a
patient where we have recorded how much exercise they get per week, and their cholesterol level. Note that this is simulated data: a higher number for exercise means the patient performed more exercise, and a higher number for cholesterol means the patient has a higher level of cholesterol (there are no units for these simulated measurements). Later, we will consider a second dataset file dataset-two.csv, which consists of the same 600 examples, except that we include the “age” of each patient, in addition to their levels of exercise and cholesterol.

## Suppose that we learn a linear model y = ax + b to predict a patient’s cholesterol level (y) given their exercise level (x). What is the resulting co-efficient a based on the dataset dataset-one.csv? Does the co-efficient suggest positive correlation or negative correlation between x and y? (Note that if you use the linear regression module in the python scikit-learn module, this coefficient appears in the coef_ member variable).
.7231 Positive Correlation

## Consider dataset-two.csv which includes the age of each patient. Suppose that we split the patients into different age groups, in their 20s (20-29), in their 30s (30-39), and so on, up the the age group in their 70s (70-79). Suppose that we again learn a linear model y = ax + b to predict a patient’s cholesterol level (y) given their exercise level (x). However, say we learn a different model for each age group, using only that age group’s data. What are the resoluting co-efficients a for each of the 6 different age groups in the dataset? Do the resulting co-efficients suggest positive correlation or negative correlation between x and y?
Negative Correlation
20-29: -0.6156
30-39: -0.6394 
40-49: -0.6018 
50-59: -0.6602 
60-69: -0.5922 
70-79: -0.7321

## The analysis that we performed in part (1) and part (2) uses the same pool of patients, except that in part (2) we incorporated the patients’ ages in the analysis. Further, we (should) have observed two different trends in each analysis. Which trend do you intuitively believe should be the correct one, and why? (This is an open-ended question).
Based on the coefficient from dataset 1, the correlation between exercise and cholesterol was positive but correlation was negative when dividing up the dataset and its model by age. Intuitively I would say that the second dataset/trend is correct because it is known that exercise is generally healthier and as a result would be more likely to decrease cholesterol.
