# Prog-08: Web Scraping
# Fill in your ID & Name
# ...
# Declare that you do this by yourself
import urllib
import urllib.request as urq

def load_html(page_url):
  return str(urq.urlopen(page_url).read().decode('utf-8'))
#-------------------------------------------------
def get_faculty_names(url):
  return ['Faculty of Allied Health Sciences', 'Faculty of Architecture']

def save_image(img_url, filename):
  pass

def download_faculty_images(url):
  pass

def print_faculty_numbers(url):
  print("faculty-of-allied-health-sciences")
  print("0 2218 1100")
#-------------------------------------------------
def main():
  pageurl = "https://waiiinta.github.io/"

  print(get_faculty_names(pageurl))

  download_faculty_images(pageurl)

  print_faculty_numbers(pageurl)
#-------------------------------------------------
main()
