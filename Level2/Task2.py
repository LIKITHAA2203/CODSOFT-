import pandas as pd
# Load the dataset
df = pd.read_csv("Dataset  (1).csv")
# Display first few rows
df.head()
# Most common price range
most_common_price_range = df['price range'].mode()[0]
print(f"Most common price range: {most_common_price_range}")
# Average rating per price range
avg_rating_by_price_range = df.groupby('price range')['aggregate rating'].mean()
print("Average rating by price range:")
print(avg_rating_by_price_range)
# Color corresponding to highest avg rating
highest_avg_rating_price_range = avg_rating_by_price_range.idxmax()

# Find the color(s) associated with that price range
color_of_highest_avg_rating = df[df['price range'] == highest_avg_rating_price_range]['rating color'].mode()[0]
print(f"Rating color with highest average rating: {color_of_highest_avg_rating}")
