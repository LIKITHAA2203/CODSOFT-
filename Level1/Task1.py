import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Dataset (1).csv")

# 1. Dataset shape and basic info
print("Number of rows and columns:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

# 2. Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Fill missing 'Cuisines' with "Not specified"
df['Cuisines'].fillna('Not Specified', inplace=True)

# 3. Data type conversion
df['Country Code'] = df['Country Code'].astype(str)
df['Has Table booking'] = df['Has Table booking'].astype('category')
df['Has Online delivery'] = df['Has Online delivery'].astype('category')
df['Is delivering now'] = df['Is delivering now'].astype('category')

# 4. Target variable: Aggregate rating
print("\nAggregate rating description:\n", df['Aggregate rating'].describe())

# Plot distribution of Aggregate Rating
plt.figure(figsize=(8, 4))
sns.histplot(df['Aggregate rating'], bins=20, kde=True)
plt.title("Distribution of Aggregate Rating")
plt.xlabel("Aggregate Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 5. Class imbalance check
rating_counts = df['Aggregate rating'].value_counts().sort_index()
print("\nAggregate Rating Value Counts:\n", rating_counts)

# Bar plot of rating counts
plt.figure(figsize=(10, 5))
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="magma")
plt.title("Aggregate Rating Class Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

