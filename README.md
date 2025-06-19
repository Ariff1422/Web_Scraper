AI Web Scraper
This project is an AI-powered web scraper designed to extract and parse specific information from websites. It leverages a combination of traditional web scraping techniques with the advanced capabilities of generative AI to intelligently identify and structure data from web pages.

Tech Stack
The following Python libraries and tools are used in this project:

selenium: For automating web browser interactions, allowing the scraper to navigate web pages, execute JavaScript, and handle dynamic content. This is essential for scraping modern websites.

beautifulsoup4: A powerful library for parsing HTML and XML documents. It helps in navigating, searching, and modifying the parse tree, making it easy to extract content.

google-generativeai: Integrates the Google Gemini API, enabling the application to use large language models for intelligent parsing and extraction of data based on natural language descriptions.

python-dotenv: Used for loading environment variables from a .env file, securely managing API keys (like your Google API Key) and other configurations.

streamlit: A fantastic framework for building interactive web applications directly in Python. It provides the user interface for entering URLs, parsing descriptions, and downloading results.

pandas: A fundamental library for data manipulation and analysis. It's used to convert the structured data extracted by the AI into a DataFrame, which can then be easily exported to CSV format.

What it Can Do
This AI Web Scraper offers the following functionalities:

Web Scraping: Navigates to a specified URL and fetches the full HTML content of the page, including content loaded dynamically by JavaScript.

DOM Content Extraction & Cleaning: Extracts the main body content from the HTML and cleans it by removing script and style tags, providing a clean text representation of the visible page content.

AI-Powered Information Parsing: Utilizes the Google Gemini large language model to intelligently parse and extract specific information from the scraped and cleaned DOM content based on a natural language description provided by the user. This allows for flexible and intelligent data extraction without needing to write specific parsing rules for each website.

Structured Data Output: The extracted information is returned in a structured JSON format (list of dictionaries), making it easy to work with.

CSV Download: Allows users to download the parsed and structured data as a CSV file, facilitating further analysis or use in other applications.

Inspiration & Future Plans
This project was initially inspired by tutorials from Tech with Tim, providing a solid foundation in web scraping and basic automation.

Looking ahead, I aim to significantly enhance this web scraper's capabilities to tackle more complex real-world scenarios. Future improvements will focus on:

Bypassing CAPTCHAs: Implementing strategies to handle various CAPTCHA challenges (e.g., reCAPTCHA, hCaptcha) to access protected content.

Managing Rate Limiting: Developing robust mechanisms to respect website rate limits and avoid IP bans, ensuring ethical and sustainable scraping practices.

Handling Anti-Bot Measures: Improving the scraper's resilience against more sophisticated anti-bot detection techniques.

Expanding AI Parsing Capabilities: Fine-tuning the AI model for even more accurate and nuanced data extraction from diverse and unstructured web content.

Installation Guide
To get this project up and running on your local machine, follow these steps:

1. Clone the Repository
First, clone this repository to your local machine:

git clone https://github.com/Ariff1422/Web_Scraper.git
cd Web_Scraper

2. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

For venv (Python's built-in virtual environment):

# Create the virtual environment
python -m venv venv

# Activate the virtual environment (Windows Command Prompt)
.\venv\Scripts\activate.bat

# Activate the virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate the virtual environment (Git Bash / WSL)
source venv/bin/activate

For conda (if you use Anaconda/Miniconda):

# Create a new conda environment
conda create --name web_scraper_env python=3.9 # Or your preferred Python version

# Activate the conda environment
conda activate web_scraper_env

3. Install Dependencies
Once your virtual environment is active, install the required Python packages using the requirements.txt file:

pip install -r requirements.txt

4. Download ChromeDriver
Selenium requires a WebDriver executable to interact with web browsers. This project is configured to use ChromeDriver.

Download ChromeDriver: Visit the official ChromeDriver download page: https://chromedriver.chromium.org/downloads

Match Chrome Version: Download the ChromeDriver version that exactly matches your installed Google Chrome browser version. You can check your Chrome version by going to chrome://version in your browser.

Place ChromeDriver: Place the downloaded chromedriver.exe (or chromedriver on Linux/macOS) file directly into your project's root directory (the same directory where scraper.py is located).

5. Set up Google Gemini API Key
The project uses the Google Gemini API for parsing. You need to set up your API key:

Get an API Key: If you don't have one, obtain a Google Gemini API key from the Google AI Studio.

Create .env file: In the root directory of your project, create a new file named .env (note the leading dot).

Add your API Key: Add the following line to your .env file, replacing YOUR_GEMINI_API_KEY with your actual key:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

Important: Do not share your .env file or commit it to version control.

6. Run the Streamlit Application
Finally, you can run the Streamlit web application:

streamlit run your_main_app_file.py

(Replace your_main_app_file.py with the actual name of your Streamlit application file, e.g., app.py or main.py).

Your web browser should automatically open to the Streamlit application.
