import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("Dataset (1).csv")

# Fill missing values
df['Cuisines'] = df['Cuisines'].fillna('Not Specified')
df['Aggregate rating'] = df['Aggregate rating'].fillna(0)

# Select features and target
features = ['Votes', 'Price range', 'Has Online delivery', 'Has Table booking',
            'Is delivering now', 'Average Cost for two']
target = 'Aggregate rating'

# Encode categorical columns
le = LabelEncoder()
for col in ['Has Online delivery', 'Has Table booking', 'Is delivering now']:
    df[col] = le.fit_transform(df[col].astype(str))

# Drop rows with missing in selected features
df = df[features + [target]].dropna()

# Split dataset
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = Random ForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")
