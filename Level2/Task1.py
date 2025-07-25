import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Dataset (1).csv")

# --- 1. Percentage of restaurants offering table booking and online delivery ---
table_booking_pct = df['Has Table booking'].value_counts(normalize=True) * 100
online_delivery_pct = df['Has Online delivery'].value_counts(normalize=True) * 100

print("📊 Table Booking Availability (%):")
print(table_booking_pct)
print("\n📦 Online Delivery Availability (%):")
print(online_delivery_pct)

# --- 2. Compare average ratings: table booking vs no table booking ---
avg_rating_with_booking = df[df['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
avg_rating_without_booking = df[df['Has Table booking'] == 'No']['Aggregate rating'].mean()

print(f"\n⭐ Average Rating (With Table Booking): {avg_rating_with_booking:.2f}")
print(f"⭐ Average Rating (Without Table Booking): {avg_rating_without_booking:.2f}")

# Bar plot for comparison
plt.figure(figsize=(6, 4))
sns.barplot(x=['With Booking', 'Without Booking'],
            y=[avg_rating_with_booking, avg_rating_without_booking],
            palette='Set2')
plt.title('Average Ratings: Table Booking vs No Booking')
plt.ylabel('Aggregate Rating')
plt.tight_layout()
plt.show()
