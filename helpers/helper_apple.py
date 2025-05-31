from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from defs import *
from helpers import Base

class Apple(Base):

  company = "apple"

  def get_jobs(self, url):
      self.driver.get(url)
      try:
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.link-inline"))
        )
      except:
        return []
      
      return self.driver.find_elements(By.CSS_SELECTOR, "a.link-inline")
  
  def get_li_elements(self, link, qual_type):
    qual = "Minimum Qualifications" if qual_type == MIN_QUAL else "Preferred Qualifications"
    
    self.child_driver.get(link)
    WebDriverWait(self.child_driver, 5).until(
          EC.presence_of_element_located((By.XPATH,".//h2[contains(text(), '{}')]".format(qual)))
      )
    
    qual_header = self.child_driver.find_element(By.XPATH,".//h2[contains(text(), '{}')]".format(qual))
    ul = qual_header.find_element(By.XPATH, "following::ul")
    return ul.find_elements(By.TAG_NAME, "li")
  
  def print_and_check_date(self):
    date = self.child_driver.find_element(By.CSS_SELECTOR,"time")
    self.print(date.text.strip())
    dt = date.get_attribute("datetime")
    given_date = datetime.strptime(dt,"%Y-%m-%d")
    today = datetime.today()
    if (today - given_date).days > 30:
      return False
    return True

  @staticmethod
  def get_title_and_link(job):
    title = " ".join(job.get_attribute("aria-label").split()[:-1])
    link = job.get_attribute("href")
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
                  "Front End",
                  "Sr. Software",
                  "Solutions Architect",
                  "Software Development Engineer in Test",
                  "Sr Software"]
    
    exclude_descriptions = ["5 years",
                            "5+ years",
                            "5 or more years",
                            "7 years",
                            "7+ years",
                            "7 or more years",
                            "10 years",
                            "10+ years",
                            "10 or more years"]
    
    # exclude_descriptions = []
    # exclude_titles = []
    
    return (filters, exclude_titles, exclude_descriptions)

  @staticmethod
  def get_base_url():
    return ["https://jobs.apple.com/en-us/search?search=%22{}%22&sort=newest&location=united-states-USA&page={}&team=machine-learning-infrastructure-MLAI-MLI+apps-and-frameworks-SFTWR-AF+cloud-and-infrastructure-SFTWR-CLD+core-operating-systems-SFTWR-COS+devops-and-site-reliability-SFTWR-DSR+engineering-project-management-SFTWR-EPM+information-systems-and-technology-SFTWR-ISTECH+machine-learning-and-ai-SFTWR-MCHLN+security-and-privacy-SFTWR-SEC+software-quality-automation-and-tools-SFTWR-SQAT+wireless-software-SFTWR-WSFT"]