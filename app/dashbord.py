from explainerdashboard import ClassifierExplainer, ExplainerDashboard
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


if __name__ == '__main__':
    df = pd.read_csv('preprocessed.csv')
    X = df[
        ['Administrative',
         'Administrative_Duration',
         'Informational',
         'Informational_Duration',
         'ProductRelated_Duration',
         'BounceRates',
         'PageValues',
         'SpecialDay']
    ]
    y = df['Revenue']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42)

    scaler = MinMaxScaler()
    X_train_transformed = scaler.fit_transform(X_train)
    X_test_transformed = pd.DataFrame(scaler.transform(X_test), columns=[
                                      'Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration', 'ProductRelated_Duration', 'BounceRates', 'PageValues', 'SpecialDay'])

    model = joblib.load('logreg_model.pkl')

    explainer = ClassifierExplainer(model, X_test_transformed, y_test)
    db = ExplainerDashboard(explainer)
    db.to_yaml("dashboard.yaml", explainerfile="explainer.joblib",
               dump_explainer=True)
