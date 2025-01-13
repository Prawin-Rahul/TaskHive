# Script to generate token.json

from google_auth_oauthlib.flow import InstalledAppFlow
import os

# Define the Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Path to your credentials.json file downloaded from Google Cloud Console
# will always be constant , based APP setting we gave
CREDENTIALS_FILE = '/home/prawin/Downloads/client_secret.json'

def main():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)

    # Save the token for future use
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
    print("Token saved to token.json")

if __name__ == '__main__':
    main()
