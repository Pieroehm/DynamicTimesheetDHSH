import imaplib
import email
from bs4 import BeautifulSoup
import os
from credentials import EUSERNAME,EPASSWORD

# Your Gmail credentials
EMAIL = EUSERNAME
PASSWORD = EPASSWORD

# Connect to mail and select the inbox
mail = imaplib.IMAP4_SSL('imap.gmx.net')
mail.login(EMAIL, PASSWORD)
mail.select('inbox')

# Search for all emails
status, email_ids = mail.search(None, 'ALL')
email_ids = email_ids[0].split()

# Directory to save attachments
SAVE_PATH = 'C:/Users/paulp/Downloads/Test'
DESIRED_NAME ='WAK-Termine.ics'

for e_id in email_ids:
    # Fetch the email by ID
    status, email_data = mail.fetch(e_id, '(RFC822)')
    raw_email = email_data[0][1]

    # Convert the raw email to an email object
    msg = email.message_from_bytes(raw_email)

    # Check if the email message is multipart
    if msg.is_multipart():
        # Loop through each part
        for part in msg.walk():
            content_disposition = str(part.get("Content-Disposition"))
            # Check if the part contains an attachment
            if "attachment" in content_disposition:
                # Download the attachment only if the filename matches the desired name
                file_name = part.get_filename()
                if file_name == DESIRED_NAME:
                    file_path = os.path.join(SAVE_PATH, file_name)
                    with open(file_path, 'wb') as f:
                        f.write(part.get_payload(decode=True))
# Logout and close the connection
mail.logout()
