# scrape_images
A python scraper to download large number of images from the larget image database, www.shutterstock.com

# Requirements
Python 3

# Setup
1. pip3 install bs4 selenium urllib
2. Install a version of ChromeDriver that is compatible with your Chrome version from https://chromedriver.chromium.org/downloads

# Usage Instructions
1. Go to www.shutterstock.com, enter your serch string and the filters that you need to find images to your satisfaction.
2. Copy the resulting URL in the line 45 the the variable *your_url*
3. Add the number of pages you wish to scrape according to the number of images you need in the variable below this.\\
4. Finally run the code: python3 scrape.py

Note: Update for the HTML tag updates by the website.
