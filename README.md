# Disaster Tweet Classification — NLP Project

**Student:** Priya  
**Project type:** Natural Language Processing / Binary Text Classification

## Files included
- `Disaster_Tweet_Classification_Priya.ipynb` — notebook covering data exploration, cleaning, TF-IDF feature extraction, model comparison, evaluation, examples, and model saving.
- `app.py` — Streamlit interface for classifying a tweet.
- `requirements.txt` — Python dependencies.
- `README.md` — setup and usage instructions.

## Dataset
Use a labelled disaster-tweet CSV with a tweet text column (usually `text`) and a binary target column (usually `target`, where 0 = non-disaster and 1 = disaster-related). The assignment describes a dataset of approximately 10,000 labelled tweets and links to a dataset, but the actual CSV was not included in the assignment PDF uploaded here.

Save the dataset as `train.csv` in the project folder. If your CSV uses different column names, edit `TEXT_COL` and `TARGET_COL` in the notebook.

## Run the notebook
1. Create and activate a virtual environment (recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the notebook:
   ```bash
   jupyter notebook Disaster_Tweet_Classification_Priya.ipynb
   ```
4. Run the cells from top to bottom.
5. The notebook saves `disaster_tweet_model.joblib` after training.

## Run the web app
After completing the notebook and generating the model file, run:
```bash
streamlit run app.py
```

## Methods used
- Text cleaning with regular expressions
- TF-IDF vectorization with unigrams and bigrams
- Logistic Regression and Multinomial Naive Bayes
- Stratified train/test split and 3-fold cross-validation on training data
- Accuracy, precision, recall, F1-score, confusion matrix, ROC curve, and precision-recall curve

## Notes
- Do not report performance values until you have run the notebook on the actual dataset.
- The app is a learning prototype. It is not an official disaster alert system and predictions need human verification.
- If you were given a classmate's README or app, use it as a reference for learning, but submit work you understand and can explain. Update the student/course details honestly and follow your institute's rules.
