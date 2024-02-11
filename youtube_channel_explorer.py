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
  st.title("YouTube Channel Explorer")

  try:
    youtube = authenticate()
  except Exception as e:
    st.error("Authentication failed: " + str(e))
    return

  search_term = st.text_input("Enter your search term:")

  if st.button("Search"):
    if search_term:
      request = youtube.search().list(
          part="snippet",
          type="channel",
          maxResults=10,
          q=search_term
      )
      response = request.execute()

      st.header("Search Results")
      for item in response['items']:
        channel_id = item['snippet']['channelId']
        channel_title = item['snippet']['title']
        channel_description = item['snippet']['description']

        st.write(f"**Channel:** {channel_title}")
        st.write(f"**Description:** {channel_description}")
        st.markdown(f"[Visit Channel]({'https://www.youtube.com/channel/' + channel_id})")
        st.write("---")

if __name__ == "__main__":
  main()
