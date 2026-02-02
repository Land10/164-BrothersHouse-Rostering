import streamlit as st
import random
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="House Chores Roster", page_icon="🏠", layout="centered")

# Custom CSS to make it "Beautiful"
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    .stTextArea>div>div>textarea {
        background-color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 Chores Assignment System")
st.subheader("House of Jesus Lover!")
st.write("Enter the names and chores below to generate a random assignment.")

# 2. Input Section
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 👤 Brothers")
        brothers_input = st.text_area("One name per line", 
                                     value="Alex\nBryan\nJohn\nMin Khang\nSin Ngu\nYile\nDeng Jie\nXiu Qing\nAaron", 
                                     height=200)
        brothers = [name.strip() for name in brothers_input.split('\n') if name.strip()]

    with col2:
        st.markdown("### 🧹 Chores")
        chores_input = st.text_area("One chore per line", 
                                   value="Staircase\nBack Yard\nFront Yard\nDining Table\nMop Floor\nToilet\nInside Kitchen\nSweep Floor\nOutside Kitchen", 
                                   height=200)
        chores = [chore.strip() for chore in chores_input.split('\n') if chore.strip()]

st.divider()

# 3. Action Section
st.info("💡 **Tip:** If you aren't satisfied with the result, just click the **'Start to Pair'** button again to reshuffle!")

if st.button("🚀 Start to Pair", type="primary"):
    if len(brothers) != len(chores):
        st.error(f"⚠️ **Mismatch Found!** You have **{len(brothers)}** brothers but **{len(chores)}** chores. Please balance the numbers.")
    elif len(brothers) == 0:
        st.warning("Please enter names and chores first.")
    else:
        # Shuffle logic
        shuffled_chores = chores.copy()
        random.shuffle(shuffled_chores)
        
        # Combine into a DataFrame for better display
        results_df = pd.DataFrame({
            "Brother": brothers,
            "Assigned Chore": shuffled_chores
        })
        
        st.success("🎉 Pairing Successful!")
        
        # Displaying with a nice UI
        st.dataframe(results_df, use_container_width=True)
        st.balloons()

# Sidebar
st.sidebar.title("Help & Support")
st.sidebar.write("""
1. List brothers in the left box.
2. List tasks in the right box.
3. Ensure the count is the same.
4. Click Pair!
""")