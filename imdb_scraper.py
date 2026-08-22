from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# ✅ Anti-detection options
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ✅ Extra step to hide navigator.webdriver flag
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
})

url = "https://www.imdb.com/chart/top/"
driver.get(url)

print("Scraping started...\n")

# ✅ WAIT for movies to load
movies = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "ul.ipc-metadata-list li")
    )
)

data = []

for i, movie in enumerate(movies, start=1):
    try:
        title = movie.find_element(By.CSS_SELECTOR, "h3").text
        rating = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star").text
        year = movie.find_elements(By.CSS_SELECTOR, "span")[-1].text

        data.append([i, title, year, rating])

        # ✅ TERMINAL OUTPUT (line by line)
        print(f"{i:3} | {title:45} | {year} | {rating}")

    except:
        continue

driver.quit()

df = pd.DataFrame(
    data,
    columns=["Rank", "Movie Title", "Release Year", "IMDb Rating"]
)

# ✅ TABLE FORMAT OUTPUT IN TERMINAL
print("\n================ IMDb TOP 250 TABLE =================\n")
print(df.to_string(index=False))

df.to_csv("imdb_top_250_movies.csv", index=False)

print("\nTotal movies scraped:", len(df))
print("IMDb Top 250 Movies CSV file created successfully!")