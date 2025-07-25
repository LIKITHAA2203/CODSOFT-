# Length of restaurant name and address
df['name_length'] = df['Restaurant Name'].apply(lambda x: len(str(x)))
df['address_length'] = df['Address'].apply(lambda x: len(str(x)))
# Encode 'Has Table booking' and 'Has Online delivery'
df['has_table_booking'] = df['Has Table booking'].apply(lambda x: 1 if x.strip().lower() == 'yes' else 0)
df['has_online_delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x.strip().lower() == 'yes' else 0)
# Encode 'Rating text' as an ordinal variable
rating_text_order = {
    'Excellent': 5,
    'Very Good': 4,
    'Good': 3,
    'Average': 2,
    'Poor': 1,
    'Not rated': 0
}
df['rating_text_encoded'] = df['Rating text'].map(rating_text_order)
