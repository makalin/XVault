# XVault - Browser_Extension

This subfolder contains the browser extension implementation of **XVault**, a tool to manually save screenshots of X (Twitter) tweets directly from your browser. It works on Chrome and Firefox, using `html2canvas` to capture the tweet’s visual content as seen on the page.

## Features
- One-click screenshot of the visible tweet on an X page.
- Saves PNG images with tweet ID and timestamp in the filename.
- Simple popup interface accessible from the browser toolbar.
- No API required—works entirely client-side.

## Prerequisites
- Google Chrome or Mozilla Firefox browser.
- Basic understanding of how to load browser extensions.

## Setup
1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/makalin/XVault.git
   cd XVault/Browser_Extension
   ```
2. **Download html2canvas**:
   - Place `html2canvas.min.js` in this folder (get it from [html2canvas.hertzen.com](https://html2canvas.hertzen.com/dist/html2canvas.min.js)).
   - Or use a CDN link in `popup.html` (see code comments).
3. **Add icons**:
   - Include `icon16.png`, `icon48.png`, and `icon128.png` (16x16, 48x48, 128x128 pixels) in this folder. Use placeholders from [Flaticon](https://www.flaticon.com/) if needed.
4. **Load the extension**:
   - **Chrome**:
     1. Open `chrome://extensions/`.
     2. Enable "Developer mode" (top right).
     3. Click "Load unpacked" and select the `Browser_Extension` folder.
   - **Firefox**:
     1. Open `about:debugging#/runtime/this-firefox`.
     2. Click "Load Temporary Add-on" and select `manifest.json` from this folder.

## Usage
1. Navigate to a tweet on X (e.g., `https://twitter.com/user/status/123456789`).
2. Click the XVault icon in your browser toolbar.
3. Click "Save Tweet Screenshot" in the popup.
4. The screenshot will download as `tweet_<tweet_id>_<timestamp>.png` (e.g., `tweet_123456789_1711345678901.png`).

## Notes
- **Scope**: Captures only the main tweet `article` element on the page. Threads or replies may need manual navigation.
- **Dynamic Content**: Some embedded media (e.g., videos) might not render fully in the screenshot due to `html2canvas` limitations.
- **Compliance**: For personal use only, per X’s Terms of Service.

## Troubleshooting
- **No Tweet Found**: Ensure you’re on a tweet page (URL includes `/status/`).
- **Blank Screenshot**: Check if `html2canvas.min.js` is loaded correctly.
- **Icon Missing**: Add placeholder icons or update `manifest.json` paths.

## Future Improvements
- Add support for capturing entire threads.
- Include a settings popup to customize filename or image quality.
- Enhance compatibility with dynamic X layouts.

## Credits
- Built with [html2canvas](https://html2canvas.hertzen.com/) for screenshot functionality.
- Icons (if used) from [Flaticon](https://www.flaticon.com/)—attribute as needed.

## License
MIT License—see the main [XVault LICENSE](../LICENSE) file.