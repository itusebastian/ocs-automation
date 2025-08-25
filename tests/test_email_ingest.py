"""
Test: test_email_ingest.py
Purpose: Unit test for EmailIngestor class in email_ingest.py
Best practices: Use mock objects to avoid real email server calls.
"""
import os
import unittest
from unittest.mock import patch, MagicMock
from src.ingestion.email_ingest import EmailIngestor

class TestEmailIngestor(unittest.TestCase):
    @patch('imaplib.IMAP4_SSL')
    def test_fetch_emails(self, mock_imap):
        # Setup mock
        instance = mock_imap.return_value
        instance.login.return_value = ('OK', [b'Logged in'])
        instance.select.return_value = ('OK', [b'INBOX selected'])
        instance.search.return_value = ('OK', [b'1'])
        instance.fetch.return_value = ('OK', [(b'1', b'Raw email bytes')])
        # Patch email.message_from_bytes to return a mock message
        with patch('email.message_from_bytes') as mock_msg_from_bytes:
            mock_msg = MagicMock()
            mock_msg.walk.return_value = []  # No attachments
            mock_msg_from_bytes.return_value = mock_msg
            ingestor = EmailIngestor('user', 'pass')
            ingestor.fetch_emails()
            instance.login.assert_called_once()
            instance.logout.assert_called_once()

if __name__ == "__main__":
    unittest.main()
