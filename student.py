import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("score.csv")

print("No of null columns")
print(df.isnull().sum())
df = df.dropna()

df['Hours'] = pd.to_numeric(df['Hours'], errors='coerce')
df['Scores'] = pd.to_numeric(df['Scores'], errors='coerce')

X = df[['Hours']]
y = df[['Scores']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

value_dict = {
  'Hours' : 5
}

new_data = pd.DataFrame([value_dict])

predicted_score = model.predict(new_data)
print(f"Predicted score: {predicted_score[0]}")

