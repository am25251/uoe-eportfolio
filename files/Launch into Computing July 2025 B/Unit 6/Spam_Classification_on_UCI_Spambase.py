# Import the libraries
import pandas as pd # Analysis and manipulation of the dataset
from sklearn.model_selection import train_test_split # Splitting the data into a test and training sets (Pedregosa, 2011)
from sklearn.ensemble import RandomForestClassifier # Machine learning model: Random Forest (Pedregosa, 2011)
from sklearn.metrics import recall_score, precision_score, accuracy_score, classification_report # Evaluation metrics

#  load the dataset 
# Spambase dataset URL main dataset hosted on the UCI Machine Learning Repository (Hopkins, 1999)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
# URL to the .names file
column_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.names"

# Read the dataset from the URL from the UCI Machine Learning Repository using Pandas (Testas, 2023)
df = pd.read_csv(url, header=None)

# split features and labels
# 1 = spam, 0 = not spam
X = df.iloc[:, :-1]  # Extracts the target labels (spam = 1, not spam = 0) from the last column
y = df.iloc[:, -1]   # Extracts the feature columns -everything except the target label

# I split the dataset into training (70%) and testing (30%) sets
# Ensuring the same random split every time the code is run is the purpose of random_state (reproducibility)
# 70% for training, 30% for testing; use random_state for reproducibility
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42 # (Pedregosa, 2011)
)

# Initialize the Random Forest classifier with a seed for reproducibility
model = RandomForestClassifier(random_state=24)
# Train the model using the training data
model.fit(X_train, y_train)  # Fit the model to the training data

# Generate predictions on the test data using the trained classifier
# Predict outcomes for the test set
y_pred = model.predict(X_test)

# Assess the model’s performance using accuracy, precision, and recall metrics
accuracy = accuracy_score(y_test, y_pred)

# precision: of predicted spams, how many were actually spam
# important to reduce false positives
precision = precision_score(y_test, y_pred)

# Recall: Of actual spams, how many were correctly identified
# in order to avoid missing true spam
recall = recall_score(y_test, y_pred)

# output the results
# Print overall performance metrics
print("**** Evaluation Metrics ****")
print(f"Accuracy:  {accuracy:.4f}")    # Overall correctness
print(f"Precision: {precision:.4f}")   # How many predicted spams are really spam
print(f"Recall:    {recall:.4f}")      # How many actual spams were caught

# Classification report includes F1-score and support for each class
print("\n*** Classification Report ***")
print(classification_report(y_test, y_pred))
