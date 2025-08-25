"""
Module: email_ingest.py
Description: Fetch emails and download attachments for OCS automation system.
Best practices: Use environment variables for credentials, add logging, handle errors gracefully.
"""
import imaplib
import email
import os
import logging
from typing import Optional

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

class EmailIngestor:
    def __init__(self, username: str, password: str, imap_server: str = 'imap.gmail.com', folder: str = 'INBOX', save_dir: str = 'data/'):
        self.username = username
        self.password = password
        self.imap_server = imap_server
        self.folder = folder
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)

    def fetch_emails(self):
        try:
            mail = imaplib.IMAP4_SSL(self.imap_server)
            mail.login(self.username, self.password)
            mail.select(self.folder)
            typ, data = mail.search(None, 'ALL')
            for num in data[0].split():
                typ, msg_data = mail.fetch(num, '(RFC822)')
                msg = email.message_from_bytes(msg_data[0][1])
                self._save_attachments(msg)
            mail.logout()
            logging.info('Email fetching completed.')
        except Exception as e:
            logging.error(f'Error fetching emails: {e}')

    def _save_attachments(self, msg):
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            if filename:
                filepath = os.path.join(self.save_dir, filename)
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                logging.info(f'Attachment saved: {filepath}')

if __name__ == "__main__":
    # Example usage (replace with environment variables in production)
    USERNAME = os.getenv('OCS_EMAIL_USER', 'your_email@gmail.com')
    PASSWORD = os.getenv('OCS_EMAIL_PASS', 'your_password')
    ingestor = EmailIngestor(USERNAME, PASSWORD)
    ingestor.fetch_emails()
