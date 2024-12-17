# Youtube Comments Sentiment Analysis Project
## 1. Overall
- In this project, we perform Sentiment Analysis on YouTube comments to classify user feedback into three categories: Neutral, Negative, and Positive. This kind of analysis helps to understand how audiences are reacting to content, identify trends in user sentiment, and gain insights into viewer engagement.
## 2. Methodology
- **Data Collection**:
Gathered comments from YouTube videos using the YouTube API or from pre-existing datasets.
Each comment is labeled with a sentiment score: 0 (Neutral), 1 (Negative), or 2 (Positive).
- **Exploratory Data Analysis (EDA)**:
Visualized the distribution of comments based on sentiment.
Created word clouds to highlight the most common words in positive and negative comments.
Examined the relationship between comment features (e.g., comment length) and sentiment labels using boxplots and density plots.
- **Data Preprocessing**:
Cleaned the text data by removing noise such as URLs, special characters, and extra spaces.
Tokenized the comments, converting them into a list of meaningful words.
Performed additional text processing like lowercasing, removing stop words, and lemmatization.
- **Feature Extraction**:
Extracted useful features such as comment length, average word length, or word count.
Used advanced text representations like TF-IDF (Term Frequency-Inverse Document Frequency) to convert comments into numerical vectors.
- **Model Training**:
Trained various machine learning models (such as Logistic Regression, Naive Bayes, and Random Forest) to classify comments based on sentiment.
Also implemented deep learning models like RoBERTa for more accurate text classification.
- **Evaluation**:
Evaluated model performance using metrics such as accuracy, precision, recall, and F1-score.
Visualized the results with confusion matrices and classification reports.


<!-- - youtube api key: AIzaSyAAwY-uPy6XUHBh0cV1u4yHPTyYzxskNgI -->
