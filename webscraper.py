from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def check_qual(card, exclude_description, xpath):
  min_qual_header = card.find_element(By.XPATH, xpath)
  ul = min_qual_header.find_element(By.XPATH, "./following-sibling::ul")
  li_elements = ul.find_elements(By.TAG_NAME, "li")
  desc = []
  for li in li_elements:
    qual_text = li.text.lower()
    desc.append(qual_text)
    if any(desc in qual_text for desc in exclude_description):
      return (True, desc)
  return (False, desc)

def write_cancel(desc, link, title):
  with open("cancel.txt", "a") as f:
    f.write("{}\n".format(title))
    for desc in desc:
      f.write("{}\n".format(desc))
    f.write("{}\n\n".format(link))

def get_title_and_link(filter, exclude_title, exclude_description, driver):
  link_set = set()
  counter = 1
  page = 1
  base_url = "https://www.google.com/about/careers/applications/jobs/results/?q=%22{}%22&target_level=EARLY&target_level=MID&location=United%20States&sort_by=date&page={}"

  print("\n✅ Filtered Job Titles with filter: ",filter,":\n")

  while True:
    # print("-------------------------------PAGE ",page,"-------------------------------")
    driver.get(base_url.format(filter, page))

    # Explicit wait until job titles are present
    try:
      WebDriverWait(driver, 5).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, "h3.QJPWVe"))
      )

      cards = driver.find_elements(By.CSS_SELECTOR, "div[jscontroller='snXUJb']")

      # print(len(cards))

      for card in cards:
          title = card.find_elements(By.CSS_SELECTOR, "h3.QJPWVe")[0].text.strip()
          link = card.find_elements(By.CSS_SELECTOR, "a.WpHeLc")[0].get_attribute("href")

          if title and link not in link_set and not any(ex in title for ex in exclude_title):
          # if title:
              (flag, min_descs) = check_qual(card, exclude_description, ".//h4[contains(text(), 'Minimum qualifications')]")
              if flag:
                write_cancel(min_descs, link, title)
              else:
                child_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                child_driver.get(link)
                flag, pref_qual = check_qual(child_driver,exclude_description,".//h3[contains(text(), 'Preferred qualifications')]")
                child_driver.quit()
                if flag:
                  write_cancel(pref_qual, link, title)
                else:
                  print("{}) {}".format(counter, title))
                  print(link)
                  print("Min Qual: ")
                  for desc in min_descs:
                    print(desc)
                  print()
                  print("Pref Qual")
                  for desc in pref_qual:
                    print(desc)
                  
                  link_set.add(link)
                  print("-"*120,"\n")
                  counter += 1
      page += 1
    
    except:
      break
   


# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
filters = ["Software Engineer",
           "Software Developer"]

# filters = ["Software Developer"]

exclude_title = ["Senior",
           "Staff",
           "Mobile",
           "Android",
           "iOS",
           "Manager",
           "PhD"]

exclude_description = ["5 years of experience"]

with open("cancel.txt","w"):
  a = 5

# exclude = []

for filter in filters:
  get_title_and_link(filter.replace(" ","%20"), exclude_title, exclude_description, driver)

driver.quit()
