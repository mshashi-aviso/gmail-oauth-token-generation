from __future__ import print_function
import pickle
import os.path
import json
import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


'''
Copy the content of the credentials.json file here
'''
# CLIENT_CONFIG = {"installed": {"client_id": "blah blah", ...... }}
CLIENT_CONFIG = '' #TODO placeholder

# Add the additional scopes here if required
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.metadata',
          'https://www.googleapis.com/auth/gmail.modify']


def main():
    """
    Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(
                CLIENT_CONFIG, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # creds_to_save = {}
    # print(creds_to_save.update(CLIENT_CONFIG['installed']))
    # creds_to_save = creds_to_save.update(CLIENT_CONFIG['installed']).update(creds.to_json())

    print("''''''''''''''''''''''''''''''''''''''''''''''")
    # print(CLIENT_CONFIG['installed'])
    # print(creds.to_json())
    pprint.pprint({ **CLIENT_CONFIG['installed'], **json.loads(creds.to_json()), **{'delete_emails': False}})
    print("''''''''''''''''''''''''''''''''''''''''''''''")

    service = build('gmail', 'v1', credentials=creds)

    '''
    Uncomment the below code to check if it is working or not
    '''

    # Call the Gmail API
    # results = service.users().messages().list(userId='me').execute()
    # message_label = results['messages'][0]

    # if not message_label:
    #     print('No labels found.')
    # else:
    #     message_headers = service.users().messages().get(userId='me',id=message_label['id'], format='metadata').execute()
    #     print('Message Label:', message_label)
    #     print('Message Headers: ', message_headers)


if __name__ == '__main__':
    main()


'''
Above program will generate the credentials data and print it on the console, copy those and use in the main program. 
Save it to the desired place according to the application usage
'''