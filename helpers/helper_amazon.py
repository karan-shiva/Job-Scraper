from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from defs import *
from helpers import Base

class Amazon(Base):

  company = "amazon"

  def get_jobs(self, url):
      self.driver.get(url)
      try:
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.job-link"))
        )
      except:
        return []
      
      return self.driver.find_elements(By.CSS_SELECTOR, "a.job-link")

  def get_qualifications(self, link, qual_type):
    qual = "BASIC QUALIFICATIONS" if qual_type == MIN_QUAL else "PREFERRED QUALIFICATIONS"
    
    self.child_driver.get(link)
    WebDriverWait(self.child_driver, 5).until(
      EC.presence_of_element_located((By.XPATH,".//h2[contains(text(), '{}')]".format(qual)))
    )

    qual_header = self.child_driver.find_element(By.XPATH,".//h2[contains(text(), '{}')]".format(qual))
    p = qual_header.find_element(By.XPATH, "./following-sibling::p")
    return [p.text.replace("Amazon is an equal opportunity employer and does not discriminate on the basis of protected veteran status, disability, or other legally protected status.","").
            replace("Our inclusive culture empowers Amazonians to deliver the best results for our customers. If you have a disability and need a workplace accommodation or adjustment during the application and hiring process, including support for the interview or onboarding process, please visit","").
            replace("https://amazon.jobs/content/en/how-we-hire/accommodations","").
            replace("for more information. If the country/region you’re applying in isn’t listed, please contact your Recruiting Partner.","").
            replace("Our compensation reflects the cost of labor across several US geographic markets. The base pay for this position ranges from $99,500/year in our lowest geographic market up to $200,000/year in our highest geographic market. Pay is based on a number of factors including market location and may vary depending on job-related knowledge, skills, and experience. Amazon is a total compensation company. Dependent on the position offered, equity, sign-on payments, and other forms of compensation may be provided as part of a total compensation package, in addition to a full range of medical, financial, and/or other benefits. For more information,  please visit","").
            replace("https://www.aboutamazon.com/workplace/employee-benefits","").
            replace(". This position will remain posted until filled. Applicants should apply via our internal or external career site.","")]
  
  @staticmethod
  def get_title_and_link(job):
    title = job.text.strip()
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
    return [
            "https://www.amazon.jobs/en/search?base_query=%22{}%22&offset={}&result_limit=10&sort=recent&distanceType=Mi&radius=80km&industry_experience=less_than_1_year&latitude=38.89036&longitude=-77.03196&loc_group_id=&loc_query=United%20States&city=&country=USA&region=&county=&query_options=&",
            "https://www.amazon.jobs/en/search?base_query=%22{}%22&offset={}0&result_limit=10&sort=recent&distanceType=Mi&radius=80km&industry_experience=one_to_three_years&latitude=38.89036&longitude=-77.03196&loc_group_id=&loc_query=United%20States&city=&country=USA&region=&county=&query_options=&"
            ]
  
  @staticmethod
  def get_start_pageID():
    return 0
  
  @staticmethod
  def get_page_increement():
    return 10