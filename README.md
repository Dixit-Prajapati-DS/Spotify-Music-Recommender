<h1>Spotify Music Recommender</h1>
<p>A music recommendation system built using the Spotify API and Streamlit.</p>

<hr>

<h2>🌟 Project Overview</h2>
<p>
This app helps you discover songs similar to a song you like. You pick a track, 
and it shows you a list of recommended songs including their cover art, artist, and name.
</p>

<hr>

<h2>🚀 Why it Matters</h2>
<ul>
  <li>Makes exploring new music easier by recommending tracks you might enjoy.</li>
  <li>Uses real-track features (via the Spotify API) to find meaningful similarity, not just random songs.</li>
  <li>Visual interface built with Streamlit makes it easy to use and share.</li>
</ul>

<hr>

<h2>🧰 How to Use</h2>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/Dixit-Prajapati-DS/Spotify-Music-Recommender.git
cd Spotify-Music-Recommender
</code></pre>

<h3>2. Install dependencies</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>3. Set up Spotify credentials</h3>
<p>
Go to <a href="https://developer.spotify.com/dashboard/" target="_blank">Spotify Developer Dashboard</a> 
and create a new app.<br>
Copy your <b>Client ID</b> and <b>Client Secret</b>.<br>
In your code (or a <code>.env</code> file) set these values so the app can authenticate.
</p>

<h3>4. Run the app</h3>
<pre><code>streamlit run app.py
</code></pre>
<p>
A browser window will typically open at <code>http://localhost:8501</code>.<br>
In the dropdown, select your base song, then click “Recommend” to see similar songs.
</p>

<hr>

<h2>🧠 How It Works (Simplified)</h2>
<ol>
  <li>You pick a song.</li>
  <li>The app uses the Spotify API to fetch audio features and metadata (artist, cover art).</li>
  <li>The system compares that song’s features with a dataset of songs to find the closest ones.</li>
  <li>The recommendations appear in your interface with cover art and details.</li>
</ol>

<hr>

<h2>🔧 What’s Inside the Repo</h2>
<ul>
  <li><b>app.py</b> – Streamlit front-end that handles user input and displays results.</li>
  <li>Recommendation logic module – computes song similarity.</li>
  <li>Utility functions – fetch album art and details using Spotify track IDs.</li>
  <li><b>requirements.txt</b> – List of Python packages required.</li>
  <li>Optional dataset or pre-computed similarity matrix.</li>
</ul>

<hr>

<h2>✅ Good To Know</h2>
<ul>
  <li>Needs an internet connection to fetch data from Spotify.</li>
  <li>Spotify API rate limits may apply for many requests.</li>
  <li>The accuracy depends on your dataset and similarity model.</li>
  <li>The UI currently shows a fixed number of recommendations (e.g., 5).</li>
</ul>

<hr>

<h2>📈 Possible Improvements</h2>
<ul>
  <li>Allow user input of playlists instead of a single song.</li>
  <li>Combine content-based and collaborative filtering for better accuracy.</li>
  <li>Cache posters and metadata to reduce API calls.</li>
  <li>Add play/preview buttons using Spotify’s embed player.</li>
  <li>Show album name, year, and genre for each song.</li>
  <li>Deploy online so anyone can access it without installing locally.</li>
</ul>
