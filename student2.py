import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("score.csv")

print("No of null columns")
print(df.isnull().sum())
df = df.dropna()

df['Hours'] = pd.to_numeric(df['Hours'],errors='coerce')
df['Scores'] = pd.to_numeric(df['Scores'],errors='coerce')

bins = [0, 50, 75, 100]  
labels = ['0-50 Marks', '51-75 Marks', '76-100 Marks'] 
df['Score_Category'] = pd.cut(df['Scores'], bins=bins, labels=labels, right=True)

le = LabelEncoder()
le.fit(df['Score_Category']) 
df['Score_Category_Encoded'] = le.transform(df['Score_Category']) 

X = df[['Hours']]
y = df['Score_Category_Encoded'] 

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression(multi_class='multinomial',max_iter=1000)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

value_dict = {
    'Hours' : 5
}

new_data = pd.DataFrame([value_dict])

predicted_score = model.predict(new_data)
predicted_category = le.inverse_transform(predicted_score) 
print(f"Predicted Score : {predicted_category[0]}")
