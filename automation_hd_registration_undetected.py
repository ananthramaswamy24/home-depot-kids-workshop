#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
# import relevant libraries
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import ssl
import certifi
import os

# Fix SSL certificate issues on macOS
ssl._create_default_https_context = ssl._create_unverified_context
os.environ['SSL_CERT_FILE'] = certifi.where()

# define url
url = "https://www.homedepot.com/c/kids-workshop"

# Initialize undetected Chrome browser (automatically bypasses bot detection)
# This works on macOS and bypasses Cloudflare and other bot detection
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# Note: undetected-chromedriver handles these automatically, so we keep it simple

# Initialize Chrome - undetected-chromedriver will auto-detect Chrome version
# If SSL errors occur, it will retry automatically
try:
    driver = uc.Chrome(options=options, use_subprocess=True)
except Exception as e:
    print(f"Error initializing Chrome: {e}")
    print("Trying with driver_executable_path=None...")
    # Fallback: let it auto-detect everything
    driver = uc.Chrome(options=options)

# Execute script to remove webdriver property
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# maximize browser window
driver.maximize_window()

# load the webpage 
driver.get(url)

# Add initial delay to let page load naturally
sleep(random.uniform(2, 3))

wait = WebDriverWait(driver, 30)

# find the register button
register_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Hero-31VZOFQYk9QZDcSiaC6SJ7"]/div/button')))
# Add small delay before clicking
sleep(random.uniform(0.5, 1.0))
# click on the register button
register_button.click()
# Add delay after clicking to let page load naturally
sleep(random.uniform(2, 3))

# wait for the form to load after clicking register

# Wait for the first name field to be present and clickable
# Use a stable selector instead of the brittle absolute XPath
wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'First') or contains(@name,'first')]")))
# Add a small random delay to appear more human-like
sleep(random.uniform(0.5, 1.5))
# Re-find the element right before using it to avoid stale element errors
first_name = driver.find_element(By.XPATH, "//input[contains(@placeholder,'First') or contains(@name,'first')]")
# fill out the first name field
first_name.send_keys("ananth")


# find the last name field 
sleep(random.uniform(0.3, 0.8))
wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'Last') or contains(@name,'last')]")))
# Re-find the element right before using it
last_name = driver.find_element(By.XPATH, "//input[contains(@placeholder,'Last') or contains(@name,'last')]")
# fill out the last name field 
last_name.send_keys("ram")

# find the email field 
sleep(random.uniform(0.3, 0.8))
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email' or contains(@placeholder,'email') or contains(@name,'email')]")))
# Re-find the element right before using it
email = driver.find_element(By.XPATH, "//input[@type='email' or contains(@placeholder,'email') or contains(@name,'email')]")
# fill in the email field 
email.send_keys("younggunnerananth@gmail.com")


# click workshop name dropdown
sleep(random.uniform(0.5, 1.0))
workshop_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sui-wGoZRs6NhEZq9kXIsdHoa"]/span[1]')))
# click on it 
workshop_name.click()
sleep(random.uniform(0.5, 1.0))


# click workshop selection dropdown
# NOTE: This XPath contains [object Object] which may need to be fixed
sleep(random.uniform(0.5, 1.0))
try:
    workshop_selection = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sui-zAxHOkYdWq3su0FFU7vRy-[object Object]"]')))
    # click on it 
    workshop_selection.click()
    sleep(random.uniform(0.5, 1.0))
except Exception as e:
    print(f"Warning: Could not find workshop selection: {e}")


# click workshop selection dropdown
sleep(random.uniform(0.5, 1.0))
reference_workshop_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sui-KALV2dQqQmrhnx7xikRYa"]/span[1]')))
# click on it 
reference_workshop_dropdown.click()
sleep(random.uniform(0.5, 1.0))

# click workshop selection dropdown
reference_workshop_selection = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sui-hVNcfQ3k-eQBoJE7zgGMd-Social Media - Instagram"]')))
# click on it 
reference_workshop_selection.click()
sleep(random.uniform(0.5, 1.0))


# find the register button
register_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[12]/div[3]/div/div[2]/div/div/form/div[7]/div[2]/div/button')))
# click on the continue button
register_button.click()

# scroll down by 200 units to view the lower part of the page
sleep(random.uniform(1, 2))
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

# pause the program to view the results
sleep(30)

# close the driver
driver.quit()

