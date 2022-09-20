# Basic libraries for data processing
import numpy as np
import pandas as pd

# Visualization tools
import matplotlib.pyplot as plt
import seaborn as sns

# Classifiers
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB 
from xgboost.sklearn import XGBClassifier

# Evaluation tools
from sklearn.metrics import confusion_matrix, classification_report
from yellowbrick.model_selection import feature_importances

#===============================================================================================#

# Classification Models Class

#===============================================================================================#

class Classification():
    
    """
    This class aims to perform Classifcation using Logistic Regression, Decision Tree, Random Forest, Naive Bayes, AdaBoost, Stacking Classifier, and XGBoost.
    
    Parameters
    ----------
    model_type: 'Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM'
    the type of classifcation algorithm you would like to apply 
    
    x_train: dataframe
    the independent variables of the training data
    
    x_val: dataframe
    the independent variables of the validation data
    
    y_train: series
    the target variable of the training data
    
    y_val: series
    the target variable of the validation data
    
    """
    
    def __init__(self,model_type,x_train,x_val,y_train,y_val):

        self.model_type = model_type
        self.x_train = x_train
        self.y_train = y_train
        self.x_val = x_val
        self.y_val = y_val
        self.scores_table = pd.DataFrame()
        self.feature_importances = pd.DataFrame()
        self.name = self
        
        if self.model_type == 'Logistic Regression':
            self.technique = LogisticRegression(solver='lbfgs', max_iter=1000)
        elif self.model_type == 'Decision Tree':
            self.technique = DecisionTreeClassifier(random_state=42)
        elif self.model_type == 'Random Forest':
            self.technique = RandomForestClassifier(n_estimators=20,n_jobs=-1,random_state=42)
        elif self.model_type == 'SVM':
            self.technique = SVC()
        elif self.model_type == 'Multinomial Naive Bayes':
            self.technique = MultinomialNB()
        elif self.model_type == 'KNN':
            self.technique = KNeighborsClassifier(n_jobs=-1)
        elif self.model_type == "AdaBoost":
            self.technique = AdaBoostClassifier(algorithm='SAMME')
        elif self.model_type == "XGBoost":
            self.technique = XGBClassifier(n_jobs=-1)
            
#===============================================================================================#

# Score Function

#===============================================================================================#

    def scores(self,model,x_train,x_val,y_train,y_val):
        
        """
        Gets the accuracy for the given data and creates a dataframe containing scores.
        Parameters
        ----------
        model: 'Logistic Regression', 'Decision Tree', 'Random Forest', 'SVM'
        the type of classifcation applied
        x_train: dataframe
        the independant variables of the training data
        x_val: dataframe
        the independant variables of the validation data
        y_train: series
        the target variable of the training data
        y_val: series
        the target variable of the validation data
        
        Returns
        ----------
        scores_table: a dataframe with the model used, the train accuracy and validation accuracy
        """
        
        self.acc_train = self.best_model.score(x_train,y_train)
        self.acc_val = self.best_model.score(x_val,y_val)
        
        d = {'Model Name': [self.model_type],
             'Train Accuracy': [self.acc_train], 
             'Validation Accuracy': [self.acc_val],
             'Accuracy Difference':[self.acc_train-self.acc_val]}
        self.scores_table = pd.DataFrame(data=d)
        
        return self.scores_table


#===============================================================================================#

# Get Scores Function

#===============================================================================================#

    def get_scores(self,params,cv_type):
        
        """
        Performs a gridsearch cross validation with given hyperparameters and data.
        Gets the accuracy for the given data and creates a dataframe containing scores.
        Parameters
        ----------
        param_grid: dictionary 
        specified hyperparameters for chosen classification algorithm to be passed through gridsearch cross validation
        
        cv_type: 'skf'
        the type of cross validation split to be used for gridsearch
        """
        
        classifier = self.technique
        fit_classifier = classifier.fit(self.x_train,self.y_train)
        opt_model = GridSearchCV(fit_classifier,
                                 params,
                                 cv=cv_type,
                                 scoring='accuracy',
                                 return_train_score=True,
                                 n_jobs=-1)
        self.opt_model = opt_model.fit(self.x_train,self.y_train) 
        self.best_model = opt_model.best_estimator_
        self.scores = Classification.scores(self,self.best_model,self.x_train,self.x_val,self.y_train,self.y_val)
        self.best_params = opt_model.best_params_
        display(self.scores_table)
        if params == {}:
            pass
        else:
            print("The best hyperparameters are: ", self.best_params,'\n')
        self.y_validated = self.best_model.predict(self.x_val)
        self.classification_report = pd.DataFrame.from_dict(classification_report(self.y_val,self.y_validated,output_dict=True)).iloc[0:3,0:5]
        return self.classification_report

#===============================================================================================#

# Feature Importance Function

#===============================================================================================#
   
    def get_feature_importances(self):
        
        """
        Create a confusion matrix.
        Returns
        ----------
        feature_importances_bar : a bar chart with feature importance of given model
        """
        if (self.model_type == 'Decision Tree') or (self.model_type == 'Random Forest') or (self.model_type == 'SVM'):    
            self.feature_importances_table = pd.DataFrame(self.best_model.feature_importances_,
                                                    index = self.x_train.columns,
                                                    columns=['Importance']).sort_values('Importance',ascending =False)
            plt.figure(figsize=(9,7.5))
            self.feature_importances_bar = sns.barplot(y= self.feature_importances_table.index[:15], x= self.feature_importances_table['Importance'][:15])
            plt.show()
            return self.feature_importances_bar
        
        else:
            return print('This classification method does not have the attribute feature importance.')

#===============================================================================================#

# Confusion Matrix Function

#===============================================================================================#

    def conf_matrix(self):
        
        """
        Create a confusion matrix.
        
        Returns
        ----------
        scores_table: a confusion matrix
        """
        
        plt.figure(figsize=(9,9))
        ax = sns.heatmap(confusion_matrix(self.y_val, self.y_validated),
                         annot= True, 
                         fmt = '.4g', 
                         cbar=0,
                         xticklabels=[1,2,3,4,5],
                         yticklabels=[1,2,3,4,5])
        ax.set(xlabel='Predicted', ylabel='True')
        plt.show()



#===============================================================================================#

# Test Score Function

#===============================================================================================#

    def get_test_scores(self,X_test,y_test):
        
        """
        Gets a ROC AUC score for given data and creates a dataframe containing scores.
        Creates a ROC plot.
        
        Parameters
        ----------
        x_test: dataframe 
        independant variables of the test data
        
        y_test: dataframe 
        target variable of the test data
        """
            
        self.y_test = y_test
        self.x_test = X_test
        self.scores_table = pd.DataFrame()
        self.test_scores = Classification.scores(self,self.best_model,self.x_train,self.x_test,self.y_train,self.y_test)
        display(self.scores_table)
        self.y_tested = self.best_model.predict(self.x_test)
        self.test_classification_report = pd.DataFrame.from_dict(classification_report(self.y_test,self.y_tested,output_dict=True)).iloc[0:3,0:5]
        
        return self.test_classification_report
    
#===============================================================================================#

# Show Test Confusion Matrix Function

#===============================================================================================#

    def test_conf_matrix(self):
        
        """
        Create a confusion matrix for the test data.
        
        Returns
        ----------
        scores_table: a confusion matrix
        """
        plt.figure(figsize=(9,9))
        ax = sns.heatmap(confusion_matrix(self.y_test, self.y_tested),
                         annot= True, 
                         fmt = '.4g', 
                         cbar=0,
                         xticklabels=[1,2,3,4,5],
                         yticklabels=[1,2,3,4,5])
        ax.set(xlabel='Predicted', ylabel='True')
        plt.show()