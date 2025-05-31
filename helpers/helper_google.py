from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from defs import *
from helpers import Base

class Google(Base):

  company = "google"

  def get_jobs(self, url):
      self.driver.get(url)
      try:
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3.QJPWVe"))
        )
      except:
        return []
      
      return self.driver.find_elements(By.CSS_SELECTOR, "div[jscontroller='snXUJb']")

  def get_li_elements(self, link, qual_type):
    if qual_type == MIN_QUAL:
      qual = ".//h4[contains(text(), 'Minimum qualifications')]"
      qual_header = self.driver.find_element(By.XPATH,qual)
    else:
      qual = ".//h3[contains(text(), 'Preferred qualifications')]"
      self.child_driver.get(link)
      WebDriverWait(self.child_driver, 5).until(
          EC.presence_of_element_located((By.XPATH,qual))
      )
      qual_header = self.child_driver.find_element(By.XPATH,qual)
    ul = qual_header.find_element(By.XPATH, "./following-sibling::ul")
    return ul.find_elements(By.TAG_NAME, "li")
  
  @staticmethod
  def get_title_and_link(job):
    title = job.find_elements(By.CSS_SELECTOR, "h3.QJPWVe")[0].text.strip()
    link = job.find_elements(By.CSS_SELECTOR, "a.WpHeLc")[0].get_attribute("href")
    return (title, link)

  @staticmethod
  def get_filter_and_excludes():
    filters = ["Software Engineer",
              "Software Developer"]
    
    exclude_titles = ["Senior",
                      "Staff",
                      "Mobile",
                      "Android",
                      "iOS",
                      "Manager",
                      "PhD",
                      "Front End"
                      ]
    
    exclude_descriptions = []
    for i in range(5,11):
      exclude_descriptions.append("{} years".format(i))
      exclude_descriptions.append("{}+ years".format(i))
      exclude_descriptions.append("{} or more years".format(i))
    
    return (filters, exclude_titles, exclude_descriptions)

  @staticmethod
  def get_base_url():
    return ["https://www.google.com/about/careers/applications/jobs/results/?q=%22{}%22&target_level=EARLY&target_level=MID&location=United%20States&sort_by=date&page={}"]