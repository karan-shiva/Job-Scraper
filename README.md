# Job Scraper 🧠💼

A modular, extensible Python-based job scraping framework that extracts job listings from multiple company career portals. It uses a clean, template-driven structure to make scaling effortless — just copy and configure a new helper file for any company, and their job listings will be stored in a dedicated folder. 

---

## 🚀 Features

### 🔧 Core Functionality (Base Features)

* 🔍 **Searches Career Websites by keyword** (e.g., `"Software Developer"`)
* ❌ **Filters out job titles** with unwanted terms (e.g., `"Senior"`, `"Mobile"`)
* 🧠 **Inspects 'Minimum' and 'Preferred Qualifications'** for filtering criteria
* ⚠️ **Skips jobs mentioning disqualifying experience** (e.g., `"5 years of experience"`)
* 🗂️ **Logs skipped jobs** to structured files:

  * `<company>-exclude-title.txt` for title-based exclusions
  * `<company>-exclude-desc.txt` for description-based exclusions
* 📄 **Outputs matched jobs** to text files with structured formatting: title, description, and job link

### 🧱 Template-Based Architecture (Scalability Features)

* 🧩 **Easily extendable** via reusable `helper_template.py`
* 📁 **Each company has its own helper file** and a dedicated output directory
* ✂️ **In-built filtering logic** per helper
* 🧹 **Clean separation of output** for accepted and excluded jobs

---

## 🏗️ Project Structure

```
.
├── helpers/
│   ├── helper_base.py             # Core logic shared by all scrapers
│   ├── helper_template.py         # Template to create new scrapers
│   ├── helper_google.py           # Google scraper (example)
│   └── helper_amazon.py           # Amazon scraper (example)
├── google/
│   ├── google-jobs.txt
│   ├── google-exclude-title.txt
│   └── google-exclude-desc.txt
├── amazon/
│   ├── amazon-jobs.txt
│   ├── amazon-exclude-title.txt
│   └── amazon-exclude-desc.txt
├── webscraper.py                  # Main script to run all scrapers
└── requirements.txt               # Dependencies
```

---

## 🧠 How It Works

1. **Each helper file (e.g., `helper_google.py`)** scrapes jobs from the respective company's website.
2. Jobs are filtered based on titles and descriptions (logic defined within the helper file).
3. Results are saved inside a company-specific folder:

   * `<company>/<company>-jobs.txt` – accepted jobs
   * `<company>/<company>-exclude-title.txt` – excluded by title
   * `<company>/<company>-exclude-desc.txt` – excluded by description

---

## 🧩 Adding a New Company

To add a new scraper for a company:

1. **Copy the template**:

   ```bash
   cp helpers/helper_template.py helpers/helper_<company>.py
   ```

2. **Inside `helper_<company>.py`, update**:

   * 🔗 **`base_url`** – Set the correct careers page.
   * ❌ **`exclude_titles` / `exclude_descriptions`** – Customize keywords to filter unwanted job titles and descriptions.
   * 🏷️ **Selenium selectors** – Update `find_element` / `find_elements` logic to correctly extract:

     * Job Title
     * Job Description
     * Job URL (if applicable)

3. **In `webscraper.py`, import and run your scraper**:

   ```python
   from helpers import helper_<company>

   scraper = helper_<company>.YourCompanyScraper()
   scraper.print_valid_jobs()
   ```

4. **Execute**:

   ```bash
   python webscraper.py
   ```

---

## ✅ Example Output

Running `python webscraper.py` with Google and Amazon enabled will result in:

```
google/
├── google-jobs.txt
├── google-exclude-title.txt
└── google-exclude-desc.txt

amazon/
├── amazon-jobs.txt
├── amazon-exclude-title.txt
└── amazon-exclude-desc.txt
```

---

## 📦 Installation

```bash
git clone https://github.com/karan-shiva/Job-Scraper.git
cd Job-Scraper
pip install -r requirements.txt
```

---

## 👨‍💻 Author

**Karan Shiva**
GitHub: [@karan-shiva](https://github.com/karan-shiva)

---

