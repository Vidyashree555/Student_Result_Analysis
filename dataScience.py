
#Student Result Analysis Project with Python & Data Analysis


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"D:\MCA_Data_Science Project\student_scores.csv")
print(df.head())

df.describe()

df.info()

df.isnull().sum()

#drop unnamed column
df=df.drop("Unnamed: 0", axis = 1)
print(df.head())

#change weekly study hr column
df["WklyStudyHours"]=df["WklyStudyHours"].str.replace("5-oct","5-10")
df.head()

#gender distribution
plt.figure(figsize= (4,4))
ax=sns.countplot(data = df, x = "Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()

#from the above displayed chart we have analyzed that the number of females in the data is more than the number of males
gb=df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)

plt.figure(figsize= (4,4))
sns.heatmap(gb, annot = True)
plt.title("Relationship between Parent's Education and student's Score")
plt.show()

#from the above chart we are concluded that the education of the parents have a good impact on their course
gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb1)

#from the above chart we have concluded that there is no?neglagible impact on the student score due to their parents marital status
sns.boxplot(data = df, x = "MathScore")
plt.show()

sns.boxplot(data = df, x = "ReadingScore")
plt.show()

sns.boxplot(data = df, x = "WritingScore")
plt.show()

df['EthnicGroup'].fillna(df['EthnicGroup'].mode()[0], inplace=True)
# Standardize 'EthnicGroup' labels to lowercase
df['EthnicGroup'] = df['EthnicGroup'].str.lower()
# Count occurrences of each ethnic group
group_counts = df['EthnicGroup'].value_counts()
# Plot pie chart
plt.pie(group_counts, labels=group_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Ethnic Groups')
plt.show()

print(df.columns)
df.columns = df.columns.str.strip().str.lower()
if 'ethnicgroup' in df.columns:
    ax = sns.countplot(data=df, x='ethnicgroup', palette='viridis')
    ax.bar_label(ax.containers[0])
    plt.title("Ethnic Group Distribution")
    plt.show()
else:
    print("'ethnicgroup' column not found in the DataFrame.")
if 'ethnicgroup' in df.columns:
    df['ethnicgroup'].fillna(df['ethnicgroup'].mode()[0], inplace=True)
if 'ethnicgroup' in df.columns:
    df['ethnicgroup'] = df['ethnicgroup'].str.lower()















