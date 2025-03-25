const { TwitterApi } = require('twitter-api-v2');
const puppeteer = require('puppeteer');
const fs = require('fs').promises;
const path = require('path');
const yargs = require('yargs');

// Parse command-line arguments
const argv = yargs
    .option('query', { alias: 'q', type: 'string', default: 'Turkey protests 2025 -filter:retweets', description: 'Search query for tweets' })
    .option('max-results', { alias: 'm', type: 'number', default: 10, description: 'Max number of tweets to archive' })
    .option('output-dir', { alias: 'o', type: 'string', default: 'screenshots', description: 'Directory to save screenshots' })
    .option('api-key', { type: 'string', demandOption: true, description: 'X API Key' })
    .option('api-secret', { type: 'string', demandOption: true, description: 'X API Secret' })
    .option('access-token', { type: 'string', demandOption: true, description: 'X Access Token' })
    .option('access-secret', { type: 'string', demandOption: true, description: 'X Access Token Secret' })
    .argv;

// Initialize Twitter client
const client = new TwitterApi({
    appKey: argv['api-key'],
    appSecret: argv['api-secret'],
    accessToken: argv['access-token'],
    accessSecret: argv['access-secret'],
});

async function archiveTweets() {
    const outputDir = path.resolve(argv['output-dir']);
    try {
        // Create output directory if it doesn't exist
        await fs.mkdir(outputDir, { recursive: true });

        // Fetch tweets
        const tweets = await client.v2.search(argv.query, {
            'tweet.fields': 'created_at,author_id',
            max_results: argv['max-results'],
        });

        if (!tweets.data?.data) {
            console.log('No tweets found for the query.');
            return;
        }

        // Launch Puppeteer
        const browser = await puppeteer.launch({ headless: true });
        const page = await browser.newPage();

        // Process each tweet
        for (const tweet of tweets.data.data) {
            const tweetUrl = `https://twitter.com/user/status/${tweet.id}`;
            try {
                await page.goto(tweetUrl, { waitUntil: 'networkidle2' });
                const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
                const filename = path.join(outputDir, `tweet_${tweet.id}_${timestamp}.png`);
                await page.screenshot({ path: filename, fullPage: true });
                console.log(`Saved screenshot: ${filename}`);
            } catch (error) {
                console.error(`Failed to screenshot ${tweetUrl}: ${error.message}`);
            }
        }

        await browser.close();
    } catch (error) {
        console.error(`Error during archiving: ${error.message}`);
    }
}

// Run the archiving process
archiveTweets().then(() => console.log('Archiving complete.'));