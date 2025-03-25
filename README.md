# XVault

![XVault Logo](xvault_logo.png)

**XVault** is a collection of X (Twitter) archiving tools designed to capture and preserve tweets as screenshots. Whether you're documenting real-time events, like the 2025 Turkey protests following Istanbul Mayor Ekrem Imamoglu’s arrest, or building a personal archive, XVault offers flexible options to save tweet visuals—text, images, and layout intact—for future reference.

## Purpose
The goal of XVault is to provide a reliable way to archive X posts in their original form, bypassing text-only limitations of standard APIs. By saving screenshots, XVault ensures you retain the full context of tweets, making it ideal for researchers, journalists, or anyone preserving digital history.

## Features
- Capture full tweet screenshots, including media and formatting.
- Multiple implementation options to suit different skill levels and needs.
- Store archives locally or adapt for cloud integration.
- Focused on ease of use and customization.

## Subfolders
XVault includes several approaches to achieve its goal. Each subfolder contains a unique implementation—choose based on your technical preference:

- **`Python_Playwright`**: Automated screenshot tool using Python and Playwright with X API integration.
- **`Browser_Extension`**: Manual screenshot Chrome/Firefox extension for quick, browser-based captures.
- **`Node_Puppeteer`**: Node.js solution with Puppeteer for headless browser screenshots.
- **`PyQt_App`**: Desktop GUI app built with PyQt for a user-friendly archiving experience.

*Details and setup instructions for each are in their respective subfolder READMEs.*

## Getting Started
1. Clone this repository:
   ```bash
   git clone https://github.com/makalin/XVault.git
   ```
2. Navigate to the subfolder of your chosen implementation (e.g., `cd XVault/Python_Playwright`).
3. Follow the specific README in that subfolder for setup and usage instructions.

## Requirements
- An X Developer account and API credentials (for API-based options).
- Basic familiarity with the tools used in your chosen subfolder (e.g., Python, Node.js, or browser extension development).
- Compliance with X’s Terms of Service and local laws for personal archiving.

## Contributing
Feel free to fork this repo, submit pull requests, or open issues with ideas to improve XVault. Contributions to enhance functionality, add new methods, or refine existing ones are welcome!

## License
This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with inspiration from the need to preserve digital moments, like the 2025 Turkey protests.
- Thanks to open-source tools like Tweepy, Playwright, Puppeteer, and PyQt.
