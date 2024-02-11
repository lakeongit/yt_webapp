import streamlit as st
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Authentication setup
CLIENT_SECRETS_FILE = "client_secrets.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def authenticate():
  flow = InstalledAppFlow.from_client_secrets_file(
      CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_local_server(port=0)
  return build('youtube', 'v3', credentials=credentials)

# Main app function
def main():
  st.title("YouTube Data Explorer")

  # Authentication
  try:
    youtube = authenticate()
  except Exception as e:
    st.error("Authentication failed: " + str(e))
    return

  # Search input
  search_term = st.text_input("Enter your search term:")

  # Search button
  if st.button("Search"):
    if search_term:
      # Build the search query
      request = youtube.search().list(
          part="snippet",
          maxResults=10,
          q=search_term
      )

      # Execute the search
      response = request.execute()

      # Display results
      for item in response['items']:
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        thumbnail = item['snippet']['thumbnails']['default']['url']

        st.write(f"<a href='https://www.youtube.com/watch?v={video_id}'>{title}</a>")
        st.image(thumbnail)

if __name__ == "__main__":
  main()
