import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTextEdit
from PyQt5.QtCore import Qt
from playwright.sync_api import sync_playwright
import tweepy
from datetime import datetime

class XVaultApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layout
        layout = QVBoxLayout()

        # API Credentials Inputs
        self.api_key_input = QLineEdit(self)
        self.api_key_input.setPlaceholderText("X API Key")
        layout.addWidget(QLabel("X API Key:"))
        layout.addWidget(self.api_key_input)

        self.api_secret_input = QLineEdit(self)
        self.api_secret_input.setPlaceholderText("X API Secret")
        layout.addWidget(QLabel("X API Secret:"))
        layout.addWidget(self.api_secret_input)

        self.access_token_input = QLineEdit(self)
        self.access_token_input.setPlaceholderText("X Access Token")
        layout.addWidget(QLabel("X Access Token:"))
        layout.addWidget(self.access_token_input)

        self.access_secret_input = QLineEdit(self)
        self.access_secret_input.setPlaceholderText("X Access Token Secret")
        layout.addWidget(QLabel("X Access Token Secret:"))
        layout.addWidget(self.access_secret_input)

        # Query Input
        self.query_input = QLineEdit(self)
        self.query_input.setPlaceholderText("e.g., Turkey protests 2025 -filter:retweets")
        layout.addWidget(QLabel("Search Query:"))
        layout.addWidget(self.query_input)

        # Max Results Input
        self.max_results_input = QLineEdit(self)
        self.max_results_input.setText("10")
        layout.addWidget(QLabel("Max Results:"))
        layout.addWidget(self.max_results_input)

        # Output Directory Input
        self.output_dir_input = QLineEdit(self)
        self.output_dir_input.setText("screenshots")
        layout.addWidget(QLabel("Output Directory:"))
        layout.addWidget(self.output_dir_input)

        # Archive Button
        self.archive_button = QPushButton("Archive Tweets", self)
        self.archive_button.clicked.connect(self.archive_tweets)
        layout.addWidget(self.archive_button)

        # Log Output
        self.log = QTextEdit(self)
        self.log.setReadOnly(True)
        layout.addWidget(QLabel("Log:"))
        layout.addWidget(self.log)

        # Window Setup
        self.setLayout(layout)
        self.setWindowTitle("XVault - Tweet Archiver")
        self.setGeometry(100, 100, 400, 600)

    def log_message(self, message):
        self.log.append(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

    def authenticate_twitter(self):
        try:
            client = tweepy.Client(
                consumer_key=self.api_key_input.text(),
                consumer_secret=self.api_secret_input.text(),
                access_token=self.access_token_input.text(),
                access_token_secret=self.access_secret_input.text()
            )
            return client
        except Exception as e:
            self.log_message(f"Authentication failed: {e}")
            return None

    def archive_tweets(self):
        client = self.authenticate_twitter()
        if not client:
            return

        query = self.query_input.text() or "Turkey protests 2025 -filter:retweets"
        try:
            max_results = int(self.max_results_input.text())
        except ValueError:
            max_results = 10
            self.log_message("Invalid max results, defaulting to 10.")

        output_dir = self.output_dir_input.text() or "screenshots"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        self.log_message(f"Starting archive for query: '{query}'")
        try:
            tweets = client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=["created_at", "author_id"]
            )
            if not tweets.data:
                self.log_message("No tweets found.")
                return

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                for tweet in tweets.data:
                    tweet_url = f"https://twitter.com/user/status/{tweet.id}"
                    try:
                        page.goto(tweet_url, wait_until="networkidle")
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        filename = f"{output_dir}/tweet_{tweet.id}_{timestamp}.png"
                        page.screenshot(path=filename, full_page=True)
                        self.log_message(f"Saved: {filename}")
                    except Exception as e:
                        self.log_message(f"Failed to screenshot {tweet_url}: {e}")
                browser.close()
            self.log_message("Archiving complete.")
        except Exception as e:
            self.log_message(f"Error fetching tweets: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = XVaultApp()
    window.show()
    sys.exit(app.exec_())