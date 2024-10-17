import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('E-commerce Company Insights')
st.write('Here is our LLM generated dashboard')
import matplotlib.pyplot as plt

# Data
genders = ['Male', 'Female']
user_counts = [49688, 50312]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(genders, user_counts, color=['blue', 'pink'])
plt.title('Number of Users by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Users')

st.pyplot()
