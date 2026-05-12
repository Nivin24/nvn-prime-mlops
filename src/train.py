import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import json 
import os


def train_model():
    """Load data from data/ dir tracked by DVC"""

    df = pd.read_csv('data/nvn_prime_data.csv')

    X = df.drop(['churn_label', 'timestamp', 'customer_id'], axis=1)
    X = pd.get_dummies(X)
    y = df['churn_label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Training
    model = XGBClassifier()
    model.fit(X_train, y_train)

    # Evaluate
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)

    # Save Artifacts
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/churn_model.pkl')

    # Save Metrics for DVC to track
    with open('metrics.json', 'w') as f:
        json.dump({'accuracy' : acc}, f)

    print(f"Training Complete. Accuracy : {acc}")

if __name__ == "__main__":
    train_model()



