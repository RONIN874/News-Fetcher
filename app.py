import streamlit as st
import time

# Import existing backend modules
from config import validate_config
from services.news_fetcher import fetch_articles
from agents.summarizer import summarize_all
from agents.brief_generator import generate_brief, generate_why_it_matters

# Configure the Streamlit page
st.set_page_config(
    page_title="News Fetcher",
    page_icon="📰",
    layout="wide"
)

# Enforce config validation before running UI logic
try:
    validate_config()
except ValueError as e:
    st.error(f"Configuration Error: {e}")
    st.stop()

# Main Title
st.title("📰 Morning News Brief Generator")
st.markdown("Transform scattered news articles into a quick, digestible morning briefing powered by AI.")

# ================= SIDEBAR =================
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("Customize your news brief.")
    
    topic_input = st.text_input("News Topic", value="climate change", help="Enter a topic to search for.")
    use_api = st.checkbox("Toggle Live NewsAPI", value=False, help="Uncheck to use sample articles (Phase A).")
    
    st.divider()
    fetch_button = st.button("🚀 Fetch News", type="primary", use_container_width=True)

# ================= MAIN CONTENT =================
if fetch_button:
    topic = topic_input.strip()
    
    if not topic:
        st.error("❌ Please enter a valid topic to fetch news.")
    else:
        st.markdown(f"### Results for: **{topic}**")
        
        # 1. Fetching News Articles
        with st.spinner(f"Fetching articles for '{topic}'..."):
            articles = fetch_articles(topic, use_api=use_api)
        
        if not articles:
            st.warning("No articles found for the given topic. Please try another one.")
        else:
            st.success(f"✅ Successfully fetched {len(articles)} articles!")
            
            # --- Display Top Articles ---
            st.subheader("🔥 Top Articles")
            
            # Layout articles in columns (max 3 wide)
            columns = st.columns(min(len(articles), 3))
            for idx, article in enumerate(articles):
                with columns[idx % 3]:
                    with st.container(border=True):
                        st.markdown(f"**{article.get('title', 'Untitled')}**")
                        st.caption(f"🗞️ Source: {article.get('source', 'Unknown')}")
                        
                        content = article.get('content', '')
                        preview = content[:300] + "..." if len(content) > 300 else content
                        
                        with st.expander("Read More"):
                            st.write(preview)

            st.divider()
            
            # 2. Processing Summaries & Morning Brief
            with st.spinner("🧠 AI is analyzing and generating the Morning Brief..."):
                # Call backend LLM agents
                summaries = summarize_all(articles)
                
                # Check for LLM / JSON failure
                if not summaries:
                    st.error("Failed to generate article summaries. The LLM may have timed out or hit limits.")
                else:
                    brief = generate_brief(summaries, topic)
                    why_it_matters = generate_why_it_matters(brief, topic)
                    
                    st.success("✅ Brief generation complete!")
                    st.divider()
                    
                    # --- Display Final Output ---
                    col1, col2 = st.columns([1.2, 2])
                    
                    # Left Column: Concise Summaries
                    with col1:
                        st.subheader("⚡ Quick Summary")
                        for s in summaries:
                            with st.container(border=True):
                                st.markdown(f"**{s.get('title', 'Headline')}**")
                                st.info(s.get('summary', ''))
                    
                    # Right Column: The Full Brief
                    with col2:
                        st.subheader("📰 Morning Brief")
                        st.markdown(
                            f"""
                            <div style="padding: 1.5rem; background-color: rgba(46, 204, 113, 0.1); border-left: 5px solid #2ecc71; border-radius: 5px;">
                                <p style="font-size: 1.1rem; line-height: 1.6;">{brief}</p>
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
                        
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.subheader("🎯 Why It Matters")
                        st.markdown(
                            f"""
                            <div style="padding: 1.5rem; background-color: rgba(231, 76, 60, 0.1); border-left: 5px solid #e74c3c; border-radius: 5px;">
                                <p style="font-size: 1.05rem; line-height: 1.6;"><b>{why_it_matters}</b></p>
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
