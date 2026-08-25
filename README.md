# 🎬 IMDb Movie Scraper

## 📌 Project Overview

The **IMDb Movie Scraper** is a Python-based web scraping project developed to collect movie information from IMDb.

The application automates the process of extracting useful movie details from web pages and organizes the collected information into a structured format for further analysis and use.

## 🎯 Objectives

* Scrape movie information from IMDb
* Collect and organize movie details efficiently
* Automate the data collection process
* Store scraped movie information in a structured format
* Reduce manual data collection
* Prepare collected data for further analysis

## 🛠️ Technologies Used

* **Python**
* **Selenium**
* **BeautifulSoup**
* **Pandas**
* **Web Scraping**
* **ChromeDriver**

## ✨ Features

* 🤖 Automated movie data scraping
* 🎬 Extract movie information from IMDb
* 🌐 Handle dynamic web content using Selenium
* 🔎 Parse web page content using BeautifulSoup
* 📊 Store scraped data using Pandas
* 📁 Export collected movie data for further analysis
* ⚡ Reduce manual data collection

## 📊 Data Collected

The scraper can collect movie-related information such as:

* Movie Title
* Release Year
* Movie Rating
* Duration
* Genre
* Movie Description
* Other available movie details

## 🔄 Project Workflow

### 1️⃣ Open IMDb

The scraper accesses the required IMDb movie web pages using Selenium.

### 2️⃣ Load Web Content

Selenium is used to open and interact with the web page, including dynamically loaded content.

### 3️⃣ Extract Page Source

The required web page content is collected for further processing.

### 4️⃣ Parse Movie Information

BeautifulSoup is used to parse the HTML content and extract relevant movie details.

### 5️⃣ Organize the Data

The collected information is organized into structured data using Pandas.

### 6️⃣ Export the Data

The scraped movie information can be saved in a structured format such as CSV for further analysis.

## ⚙️ Installation & Setup

Follow the steps below to set up and run the **IMDb Movie Scraper** on your local system.

### 1️⃣ Install Python

Download and install Python on your system.

Verify the installation:

```bash
python --version
```

### 2️⃣ Install Google Chrome

Make sure **Google Chrome** is installed on your system.

The scraper uses Chrome for browser automation through Selenium.

### 3️⃣ Clone the Repository

Open **Git Bash, Command Prompt, or VS Code Terminal** and run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 4️⃣ Navigate to the Project Folder

```bash
cd imdb-movie-scraper
```

### 5️⃣ Create a Virtual Environment

Create a virtual environment for the project:

```bash
python -m venv .venv
```

### 6️⃣ Activate the Virtual Environment

#### Windows – Command Prompt

```cmd
.venv\Scripts\activate
```

#### Windows – PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows – Git Bash

```bash
source .venv/Scripts/activate
```

After successful activation, you should see:

```text
(.venv)
```

at the beginning of the terminal.

### 7️⃣ Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 8️⃣ Install Required Packages

If a `requirements.txt` file is available, install all dependencies using:

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install the required packages manually:

```bash
pip install selenium beautifulsoup4 pandas
```

### 9️⃣ WebDriver Setup

The project uses **ChromeDriver** with Selenium.

Make sure ChromeDriver is properly configured for your installed Chrome browser version.

If the project uses `webdriver-manager`, install it using:

```bash
pip install webdriver-manager
```

The required driver can then be managed automatically by the project code.

### 🔟 Run the Scraper

Run the main Python file:

```bash
python scraper.py
```

> **Note:** Replace `scraper.py` with the actual Python file name if your project uses a different file name.

The scraper will open the browser, collect the required movie information, and save the extracted data according to the project configuration.

## 📂 Project Structure

```text
IMDb-Movie-Scraper/
│
├── scraper.py
├── requirements.txt
├── data/
│   └── scraped movie data
│
├── output/
│   └── generated output files
│
└── README.md
```

## 📁 Output

The scraped movie information can be exported into a structured file such as:

```text
CSV
```

The output may contain fields such as:

* Movie Title
* Release Year
* Rating
* Duration
* Genre
* Description

## ▶️ Running the Project Again

After completing the initial setup, use the following commands whenever you want to run the scraper again:

### Navigate to the project folder

```bash
cd imdb-movie-scraper
```

### Activate the virtual environment

For Windows:

```bash
.venv\Scripts\activate
```

For Git Bash:

```bash
source .venv/Scripts/activate
```

### Run the scraper

```bash
python scraper.py
```

## 🛑 Stop the Scraper

If the scraper is running and you want to stop the process, press:

```text
Ctrl + C
```

## 🚀 Future Enhancements

* Scrape additional movie details
* Add advanced filtering options
* Store data directly in a database
* Create a movie analytics dashboard
* Add automated scheduled scraping
* Improve scraping performance
* Add data visualization
* Add pagination support
* Add error handling and logging
* Automate data cleaning and preprocessing

## 💡 Benefits

The IMDb Movie Scraper helps to:

* Automate movie data collection
* Reduce manual data entry
* Collect large amounts of movie information efficiently
* Organize scraped data systematically
* Prepare data for analysis and visualization
* Demonstrate practical web scraping techniques

## 📌 Key Outcome

The **IMDb Movie Scraper** demonstrates how Python-based web scraping technologies such as **Selenium and BeautifulSoup** can be used to automatically collect and organize movie information from web pages for further analysis.

LinkedIn: https://www.linkedin.com/in/rajasree-karthick-497074294
