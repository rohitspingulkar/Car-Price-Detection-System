# Car-Price-Detection-System

In this project i have taken the data set from kaggle, link is in the description below and also the data is in repo
So first I analysed the data and all the subtraction and reduction is there in the python notebook
Reduced the column data to one hot encoding so that it will be eaiser for the model to train and give accurate results.

After all the data preprocessing steps i created lists of hyper parameters or you can say a default value dictionary for hyperparameters 
This is done in order to get the best possible hyper parameters for our model
Here we are using Random Forest Regressor for building ML model and the hyper parameters are calculated by Randomized Search CV.

RandomizedSearchCV implements a “fit” and a “score” method. It also implements “score_samples”, “predict”, “predict_proba”, “decision_function”, “transform” and “inverse_transform” if they are implemented in the estimator used.

The parameters of the estimator used to apply these methods are optimized by cross-validated search over parameter settings.

In contrast to GridSearchCV, not all parameter values are tried out, but rather a fixed number of parameter settings is sampled from the specified distributions. The number of parameter settings that are tried is given by n_iter.

If all parameters are presented as a list, sampling without replacement is performed. If at least one parameter is given as a distribution, sampling with replacement is used. It is highly recommended to use continuous distributions for continuous parameters.

So after fitting the model i did model predictions and accuracy test and it came out to be pretty good.

For the deployment of the app i used basic tkinter, the best, the clean and very basic.

Preview of the app:

![Screenshot (14)](https://user-images.githubusercontent.com/36771361/127529267-bc08d3fb-e48c-4ace-bcb3-d15fc8e02efd.png)         


![Screenshot (16)](https://user-images.githubusercontent.com/36771361/127529464-12160744-3866-40be-90a4-d0fef6d64a0b.png)

Nice and easy project for beginers.
Any doubts you can directly contact me on email or git.

Kaggle Data Link : https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho
