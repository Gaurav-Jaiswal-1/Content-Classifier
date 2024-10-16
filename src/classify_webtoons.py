import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Sample webtoon descriptions and their categories
data = r'C:\Users\Gaurav\OneDrive\Desktop\Task 1\Content-Classifier\data\webtoons_data.csv'


# Split the data into descriptions and categories
descriptions = [item['Paragraph'] for item in data]
title = [item['Heading'] for item in data]

# Convert descriptions into TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(descriptions)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, title, test_size=0.3, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Show classification report
print(classification_report(y_test, y_pred))
