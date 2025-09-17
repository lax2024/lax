import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

columns = ['class','cap-shape','cap-surface','cap-color','bruises','odor','gill-attachment',
           'gill-spacing','gill-size','gill-color','stalk-shape','stalk-root','stalk-surface-above-ring',
           'stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring',
           'veil-type','veil-color','ring-number','ring-type','spore-print-color','population','habitat']

df = pd.read_csv("agaricus-lepiota.data", names=columns)

print("Counts of '?' in columns:")
print((df == '?').sum())

# Replace '?' with a new category label
df.replace('?', 'missing', inplace=True)

label_encoder = {}
for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoder[column] = le

X = df.drop(columns=["class"])
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)  
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
