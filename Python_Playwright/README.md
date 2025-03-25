# XVault - Python_Playwright

This subfolder contains the Python + Playwright implementation of **XVault**, a tool to archive X (Twitter) tweets as screenshots. It leverages the X API via Tweepy to fetch tweets and Playwright to capture full-page screenshots, preserving the visual context of posts.

## Features
- Fetch recent tweets based on a search query (e.g., "Turkey protests 2025").
- Save screenshots of each tweet in PNG format with timestamps.
- Command-line interface for easy customization.
- Handles errors gracefully for robust archiving.

## Prerequisites
- Python 3.8 or higher
- X Developer account with API credentials (Free tier works for small-scale use)
- Installed dependencies (see Setup)

## Setup
1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/makalin/XVault.git
   cd XVault/Python_Playwright
   ```
2. **Install dependencies**:
   ```bash
   pip install tweepy playwright
   playwright install  # Installs browser binaries for Playwright
   ```
3. **Get X API credentials**:
   - Sign up at [developer.x.com](https://developer.x.com).
   - Create an app and note your API Key, API Secret, Access Token, and Access Token Secret.

## Usage
Run the script with your API credentials and optional parameters:

```bash
python xvault_playwright.py \
  --api-key "YOUR_API_KEY" \
  --api-secret "YOUR_API_SECRET" \
  --access-token "YOUR_ACCESS_TOKEN" \
  --access-secret "YOUR_ACCESS_TOKEN_SECRET" \
  --query "Turkey protests 2025 -filter:retweets" \
  --max-results 10 \
  --output-dir "screenshots"
```

- `--query`: Search term for tweets (default: "Turkey protests 2025 -filter:retweets").
- `--max-results`: Number of tweets to fetch (default: 10, limited by API tier).
- `--output-dir`: Folder to save screenshots (default: "screenshots").

Screenshots will be saved as `tweet_<tweet_id>_<timestamp>.png` in the specified directory.

## Example
To archive 5 tweets about the 2025 Turkey protests:
```bash
python xvault_playwright.py \
  --api-key "abc123" \
  --api-secret "def456" \
  --access-token "ghi789" \
  --access-secret "jkl012" \
  --query "Imamoglu arrest protest" \
  --max-results 5
```

## Notes
- **API Limits**: The Free tier allows 500 tweets/month; upgrade to Basic ($100/month) for more.
- **Headless Mode**: Runs in the background; set `headless=False` in the code to see the browser.
- **Error Handling**: Skips failed screenshots and logs issues to the console.
- **Compliance**: Use for personal archiving only, per X’s Terms of Service.

## Troubleshooting
- **Authentication Errors**: Double-check API credentials.
- **Playwright Fails**: Ensure `playwright install` ran successfully.
- **No Tweets Found**: Adjust the query or check API quota.

## Future Improvements
- Add support for tweet threads.
- Integrate cloud storage (e.g., Google Drive).
- Include metadata (e.g., tweet text) in a separate file.

## License
MIT License—see the main [XVault LICENSE](../LICENSE) file.