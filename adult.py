import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("adult.csv")

print("No of null columns")
print(df.isnull().sum())
df = df.dropna()

columns = ["age","workclass","fnlwgt","education","education.num","marital.status","occupation","relationship","race","sex","capital.gain","capital.loss","hours.per.week","native.country"]

X = df[columns]
y = df['income']

X_test,X_train,y_test,y_train = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression(multi_class='multinomial',max_iter=1000)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

val

