# XVault - Node_Puppeteer

This subfolder contains the Node.js + Puppeteer implementation of **XVault**, a tool to archive X (Twitter) tweets as screenshots. It uses the X API (via `twitter-api-v2`) to fetch tweets and Puppeteer to capture full-page screenshots in a headless browser, ideal for automated batch archiving.

## Features
- Fetch recent tweets based on a search query (e.g., "Turkey protests 2025").
- Save full-page screenshots as PNGs with tweet IDs and timestamps.
- Command-line interface for flexible configuration.
- Robust error handling for reliable operation.

## Prerequisites
- Node.js 16.x or higher
- X Developer account with API credentials (Free tier works for small-scale use)

## Setup
1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/makalin/XVault.git
   cd XVault/Node_Puppeteer
   ```
2. **Install dependencies**:
   ```bash
   npm install
   ```
   This installs `puppeteer`, `twitter-api-v2`, and `yargs`.
3. **Get X API credentials**:
   - Sign up at [developer.x.com](https://developer.x.com).
   - Create an app and note your API Key, API Secret, Access Token, and Access Token Secret.

## Usage
Run the script with your API credentials and optional parameters:

```bash
node xvault_puppeteer.js \
  --api-key "YOUR_API_KEY" \
  --api-secret "YOUR_API_SECRET" \
  --access-token "YOUR_ACCESS_TOKEN" \
  --access-secret "YOUR_ACCESS_TOKEN_SECRET" \
  --query "Turkey protests 2025 -filter:retweets" \
  --max-results 10 \
  --output-dir "screenshots"
```

- `--query` (or `-q`): Search term for tweets (default: "Turkey protests 2025 -filter:retweets").
- `--max-results` (or `-m`): Number of tweets to fetch (default: 10, limited by API tier).
- `--output-dir` (or `-o`): Folder to save screenshots (default: "screenshots").

Screenshots will be saved as `tweet_<tweet_id>_<timestamp>.png` in the specified directory.

## Example
To archive 5 tweets about the 2025 Turkey protests:
```bash
node xvault_puppeteer.js \
  --api-key "abc123" \
  --api-secret "def456" \
  --access-token "ghi789" \
  --access-secret "jkl012" \
  --query "Imamoglu arrest protest" \
  --max-results 5
```

## Notes
- **API Limits**: Free tier allows 500 tweets/month; upgrade to Basic ($100/month) for more.
- **Headless Mode**: Runs silently; set `headless: false` in the code to debug visually.
- **Error Handling**: Skips failed screenshots and logs errors to the console.
- **Compliance**: Use for personal archiving only, per X’s Terms of Service.

## Troubleshooting
- **Authentication Errors**: Verify API credentials are correct.
- **Puppeteer Fails**: Ensure Node.js is updated and retry `npm install`.
- **No Tweets Found**: Adjust query or check API quota.

## Future Improvements
- Add support for saving tweet metadata alongside screenshots.
- Implement rate limiting to handle larger batches.
- Integrate with cloud storage (e.g., AWS S3).

## License
MIT License—see the main [XVault LICENSE](../LICENSE) file.
