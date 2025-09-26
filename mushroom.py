import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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

new_mushroom_data_raw = pd.DataFrame({
    'cap-shape': ['x'], 'cap-surface': ['s'], 'cap-color': ['n'], 
    'bruises': ['t'], 'odor': ['a'], 'gill-attachment': ['f'],
    'gill-spacing': ['c'], 'gill-size': ['n'], 'gill-color': ['k'],
    'stalk-shape': ['e'], 'stalk-root': ['e'], 'stalk-surface-above-ring': ['s'],
    'stalk-surface-below-ring': ['s'], 'stalk-color-above-ring': ['w'],
    'stalk-color-below-ring': ['w'], 'veil-type': ['p'], 'veil-color': ['w'],
    'ring-number': ['o'], 'ring-type': ['p'], 'spore-print-color': ['n'],
    'population': ['n'], 'habitat': ['g']
})

new_mushroom_data = new_mushroom_data_raw.copy()
for column in new_mushroom_data.columns:
    if column in label_encoder:
        le = label_encoder[column]
        new_mushroom_data[column] = le.transform(new_mushroom_data[column])
        
predicted_label = model.predict(new_mushroom_data)

predicted_class_raw = label_encoder['class'].inverse_transform(predicted_label)

print(f"The predicted class for the new mushroom is: {predicted_class_raw[0]}")

class_names = label_encoder['class'].classes_ 

disp = ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, display_labels=class_names)
disp.ax_.set_xlabel("Predicted Label")
disp.ax_.set_ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()

