import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def scraper(website):
    print("Starting scraper...")

    chrome_driver_path = "./chromedriver.exe" #defines the path to the ChromeDriver executable 
    options = webdriver.ChromeOptions() #how should the scraper behaves
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print(f"Scraping {website}...")
        html = driver.page_source
        time.sleep(20)  # Wait for the page to load completely

        return html
    finally:
        driver.quit()

def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()  # Remove script and style elements

    cleaned_content = soup.get_text(separator="\n", strip=True) #seperate text with newlines and strip leading/trailing whitespace
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())  # Remove empty lines if it is not seperating anything
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)] #I am creating the first 6000 characters and then it will step forward 6000 and then it will keep repeating the same step till we finish
