import streamlit as st
import pandas as pd

# Load recommendations
recommendations_df = pd.read_csv("recommendations.csv")

st.title("📖 Pratilipi Story Recommendation System")

# User input
user_id = st.number_input("Enter User ID:", min_value=int(recommendations_df['user_id'].min()), 
                          max_value=int(recommendations_df['user_id'].max()), step=1)

# Show recommendations
if st.button("Get Recommendations"):
    user_recs = recommendations_df[recommendations_df['user_id'] == user_id]
    
    if not user_recs.empty:
        recs = user_recs.iloc[0, 1:].tolist()
        st.write(f"📚 Recommended Stories for User {user_id}:")
        st.write(recs)
    else:
        st.error("User ID not found. Try another.")
