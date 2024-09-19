import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from fairlearn.metrics import MetricFrame
from sklearn.metrics import accuracy_score


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


if __name__ == "__main__":
    df = pd.read_csv('student_data_with_fake_pii.csv')
    df = df.drop(['StudentID', 'GPA', 'name', 'ssn'], axis=1)
    df['GradeClass'] = np.where(
        df['GradeClass'] == 1,
        1,
        0
    )

    y = df['GradeClass']
    x = df.drop('GradeClass', axis=1)

    model = RandomForestClassifier(max_depth=3, min_samples_leaf=5)
    model.fit(x, y)

    predictions = model.predict(x)
    mf = MetricFrame(metrics=accuracy_score, y_true=y, y_pred=predictions, sensitive_features=x['Ethnicity'])
    print(mf.by_group)
