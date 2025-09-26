import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("sales.csv")

# df['TV Ad Budget ($)'] = pd.to_numeric(df['TV Ad Budget ($)'], errors='coerce')
# df['Radio Ad Budget ($)'] = pd.to_numeric(df['Radio Ad Budget ($)'], errors='coerce')
# df['Newspaper Ad Budget ($)'] = pd.to_numeric(df['Newspaper Ad Budget ($)'], errors='coerce')

print("No of null values")
print(df.isnull().sum())
df = df.dropna()

budget = ["TV Ad Budget ($)","Radio Ad Budget ($)","Newspaper Ad Budget ($)"]
target = "Sales ($)"

X =  df[budget] 
y = df[[target]]

print(f"Total rows after cleaning: {len(X)}") 

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

value_dict = {
    'TV Ad Budget ($)' :200,
    'Radio Ad Budget ($)' : 150,
    'Newspaper Ad Budget ($)' : 100
}

new_data = pd.DataFrame([value_dict])
predict_data = model.predict(new_data)
print(f"Predicted sales : {predict_data[0][0]:.4f}")
