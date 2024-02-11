# yt_webapp
This code imports necessary libraries for authentication, YouTube API access, and Streamlit UI.
It defines authentication functions using google-auth libraries and a client_secrets.json file containing your Google Cloud project credentials.
The main function displays a title, handles authentication, and takes a search term input.
When the "Search" button is clicked, a YouTube API search is executed using the search term.
The search results are displayed with titles, thumbnails, and links to the videos.
Deployment to Google Cloud Run:

Create a Google Cloud project and enable billing.
Set up a service account with the YouTube Data API v3 enabled.
Download the service account key file and rename it to client_secrets.json.
Build a container image with your dependencies and app code (e.g., using Docker).
Deploy the container image to Google Cloud Run with appropriate configuration.
Further enhancements:

Add more details to search results (e.g., channel name, publish date).
Implement pagination for longer search results.
Allow filtering by search parameters (e.g., video duration, channel ID).
Remember to modify and adapt this code to your specific needs and Google Cloud setup. For detailed deployment instructions, refer to Google Cloud Run documentation.
