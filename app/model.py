import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import joblib

if __name__ == '__main__':
    df = pd.read_csv('preprocessed.csv')
    X = df[['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration',
            'ProductRelated_Duration', 'BounceRates', 'PageValues', 'SpecialDay']]
    y = df['Revenue']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42)

    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)

    model = LogisticRegression(
        C=10000,
        class_weight='balanced',
        penalty='l2'
    )

    model.fit(X_train, y_train)
    joblib.dump(model, 'logreg_model.pkl')
