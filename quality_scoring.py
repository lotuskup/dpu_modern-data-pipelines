import pandas as pd


df = pd.read_csv("titanic.csv")
print(df.head())

# วิธีการเรียกดูค่าใน Column
# df["Survived"]
# df.Survived

df.info()

age_not_null = df.Age.notnull()
dq_age = age_not_null.sum() / len(age_not_null)
print(f"Data Quality of Age: {dq_age}")

cabin_not_null = df.Cabin.notnull()
dq_cabin = cabin_not_null.sum() / len(cabin_not_null)
print(f"Data Quality of Cabin: {dq_cabin}")

embarked_not_null = df.Embarked.notnull()
dq_embarked = embarked_not_null.sum() / len(embarked_not_null)
print(f"Data Quality of Embarked: {dq_embarked}")
print(f"Completeness: {(dq_age + dq_cabin + dq_embarked) / 3}")
print(f"-------------------------------------")
## หา Data Quality ของแต่ละคอลัมน์
columns = ['PassengerId','Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

dq_list = []  # เก็บค่า Data Quality ของแต่ละคอลัมน์

for col in columns:
    not_null = df[col].notnull()
    dq = not_null.sum() / len(not_null)
    dq_list.append(dq)  # เก็บค่า Data Quality ในลิสต์
    print(f"Data Quality of {col}: {dq}")
    
# คำนวณค่า Completeness โดยหาค่าเฉลี่ยของ Data Quality ทั้งหมด
completeness = sum(dq_list) / len(dq_list)
print(f"Completeness: {completeness}")

