import streamlit as st
import pandas as pd
import numpy as np
import pickle 
from sklearn.metrics.pairwise import cosine_similarity
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

# Configure page
st.set_page_config(page_title="Music Recommender", layout="wide")

# Load data and models with caching
@st.cache_data
def load_data():
    """Load songs dataframe"""
    return pd.read_csv("songs.csv")

@st.cache_resource
def load_models():
    """Load vectorizer and processor"""
    vectorize = pickle.load(open('vectors.pkl', 'rb'))
    processor = pickle.load(open('process.pkl', 'rb'))
    return vectorize, processor

@st.cache_resource
def init_spotify():
    """Initialize Spotify client with credentials from environment variables"""
    # Use environment variables for security
    client_id = os.getenv('SPOTIFY_CLIENT_ID', 'd2497d19fefb42f6b6792ee2f3471172')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET', '3000a8d3cf1d49769e0d8455027c5343')
    
    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
    return spotipy.Spotify(auth_manager=auth_manager)

# Load resources
songs = load_data()
vectorize, processor = load_models()
sp = init_spotify()

def get_track_info(track_id):
    """Fetch both poster and artist in a single API call"""
    try:
        track = sp.track(track_id)
        poster = track['album']['images'][0]['url'] if track['album']['images'] else None
        artist = track['artists'][0]['name'] if track['artists'] else "Unknown"
        return poster, artist
    except Exception as e:
        st.warning(f"Could not fetch track info: {e}")
        return None, "Unknown"

def recommend_songs(song_name, top_n=5):
    """Generate song recommendations based on input song"""
    try:
        # Get song index
        song_indices = songs[songs["name"] == song_name].index
        if len(song_indices) == 0:
            st.error(f"Song '{song_name}' not found in database")
            return None
        
        index = song_indices[0]
        
        # Transform and calculate similarity
        song_input = songs[songs["name"] == song_name]
        transformed_input = processor.transform(song_input)
        similarity = cosine_similarity(vectorize, transformed_input)
        
        # Get top recommendations (excluding the input song itself)
        top_indices = sorted(
            list(enumerate(similarity.flatten())), 
            reverse=True, 
            key=lambda x: x[1]
        )[1:top_n+1]
        
        # Collect recommendation data
        recommendations = []
        for idx, score in top_indices:
            track_id = songs.iloc[idx, 3]
            poster, artist = get_track_info(track_id)
            recommendations.append({
                'name': songs.iloc[idx, 2],
                'track_id': track_id,
                'poster': poster,
                'artist': artist,
                'score': score
            })
        
        return recommendations
        
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
        return None

def display_recommendations(recommendations):
    """Display recommendations in a grid layout"""
    if not recommendations:
        return
    
    # Display in rows of 3
    for i in range(0, len(recommendations), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(recommendations):
                rec = recommendations[i + j]
                with col:
                    st.markdown(f"**{rec['name']}**")
                    st.caption(f"🎤 {rec['artist']}")
                    if rec['poster']:
                        st.image(rec['poster'], use_container_width=True)
                    else:
                        st.info("No cover art available")

# Main UI
st.title("🎵 Music Recommender System")
st.markdown("Select a song and get personalized recommendations based on audio features")

# Song selection
song_list = songs["name"].unique()
selected_song = st.selectbox(
    'Select a song:', 
    song_list,
    help="Choose a song to get similar recommendations"
)

# Recommendation button
if st.button("🎯 Get Recommendations", type="primary"):
    with st.spinner("Finding similar songs..."):
        recommendations = recommend_songs(selected_song)
        
        if recommendations:
            st.success(f"Top 5 recommendations for **{selected_song}**")
            display_recommendations(recommendations)
            
            # Optional: Show similarity scores
            # with st.expander("View similarity scores"):
            #     for i, rec in enumerate(recommendations, 1):
            #         st.write(f"{i}. {rec['name']} - Similarity: {rec['score']:.4f}")
