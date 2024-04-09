# Data Entry Job Automator

## Project Overview
This script automates the process of data entry for property listings to a Google Spreadsheet. It starts by scraping property details from a clone of Zillow's listing page using Beautiful Soup, then uses Selenium WebDriver to automate the submission of these details into a Google Form.

## Output


https://github.com/sarvesh-2109/Data-Entry-Job-Automator/assets/113255836/38fcd182-bcdd-4bdd-9938-7ca189db792b



## Features
- **Scraping Property Details:** Fetches property addresses, prices, and individual listing URLs from a specified webpage.
- **Automated Form Submission:** Automates the process of entering the scraped property details into a Google Form and submitting them.

## Technologies Used
- **Python:** The core programming language used for the script.
- **Beautiful Soup:** A Python library for pulling data out of HTML and XML files. Used here to scrape property listing information.
- **Selenium WebDriver:** Provides a programmable interface to control web browsers and automate web interactions, used here to fill and submit the Google Form.

## How It Works
1. **Scrape Property Details:** The script first makes a GET request to the specified property listing page and scrapes details including addresses, prices, and URLs of individual listings.
2. **Submit to Google Form:** It then iterates through the list of scraped properties, opens the Google Form for each property, fills in the details, and submits the form.

## Requirements
- Python
- Selenium (`pip install selenium`)
- Beautiful Soup 4 (`pip install beautifulsoup4`)
- WebDriver for the browser you intend to use (e.g., ChromeDriver for Google Chrome)

## Usage
1. Ensure all requirements are installed and the WebDriver executable is placed in a directory accessible by the system PATH.
2. Update the Google Form URLs and the XPaths for form fields in the script as needed to match your form.
3. Run the script: `python main.py`

## Note
- The script is intended for educational and demonstration purposes. Always ensure you have permission to scrape data from a website and submit it to a Google Form.
- Modify the `all_links`, `all_addresses`, and `all_prices` selectors based on the structure of the webpage you are scraping.
- The Google Form URL and the XPaths for input fields and the submit button may need to be updated if the form's structure changes.

