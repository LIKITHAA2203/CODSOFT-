import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("Dataset (1).csv")

# Drop rows with missing coordinates or ratings
df = df.dropna(subset=['Latitude', 'Longitude', 'Aggregate rating'])

# Optional: Filter for high-rating restaurants (just for visual clarity)
df_filtered = df[df['Aggregate rating'] > 0]

# Plot map using Plotly
fig = px.scatter_geo(
    df_filtered,
    lat='Latitude',
    lon='Longitude',
    color='Aggregate rating',
    hover_name='Restaurant Name',
    hover_data={'City': True, 'Cuisines': True, 'Aggregate rating': True},
    color_continuous_scale='Viridis',
    title='Restaurant Ratings Across Locations'
)

fig.update_layout(geo=dict(
    showland=True,
    landcolor='lightgray',
    showcountries=True,
    showcountries=True,
))

fig.show()


---

📦 Installation (once only):

pip install plotly pandas
