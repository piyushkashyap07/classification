from selenium.webdriver.chrome.service import Service
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import os

# Paths
chromedriver_path = r"C:\Piyush\Scripts\jobs\classifier\chromedriver-win64\chromedriver-win64\chromedriver.exe"
dest_loc = r"C:\Piyush\Scripts\jobs\classifier\images"
csv_file = r'C:\Piyush\Scripts\jobs\classifier\ajio-male-halfsleeve.csv'
destination_folder = r"C:\Piyush\Scripts\jobs\classifier\images\male_half_sleeve"

# Selenium options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Maximize the browser window
chrome_options.add_argument("--disable-notifications")  # Disable browser notifications

# Initialize WebDriver
try:
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)
except Exception as e:
    print(f"Error initializing WebDriver: {e}")
    exit()

# Target URL
url = 'https://www.ajio.com/men-tshirts/c/830216014'

# Access URL
try:
    driver.get(url)
except Exception as e:
    print(f"Error accessing URL {url}: {e}")
    driver.quit()
    exit()

# Scroll settings
scroll_pause_time = 10
scroll_step = 2000
try:
    scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
except Exception as e:
    print(f"Error getting scroll height: {e}")
    driver.quit()
    exit()

hrefs = set()

# Initial scroll to start lazy loading
try:
    driver.execute_script("window.scrollTo(0, " + str(scroll_step) + ");")
    time.sleep(5)
except Exception as e:
    print(f"Error during initial scroll: {e}")
    driver.quit()
    exit()

# Scroll and collect image URLs
try:
    while len(hrefs) < 10:
        try:
            image_elements = driver.find_elements(By.XPATH, '//img[@class="rilrtl-lazy-img  rilrtl-lazy-img-loaded"]')
            for image_element in image_elements:
                href = image_element.get_attribute('src')
                print(href)
                if href:
                    hrefs.add(href)
        except Exception as e:
            print(f"Error finding or processing image elements: {e}")

        try:
            driver.execute_script("window.scrollBy(0, " + str(scroll_step) + ");")
            time.sleep(scroll_pause_time)
        except Exception as e:
            print(f"Error during scroll: {e}")
except Exception as e:
    print(f"Error during scrolling and collecting hrefs: {e}")

# Store hrefs into CSV
try:
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['href'])
        writer.writerows([[href] for href in hrefs])
except Exception as e:
    print(f"Error writing to CSV file {csv_file}: {e}")

# Close the browser
try:
    driver.quit()
except Exception as e:
    print(f"Error closing the browser: {e}")

# Function to read CSV and return a list of URLs
def read_csv(file_path):
    urls = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                if row:
                    urls.append(row[0])
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return urls

# Function to download images
def download_images(urls, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    for i, url in enumerate(urls):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                file_path = os.path.join(dest_folder, f'image_{i + 1}.jpg')
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Downloaded {url} as image_{i + 1}.jpg")
            else:
                print(f"Failed to download {url}: Status code {response.status_code}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

# Example usage
urls = read_csv(csv_file)
download_images(urls, destination_folder)
