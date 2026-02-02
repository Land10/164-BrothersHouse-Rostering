import streamlit as st
import random
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="House Chores Roster", page_icon="🏠", layout="centered")

# --- 🖼️ Background Settings ---
# Replace this URL with any image you like (e.g., from Unsplash)
bg_image_url = "https://images.unsplash.com/photo-1513694203232-719a280e022f?q=80&w=2069&auto=format&fit=crop"

# Fancy Custom CSS
st.markdown(f"""
    <style>
    /* CORE MODIFICATION: Background Image + White Semi-transparent Overlay */
    .stApp {{
        /* The linear-gradient acts as a white overlay.
           rgba(255, 255, 255, 0.75): 255 is white, 0.75 is opacity (0=transparent, 1=solid)
        */
        background-image: linear-gradient(rgba(255,255,255,0.75), rgba(255,255,255,0.75)), url("{bg_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Button Style */
    .stButton>button {{
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
    }}
    .stButton>button:active {{
        transform: scale(0.98);
    }}
    
    /* Input Areas: Semi-transparent to blend with background */
    .stTextArea textarea {{
        border-radius: 10px !important;
        font-size: 16px !important;
        background-color: rgba(255, 255, 255, 0.8) !important;
    }}
    
    /* Expander Container Style */
    div[data-testid="stExpander"] {{
        border: none !important;
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 15px !important;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
    }}
    
    /* Verse Card Style */
    .verse-card {{
        background-color: rgba(255, 255, 255, 0.9);
        border-left: 5px solid #FF4B4B;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }}
    .verse-text {{
        font-style: italic;
        color: #333;
        font-size: 1.05em;
        margin: 0;
    }}
    .verse-ref {{
        font-weight: bold;
        color: #FF4B4B;
        margin-top: 5px;
        text-align: right;
        font-size: 0.9em;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 Chores System")

# --- ✨ NEW FANCY SUBTITLE ✨ ---
st.markdown("""
    <div style="text-align: center; margin-top: -15px; margin-bottom: 25px;">
        <span style="
            font-size: 1.3rem;
            font-weight: 800;
            letter-spacing: 1px;
            background: linear-gradient(90deg, #FF4B4B, #FF8E53);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 2px 2px 4px rgba(255,255,255,0.5);
        ">
        ✨ HOUSE OF JESUS LOVER ✨
        </span>
    </div>
    """, unsafe_allow_html=True)
# --------------------------------

# --- ✝️ BIBLE VERSE DISPLAY ---
verses = [
    ("Psalm 133:1", "How good and pleasant it is when God’s people live together in unity!"),
    ("Colossians 3:23", "Whatever you do, work at it with all your heart, as working for the Lord, not for human masters."),
    ("Galatians 6:2", "Carry each other’s burdens, and in this way you will fulfill the law of Christ."),
    ("1 Peter 4:10", "Each of you should use whatever gift you have received to serve others, as faithful stewards of God’s grace."),
    ("Proverbs 27:17", "As iron sharpens iron, so one person sharpens another."),
    ("Philippians 2:3", "Do nothing out of selfish ambition or vain conceit. Rather, in humility value others above yourselves."),
    ("1 Corinthians 10:31", "So whether you eat or drink or whatever you do, do it all for the glory of God.")
]

ref, text = random.choice(verses)

st.markdown(f"""
<div class="verse-card">
    <p class="verse-text">“{text}”</p>
    <div class="verse-ref">📖 {ref}</div>
</div>
""", unsafe_allow_html=True)
# -------------------------------------------

# Input Section
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

brothers = [name.strip() for name in brothers_input.split('\n') if name.strip()]
chores = [chore.strip() for chore in chores_input.split('\n') if chore.strip()]

st.divider()

# Action Section
if st.button("🚀 TAP TO PAIR", type="primary"):
    if len(brothers) != len(chores):
        st.error(f"⚠️ **Count Mismatch!**\n\nBrothers: {len(brothers)} | Chores: {len(chores)}")
    elif not brothers:
        st.warning("Please enter some names first!")
    else:
        shuffled_chores = list(chores)
        random.shuffle(shuffled_chores)
        
        results_df = pd.DataFrame({
            "Brother": brothers,
            "Task": shuffled_chores
        })
        
        st.success("🎉 Assignment Complete!")
        
        # Displaying the result table
        st.dataframe(results_df, use_container_width=True, hide_index=True)
        
        st.balloons()
        st.info("💡 Tap the button again to reshuffle!")

# Sidebar
with st.sidebar:
    st.header("Help")
    st.write("Ensure the number of brothers matches the number of chores.")