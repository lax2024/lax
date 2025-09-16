import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load dataset
columns=['buying','maint','doors','persons','lug_boot','safety','class']
df=pd.read_csv("car.data", names=columns)

print("null value under each column")
print(df.isnull().sum())

# Encode categorical data
label_encoder = {}
for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoder[column] = le

# Features and target
X = df.drop(columns=["class"])
y = df["class"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(multi_class="multinomial", max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Correct evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
