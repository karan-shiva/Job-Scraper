# Job Scraper 🧠💼

This is a Python-based web scraping tool using Selenium that searches for software engineering job listings from [Google Careers](https://careers.google.com), filters them based on keywords in the title and description, and prints results with full details including job title, link, and qualification checks.

---

## 🚀 Features

- Searches Google Careers by keyword (e.g., `"Software Developer"`)
- Filters out job titles with unwanted keywords (e.g., `"Senior"`, `"Mobile"`, etc.)
- Inspects **Minimum** and **Preferred Qualifications** on the same page
- Filters out roles mentioning disqualifying experience (e.g., `"5 years of experience"`)
- Logs skipped jobs to `cancel.txt`
- Outputs matched jobs with structured details

---

## 📦 Requirements

- Python 3.7+
- Google Chrome installed
- ChromeDriver (automatically managed via `webdriver-manager`)

Install dependencies:

```bash
pip install selenium webdriver-manager
