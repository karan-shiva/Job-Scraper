from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from helpers import Apple, Meta, Google, Remitly, Microsoft, Amazon
from defs import *
from urllib.parse import quote

def check_and_get_quals(company, link, exclude_description, qual_type):
  quals = company.get_qualifications(link, qual_type)
  desc = []
  for qual in quals:
    desc.append(qual)
    if any(desc in qual for desc in exclude_description):
      return (True, desc)
  return (False, desc)

def output_jobs(company: Apple, filter, exclude_titles, exclude_descriptions):
  link_set = set(company.get_link())
  base_urls = company.get_base_url()
  quals = company.get_quals()

  company.print("\n✅ Filtered Job Titles with filter: {}: \n".format(filter))

  for i, base_url in enumerate(base_urls):
    page = company.get_start_pageID()
    counter = 1
    date_counter = 1
    date_check = True

    company.print("🔗 BASE_URL {}\n".format(i+1))
    while True:
      desc_dict = {}

      print(page)
      if page > company.get_max_pages():
        break
      url = base_url.format(filter, page)
      # print(url)
      jobs = company.get_jobs(url)

      if not jobs:
        break

      for j, job in enumerate(jobs):
        title, link = company.get_title_and_link(job)

        if title and link not in link_set and not any(ex in title for ex in exclude_titles):
          company.print_link(link)
          flag = True
          for qual in quals:
            try:
              flag, descs = check_and_get_quals(company, link, exclude_descriptions, qual)
            except Exception as e:
              # company.print("ERROR: link: {}".format(link))
              # company.print("ERROR: url: {}".format(url))
              # company.print("ERROR: qual_type: {}".format(qual))
              # company.print("")
              # print("ERROR SEEN")
              # print(e)
              # break
              descs  = ["NO DESC"]
            if flag:
              company.print_exclude_desc(title, link, descs)
              break
            desc_dict[qual] = descs
          
          if flag:
            continue

          if not company.check_date(j):
            date_check = False
            break
          company.print("{}) ({}) {}".format(counter, date_counter, title))
          date_check = company.print_and_check_date(j)
          company.print(link)

          for qual in quals:
            company.print("{}: ".format(qual))
            for desc in desc_dict[qual]:
              company.print("* {}".format(desc))
            company.print("")
          
          link_set.add(link)
          company.print("-"*110+"\n")
          counter += 1
          if not date_check:
            break
        else:
          company.print_exlucde_title(title)
        date_counter += 1
            
      page += company.get_page_increement()
      if not date_check:
        break
    print("Total jobs: {}".format(counter-1))
   

def run_script(company):
  try:
    options = Options()
    options.add_argument("--headless=new")  # Use "--headless=new" for Chrome 109+
    options.add_argument("--disable-gpu")   # Optional: improves compatibility
    options.add_argument("--window-size=1920,1080")  # Optional: needed for some rendering

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    child_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    company.set_drivers(driver, child_driver)
    
    filters, exclude_titles, exclude_descriptions = company.get_filter_and_excludes()

    company.reset_files()

    for filter in filters:
      output_jobs(company, quote(filter), exclude_titles, exclude_descriptions)

  finally:
    if driver:
      driver.quit()
    if child_driver:
      child_driver.quit()



if __name__ == "__main__":
  # run_script(Apple())
  # run_script(Google())
  run_script(Meta())
  # run_script(Microsoft())
  # run_script(Remitly())
  # run_script(Apple())
