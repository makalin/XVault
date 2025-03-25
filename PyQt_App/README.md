# XVault - PyQt_App

This subfolder contains the PyQt5 desktop application implementation of **XVault**, a tool to archive X (Twitter) tweets as screenshots. It integrates the X API (via Tweepy) and Playwright for screenshot capture, offering a graphical user interface (GUI) for ease of use.

## Features
- User-friendly GUI to input API credentials, search query, and settings.
- Fetch and screenshot recent tweets based on a query (e.g., "Turkey protests 2025").
- Save full-page screenshots as PNGs with tweet IDs and timestamps.
- Real-time log display for feedback on the archiving process.

## Prerequisites
- Python 3.8 or higher
- X Developer account with API credentials (Free tier works for small-scale use)
- Installed dependencies (see Setup)

## Setup
1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/makalin/XVault.git
   cd XVault/PyQt_App
   ```
2. **Install dependencies**:
   ```bash
   pip install pyqt5 tweepy playwright
   playwright install  # Installs browser binaries for Playwright
   ```
3. **Get X API credentials**:
   - Sign up at [developer.x.com](https://developer.x.com).
   - Create an app and note your API Key, API Secret, Access Token, and Access Token Secret.

## Usage
1. Run the application:
   ```bash
   python xvault_pyqt.py
   ```
2. In the GUI:
   - Enter your X API Key, API Secret, Access Token, and Access Token Secret.
   - Input a search query (e.g., "Turkey protests 2025 -filter:retweets") or leave blank for default.
   - Set the max number of tweets (default: 10).
   - Specify an output directory (default: "screenshots").
   - Click "Archive Tweets" to start the process.
3. Check the log for progress and the output directory for screenshots (e.g., `tweet_123456789_20250324_123456.png`).

## Notes
- **API Limits**: Free tier allows 500 tweets/month; upgrade to Basic ($100/month) for more.
- **Headless Mode**: Screenshots run in the background; edit `headless=False` in the code to debug visually.
- **Error Handling**: Logs issues in the GUI; invalid inputs revert to defaults.
- **Compliance**: Use for personal archiving only, per X’s Terms of Service.

## Troubleshooting
- **GUI Doesn’t Open**: Ensure PyQt5 is installed (`pip install pyqt5`).
- **Authentication Errors**: Verify API credentials are correct.
- **No Screenshots**: Check Playwright installation (`playwright install`) and query validity.

## Future Improvements
- Add a file picker for output directory.
- Save tweet metadata in a JSON file alongside screenshots.
- Support batch processing of multiple queries.

## License
MIT License—see the main [XVault LICENSE](../LICENSE) file.