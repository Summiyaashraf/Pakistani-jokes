import streamlit as st
import requests

API_URL = "https://jokes-fastapi-production.up.railway.app/random_jokes"

# Function to fetch jokes
def get_pakistani_joke():
    """Fetch a random Pakistani joke from the FastAPI server"""
    try:
        response = requests.get(API_URL)  
        if response.status_code == 200:
            joke_data = response.json()
            return f"😂 **{joke_data.get('setup', 'Joke setup nahi mila!')}**\n\n👉 {joke_data.get('punchline', 'Punchline missing!')}"
        else:
            return "❌ Joke nahi mil saki. Phir try karein! 😅"
    except Exception as e:
        return f"⚠️ Koi masla hai! Shayad API band hai. 🤔\n\n_Error: {str(e)}_"

# Streamlit App
def main():
    # Set Page Config
    st.set_page_config(page_title="Pakistani Joke Generator", page_icon="😂", layout="centered")

    # Custom CSS for Styling
    st.markdown("""
        <style>
            body { background-color:rgb(239, 240, 240); }
            .stApp { text-align: center; }
            .joke-container { 
                background:rgb(51, 83, 244); 
                padding: 20px; 
                border-radius: 10px; 
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                font-size: 18px;
            }
            .footer {
                text-align: center; 
                font-size: 14px;
                margin-top: 30px;
                color: #555;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("<h1 style='text-align:center;'>🤣 Pakistani Joke Generator 🇵🇰</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align:center;'>Mazaydar Pakistani jokes ke liye button dabaayein! 😆</p>", unsafe_allow_html=True)

    # Button for Joke
    if st.button("🎭 Mujhe ek Pakistani joke sunao!"):
        joke = get_pakistani_joke()
        st.markdown(f"<div class='joke-container'>{joke}</div>", unsafe_allow_html=True)

    # Footer
    st.markdown(
        """
        <div class='footer'>
            Powered by <b>Pakistani Jokes API</b> 🎉 | Built with ❤ by 
            <a href='https://github.com/Summiyaashraf' target='_blank'>Summiya Ashraf</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
