import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("Housing.csv")

for col in ['mainroad', 'guestroom', 'basement', 'prefarea']:
    df[col] = df[col].map({'yes': 1, 'no': 0})

df['bedrooms'] = pd.to_numeric(df['bedrooms'], errors='coerce')
df['bathrooms'] = pd.to_numeric(df['bathrooms'], errors='coerce')

print("Null values in each column")
print(df.isnull().sum())
df = df.dropna()

features = ['bedrooms', 'bathrooms', 'mainroad', 'guestroom', 'basement', 'prefarea']

X = df[features]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

value_dict = {
    'bedrooms': 3,
    'bathrooms': 2,
    'mainroad': 1,
    'guestroom': 0,
    'basement': 1,
    'prefarea': 0
}

new_data = pd.DataFrame([value_dict])

predicted_price = model.predict(new_data)
print(f"Predicted price for new data: {predicted_price[0]}")
