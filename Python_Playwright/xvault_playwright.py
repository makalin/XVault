import tweepy
from playwright.sync_api import sync_playwright
import os
import argparse
from datetime import datetime

# Function to authenticate with X API
def authenticate_twitter(api_key, api_secret, access_token, access_token_secret):
    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        return client
    except Exception as e:
        print(f"Error authenticating with X API: {e}")
        return None

# Function to fetch tweets and take screenshots
def archive_tweets(client, query, max_results, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        tweets = client.search_recent_tweets(
            query=query,
            max_results=max_results,
            tweet_fields=["created_at", "author_id"]
        )
        if not tweets.data:
            print("No tweets found for the query.")
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
                    print(f"Saved screenshot: {filename}")
                except Exception as e:
                    print(f"Failed to screenshot {tweet_url}: {e}")
            browser.close()

    except Exception as e:
        print(f"Error fetching tweets: {e}")

# Main execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="XVault: Archive tweets as screenshots using Playwright.")
    parser.add_argument("--query", default="Turkey protests 2025 -filter:retweets", help="Search query for tweets")
    parser.add_argument("--max-results", type=int, default=10, help="Max number of tweets to archive")
    parser.add_argument("--output-dir", default="screenshots", help="Directory to save screenshots")
    parser.add_argument("--api-key", required=True, help="X API Key")
    parser.add_argument("--api-secret", required=True, help="X API Secret")
    parser.add_argument("--access-token", required=True, help="X Access Token")
    parser.add_argument("--access-secret", required=True, help="X Access Token Secret")

    args = parser.parse_args()

    # Authenticate
    client = authenticate_twitter(args.api_key, args.api_secret, args.access_token, args.access_secret)
    if client:
        # Archive tweets
        archive_tweets(client, args.query, args.max_results, args.output_dir)