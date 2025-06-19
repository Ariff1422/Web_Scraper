# 🕸️ AI Web Scraper

An AI-powered web scraper that intelligently extracts and parses specific information from websites using the power of generative AI. It combines traditional scraping tools with LLMs to flexibly structure unstructured web content.

## 🛠 Tech Stack

- **Selenium**: Automates browser interactions, handling dynamic JavaScript-rendered content.
- **BeautifulSoup4**: Parses HTML/XML for clean and efficient content extraction.
- **Google Generative AI (`google-generativeai`)**: Integrates Google Gemini LLM to enable intelligent parsing based on natural language prompts.
- **python-dotenv**: Manages environment variables and API keys securely.
- **Streamlit**: Builds the interactive web UI for users to input URLs, parsing criteria, and download results.
- **Pandas**: Structures parsed data as a `DataFrame`, allowing for easy CSV export.

---

## 🚀 Features

- **🌐 Web Scraping**: Navigate to any URL, including dynamic content via JavaScript.
- **🧹 DOM Extraction & Cleaning**: Strips away script/style tags to provide clean text content.
- **🧠 AI-Powered Parsing**: Gemini LLM intelligently extracts specific info based on your natural language description.
- **📦 Structured JSON Output**: Data returned as a list of dictionaries.
- **📥 CSV Export**: Download parsed data in `.csv` format for analysis.

---

## 💡 Inspiration & Future Roadmap

Inspired by [Tech With Tim's](https://www.youtube.com/@TechWithTim) tutorials on web scraping and automation. Planned improvements:

- ⚙️ **CAPTCHA Bypass**: Handle reCAPTCHA, hCaptcha, etc.
- 📉 **Rate Limiting Compliance**: Respect site scraping limits and prevent bans.
- 🤖 **Anti-Bot Evasion**: Improve stealth against bot detection systems.
- 🧬 **LLM Fine-Tuning**: Make parsing more robust across diverse websites.

---

## 🧪 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/Ariff1422/Web_Scraper.git
cd Web_Scraper/v1
````

### 2. Set Up a Virtual Environment

Using `venv`:

```bash
python -m venv venv
# Windows CMD
.\venv\Scripts\activate.bat
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Git Bash / WSL / macOS/Linux
source venv/bin/activate
```

Using `conda`:

```bash
conda create --name web_scraper_env python=3.9
conda activate web_scraper_env
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up ChromeDriver

1. [Download ChromeDriver](https://chromedriver.chromium.org/downloads) that matches your local Chrome version.
2. Place the `chromedriver.exe` (Windows) or `chromedriver` (macOS/Linux) in your project root directory.

### 5. Configure Google Gemini API Key

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app).
2. Create a `.env` file in the root directory and add:

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

> ⚠️ Do not share or commit your `.env` file to version control.

### 6. Run the Streamlit App

```bash
streamlit run main.py
```
---

## 📄 License

This project is for educational and personal use. Please ensure your scraping activity complies with each website’s terms of service.

---

## 🙌 Acknowledgements

Special thanks to **Tech with Tim** for the original scraping inspiration.
