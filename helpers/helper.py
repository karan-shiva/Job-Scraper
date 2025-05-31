from defs import *

class Base:

  company = "base"
  driver = None
  child_driver = None

  def print(self, s):
    with open("{}/{}-jobs.txt".format(self.company, self.company),"a") as f:
      f.write(s)
      f.write("\n")

  def print_exlucde_title(self, title):
    with open("{}/{}-exclude-title.txt".format(self.company, self.company),"a") as f:
      f.write(title)
      f.write("\n")

  def print_exclude_desc(self, title, link, desc):
      with open("{}/{}-exlude-desc.txt".format(self.company, self.company), "a") as f:
        f.write("{}\n".format(title))
        for desc in desc:
          f.write("{}\n".format(desc))
        f.write("{}\n\n".format(link))

  def print_and_check_date(self):
    return True

  def reset_files(self):
    with open("{}/{}-jobs.txt".format(self.company, self.company),"w"):
      pass
    with open("{}/{}-exclude-title.txt".format(self.company, self.company),"w"):
      pass
    with open("{}/{}-exlude-desc.txt".format(self.company, self.company), "w"):
      pass

  def set_drivers(self, driver, child_driver):
    self.driver = driver
    self.child_driver = child_driver

  @staticmethod
  def get_quals():
    return [MIN_QUAL, PREF_QUAL]
  
  @staticmethod
  def get_start_pageID():
    return 1
  
  @staticmethod
  def get_page_increement():
    return 1
  
  def get_qualifications(self, link, qual_type):
    li_elements = self.get_li_elements(link, qual_type)
    return [li.text for li in li_elements]
  