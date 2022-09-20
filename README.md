# Yelp Dataset Exploration and Sentiment Analysis

![project_header](https://github.com/adzict/yelp_sentiment_analysis/blob/main/images/yelp_logo.png)

## Table of Contents

1. [ Project Introduction ](#Project_Introduction)
2. [ Technologies Used ](#Technologies_Used)    
3. [ Methods Used ](#Methods_Used)
4. [ Project Description ](#Project_Description)
   * [ 1. Data Sources ](#Data_Sources)
   * [ 2. File Descriptions ](#File_Descriptions) 
5. [ Feature Notebooks and Deliverables ](#Notebooks_deliverables)
6. [ Most Important Findings ](#Findings)
   * [1. Which categories of businesses are getting top reviews?](#business_cat)
   * [2. How often do businesses get reviewed over time?](#frequency_reviews)
   * [3. Which business categories get bad reviews?](#bad_reviews)
   * [4. Accuracy results of Sentiment Analysis using VADER](#vader)
   * [5. Predicting the sentiment using different classifiers](#modeling)
   * [6. Conclusion and Feature Recommendations](#conclusion)
7. [ Acknowledgments ](#Acknowledgments)
8. [ Licences ](#Licences)
9. [ Contact ](#Contact)

## Project Introduction
<a name="Project_Introduction"></a>

The aim of the project is to predict the sentiment of a Yelp review, and make actionable recommendations to businesses that will help them understand customer needs, and monitor customer feedback.

## Technologies Used
<a name="Technologies_Used"></a>
* [Python](https://www.python.org/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [NLTK](https://www.nltk.org/)
* [scikit-learn](https://scikit-learn.org/stable/)

## Methods Used
<a name="Methods_Used"></a>
* Data Processing / Data Cleaning
* Data Analysis
* Descriptive Statistics
* Feature Engineering
* Data Visualization
* Text Preprocessing
* Sentiment Analysis
* Predictive Modeling and Hyperparameter Tuning
* Evaluating Model Results
* Reporting

## Project Description
<a name="Project_Description"></a>

The Yelp dataset is a collection of businesses, reviews, and user data, intended for learning purposes, published by Yelp. It contains over 8 million reviews for 200 thousand businesses in 10 metropolitan areas of the US. The dataset that will be used for the purposes of sentiment analysis and prediction will contain businesses from the Phoenix, AZ metropolitan area.

I will explore the dataset to gain valuable insights of businesses working in this area, and then proceed to perform sentiment analysis of the reviews, and make actionable recommendations to businesses that will help them understand customer needs, and monitor customer feedback. Out last step will include predicting the sentiment of a Yelp review. 

A very important step is asking questions we need to give answers to. As part of my mentorship I was tasked to answer the following:

* Gain different insights by exploring the dataset
* What businesses are getting top reviews?
* Which categories of businesses are getting top reviews?
* How often do businesses get reviewed over time?
* How do the categories of trending and top reviewed businesses differ?
* Which business categories get bad reviews?
* What are the most common words in bad reviews?
* Build a machine learning model to predict the sentiment of Yelp reviews.
* Predict or recommend something else.

### Data Sources
<a name="Data_Sources"></a>

The dataset used for this project can be found on the data.world website: [yelp_reviews.csv](https://data.world/brianray/yelp-reviews)

The complete Yelp Dataset can be found on their website: [Yelp Dataset](https://www.yelp.com/dataset) 

### File Descriptions
<a name="File_Descriptions"></a>

* [Data](https://github.com/adzict/yelp_sentiment_analysis/tree/main/data) - folder containing processed data
* [Images](https://github.com/adzict/yelp_sentiment_analysis/tree/main/images) - folder containing assets such as images
* [1. Data Preprocessing and Basic EDA](https://github.com/adzict/yelp_sentiment_analysis/blob/main/1.%20Data%20Preprocessing%20and%20Basic%20EDA.ipynb)
* [2. Business Case Data Analysis](https://github.com/adzict/yelp_sentiment_analysis/blob/main/2.%20Business%20Case%20Data%20Analysis.ipynb)
* [3. Sentiment Analysis](https://github.com/adzict/yelp_sentiment_analysis/blob/main/3.%20Sentiment%20Analysis.ipynb)
* [4. Modeling and Evaluation]()
* [Classification.py](https://github.com/adzict/yelp_sentiment_analysis/blob/main/Classification.py)

## Feature Notebooks and Deliverables
<a name="Notebooks_deliverables"></a>
### Blog Posts

* Blog post on Yelp Reviews Sentiment Analysis: [project | Yelp Reviews Sentiment Analysis]()


### Structure of Notebooks
<details>
   <summary>Collapse</summary>

      1. Data Preprocessing and Basic EDA

            1. Imports
            2. Data
               2.1 Business Dataset
               2.2 Review Dataset
               2.3 User Dataset
            3. Early EDA and Data Cleaning
               3.1 Missing values
               3.2 Duplicate rows
               3.3 Removing unnecessary features
            4. Saving data for the next stage

      2. Business Case Data Analysis

            1. Imports
            2. Data
            3. Business Case Data Analysis
               3.1 What businesses are getting top reviews?
               3.2 Which categories of businesses are getting top reviews?
               3.3 How often do businesses get reviewed over time?
               3.4 How do the categories of trending and top reviewed businesses differ?
               3.5 Which business categories get bad reviews?
               3.6 What are the most common words in bad reviews?

      3. Sentiment Analysis

            1. Imports
            2. Data
            3. Sentiment Analysis
               3.1 Testing VADER with a random review
               3.2 Computing polarity scores
               3.3 Comparison Analysis of the compound score and the original label

      4. Modeling and Evaluation

            1. Imports
            2. Data
            3. Preparing Text
               3.1 Removing Missing values
               3.2 Creating three categories of labels from ratings
               3.3 Train/Test Split
               3.4 Vectorizing the text
            4. Classification
               4.1 Further splitting data into a train and validation set
               4.2 Logistic Regression
               4.3 Multinomial Naive Bayes
               4.4 Random Forest
               4.5 Decision Tree
               4.6 K Neighbors
               4.7 AdaBoost
               4.8 XGBoost
            5. Evaluation
               5.1 Comparing scores from all models
               5.2 Fitting the best model with test data
               5.3 Additional model metrics and tuning

</details>   


### Presentation
Link to the presentation: [presentation.pdf](link here)

## Most Important Findings
<a name="Findings"></a>

### 1. Which categories of businesses are getting top reviews?
<a name="business_cat"></a>

The top 10 categories of most reviewed businesses are as follows:

![top_10_categ_all](https://github.com/adzict/yelp_sentiment_analysis/blob/main/images/top_10_categ_all.png)

### 2. How often do businesses get reviewed over time?
<a name="frequency_reviews"></a>

### 3. Which business categories get bad reviews?
<a name="bad_reviews"></a>

### 4. Accuracy results of Sentiment Analysis using VADER
<a name="vader"></a>

### 5. Predicting the sentiment using different classifiers
<a name="modeling"></a>

### 6. Conclusion and Feature Recommendations
<a name="conclusion"></a>


## Acknowledgments
<a name="Acknowledgments"></a>

Thanks so much to [awesomeahi95](https://github.com/awesomeahi95) and their Classification.py script because I was able to learn a great deal about creating an usable and bug free script that can be reused for every classification problem, based on their work. 

## Licenses
<a name="Licences"></a>
[Database Contents License (DbCL) v1.0](https://opendatacommons.org/licenses/dbcl/1-0/)

## Contact
<a name="Contact"></a>
Find me on [LinkedIn](https://www.linkedin.com/in/tanja-ad%C5%BEi%C4%87/), [Twitter](https://twitter.com/adzic_tanja) or [adzictanja.com](https://www.adzictanja.com/).
