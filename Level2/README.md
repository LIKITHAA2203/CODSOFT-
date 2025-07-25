Leve2_Task1_table_booking_delivery.pyLevel 2 – Task 1: Table Booking & Online Delivery Analysis

This task analyzes how restaurants provide table booking and online delivery, and how that relates to pricing and customer ratings.

#### ✅ What was done

- Calculated the percentage of restaurants that:
  - Offer table booking
  - Offer online delivery
- Compared **average ratings** between restaurants with and without table booking
- Analyzed **online delivery** across different **price ranges**
- Visualized comparisons using bar charts

#### 📚 Libraries Used

- `pandas`
- `matplotlib`
- `seaborn`

#### ▶️ How to Run

```bash
python Level2_Task1_table_booking_delivery.py



✅ Task 2: Price Range Analysis

Objectives:

Determine the most common price range among restaurants

Calculate average rating for each price range

Identify the rating color representing the highest average rating


Key Code Highlights:

# Most common price range
df['price range'].mode()[0]

# Average rating per price range
df.groupby('price range')['aggregate rating'].mean()

# Color with highest average rating
df[df['price range'] == highest]['rating color'].mode()[0]


---

✅ Task 3: Feature Engineering

Objectives:

Create new features from existing data

Encode categorical columns into numerical values


Newly Engineered Features:

name_length: Length of restaurant name

address_length: Length of address

has_table_booking: 1 if table booking is available, else 0

has_online_delivery: 1 if online delivery is available, else 0

rating_text_encoded: Numerical mapping of rating text

----

TOOLS USED :

Python

Pandas

NumPy

Jupyter Notebook
