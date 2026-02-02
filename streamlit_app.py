import streamlit as st
import random
import pandas as pd

# 1. Page Configuration - 'centered' is best for mobile
st.set_page_config(page_title="House Chores Roster", page_icon="🏠", layout="centered")

# Fancy Custom CSS for Mobile
st.markdown("""
    <style>
    /* Gradient background for a fancy look */
    .stApp {
        background: linear-gradient(180deg, #fdfbfb 0%, #ebedee 100%);
    }
    /* Make buttons huge and "tappable" for thumbs */
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 4em;
        background: linear-gradient(90deg, #FF4B4B, #FF7575);
        color: white;
        font-weight: bold;
        font-size: 1.2rem;
        border: none;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:active {
        transform: scale(0.98);
    }
    /* Rounded input boxes */
    .stTextArea textarea {
        border-radius: 10px !important;
        font-size: 16px !important; /* Prevents iOS auto-zoom */
    }
    /* Custom card-like containers */
    div[data-testid="stExpander"] {
        border: none !important;
        background-color: white !important;
        border-radius: 15px !important;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 Chores System")
st.markdown("*House of Jesus Lover!*")

# 2. Input Section - Using Expanders to save vertical space on phone screens
with st.expander("📝 Edit Names & Tasks", expanded=True):
    st.markdown("##### 👤 Brothers")
    brothers_input = st.text_area("List names below", 
                                 value="Alex\nBryan\nJohn\nMin Khang\nSin Ngu\nYile\nDeng Jie\nXiu Qing\nAaron", 
                                 height=150,
                                 label_visibility="collapsed")
    
    st.markdown("##### 🧹 Chores")
    chores_input = st.text_area("List chores below", 
                               value="Staircase\nBack Yard\nFront Yard\nDining Table\nMop Floor\nToilet\nInside Kitchen\nSweep Floor\nOutside Kitchen", 
                               height=150,
                               label_visibility="collapsed")

# Clean data
brothers = [name.strip() for name in brothers_input.split('\n') if name.strip()]
chores = [chore.strip() for chore in chores_input.split('\n') if chore.strip()]

st.divider()

# 3. Action Section
if st.button("🚀 TAP TO PAIR", type="primary"):
    if len(brothers) != len(chores):
        st.error(f"⚠️ **Count Mismatch!**\n\nBrothers: {len(brothers)} | Chores: {len(chores)}")
    elif not brothers:
        st.warning("Please enter some names first!")
    else:
        # Fresh shuffle logic
        shuffled_chores = list(chores)
        random.shuffle(shuffled_chores)
        
        results_df = pd.DataFrame({
            "Brother": brothers,
            "Task": shuffled_chores
        })
        
        st.success("🎉 Assignment Complete!")
        
        # 'use_container_width' ensures it fits the phone screen perfectly
        st.dataframe(results_df, use_container_width=True, hide_index=True)
        
        st.balloons()
        st.info("💡 Tap the button again to reshuffle!")

# Sidebar for extra info
with st.sidebar:
    st.header("Help")
    st.write("Ensuring the number of brothers matches the number of chores.")