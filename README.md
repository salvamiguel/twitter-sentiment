# TweetSentiment

Analyze tweets' text sentimental data for specific hashtags, keywords or time ranges with a simple Excel Workbook. This project is intended for non-technical researchers, please keep that on mind.

> Note: This project uses Twitter API via [tweepy](https://github.com/tweepy/tweepy) module and **requires the usage of [Academic Research product track](https://developer.twitter.com/en/products/twitter-api/academic-research) valid bearer token**. Otherwise, you will get 403 Forbiden error responses from tweepy.

## Usage

Before going strait to the steps for using this script, please take note of the system requirements. You can download [python for Windows here](https://www.python.org/downloads/windows/), [python for macOS here](https://www.python.org/downloads/macos/)
and [python for Linux here](https://www.python.org/downloads/source/).

### Requirements

These are the system requirements:

-   `python >=3.6`
-   `git`

### Installing dependencies and script

Once we have installed `python` we must install all the dependecies needed. Please find your computers shell or command promt (cmd for Windows, terminal for macOS/Linux) and open a new window, then type:

`git clone https://github.com/salvamiguel/tweet-sentiment.git`

This will clone this repository on your machine. Navigate on your terminal to `tweet-sentiment` folder. Install dependencies with the following command:

`pip3 install -r requirements.txt`

### Prepare input workbook

Inside of `tweet-sentiment` folder there is a `example_input.xlsx` document, you can use this file as template for inserting your queries. After adding your queries save this document as `input.xlsx` in the same folder.

### Running analysis

UNDER DEVELOPMENT

### Getting results

If everything went smooth, your results will be in a `output.xlsx` document.