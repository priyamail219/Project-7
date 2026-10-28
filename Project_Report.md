# Project Report: Disaster Tweet Classification using NLP

## 1. Introduction
Social media can carry important information during emergencies. This project builds a binary text-classification pipeline to estimate whether a tweet refers to a real disaster or is unrelated/figurative.

## 2. Objectives
- Explore a labelled tweet dataset.
- Clean and transform tweet text into numerical features.
- Train and compare baseline classification models.
- Evaluate performance with suitable classification metrics.
- Save the selected model and provide a simple web interface.

## 3. Methodology
The notebook loads a labelled CSV, checks missing values and class distribution, removes URLs and unnecessary symbols, and prepares a cleaned text column. TF-IDF features represent individual words and two-word phrases. Logistic Regression and Multinomial Naive Bayes are trained and compared. A stratified 80/20 train-test split is used, with 3-fold cross-validation on the training subset.

## 4. Evaluation
The notebook reports accuracy, precision, recall, F1-score, and a classification report. It also displays a confusion matrix, ROC curve, and precision-recall curve where supported. Actual results must be inserted after running the notebook on the provided dataset; no performance numbers are fabricated in this report.

## 5. Deployment
The trained TF-IDF/classifier pipeline is saved as `disaster_tweet_model.joblib`. The Streamlit application loads this file and accepts a tweet in a text box, then displays the predicted class and (when available) the model-estimated probability for the disaster class.

## 6. Limitations
Language is context-dependent, so a word associated with disaster may appear in a metaphorical expression. Model quality depends on dataset size, representativeness, and label quality. The app is a prototype for learning and is not intended to replace official emergency services.

## 7. Conclusion
The project demonstrates an end-to-end NLP workflow, from data exploration and feature engineering to model evaluation and a lightweight interface. Its final performance and conclusions should be based on measured results from the actual labelled dataset.
