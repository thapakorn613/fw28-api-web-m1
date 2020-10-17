# Prog-08: Web Scraping
# Fill in your ID & Name
# ...
# Declare that you do this by yourself
import urllib
import urllib.request as urq

def load_html(page_url):
  return str(urq.urlopen(page_url).read().decode('utf-8'))
#-------------------------------------------------
from bs4 import BeautifulSoup

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def find_between_r(s, first, last):
    try:
        start = s.rindex(first) + len(first)
        end = start + last
        return s[start:end]
    except ValueError:
        return ""


def get_faculty_names(url):
    s = load_html(url)
    soup = BeautifulSoup(s, "html.parser")
    tempStackFaculty = []
    prefixSplit = "Faculty of"
    for s in soup.strings:
        if (len(s) > 1):
            if (find_between_r(str(s), prefixSplit, len(s))):
                tempStackFaculty.append(
                    prefixSplit+find_between_r(str(s), prefixSplit, len(s)))
    print(tempStackFaculty)
    return tempStackFaculty


def save_image(img_url, img_name):
    fileName = img_name + ".jpg"
    urq.urlretrieve(img_url, fileName)


def download_faculty_images(url):
    s = load_html(url)
    soup = BeautifulSoup(s, "html.parser")
    mediaSet = soup.findAll("div", {"class": "post-media"})
    tempStackImage = []
    prefixSplit = "data-src=\""
    for m in mediaSet:
        mLink = find_between(str(m), prefixSplit, "\" data-srcset")
        img_name = find_between(mLink, "image/", ".jpg")
        save_image(mLink,img_name)

def print_faculty_numbers(url):
    s = load_html(url)
    soup = BeautifulSoup(s, "html.parser")
    mediaSet = soup.findAll("div", {"class": "post-media"})
    tempStackImage = []
    prefixSplit = "href=\""
    for m in mediaSet:
        if(len(find_between(str(m), prefixSplit, "\"")) > 1):
            mLink = find_between(str(m), prefixSplit, "\"")
            q = load_html(mLink)
            soup2 = BeautifulSoup(q, "html.parser")
            preficFaculty = "Faculty of"
            offSetNameFaculty = False
            offSetContact = 0
            for f in soup2.strings:
                if (len(f) > 1 & offSetContact < 2):
                    if(find_between_r(str(f), preficFaculty, len(f))):
                        tempNameFaculty = find_between_r(str(f), preficFaculty, len(f))
                        offSetContact += 1
            fullNameFaculty = preficFaculty + tempNameFaculty            
            nameFaculty = fullNameFaculty.split(", ")
            tempFaculty = nameFaculty[0].lower().split()
            nameLowerJoinSlpitFaculty = '-' .join(tempFaculty)
            print()
            print(nameLowerJoinSlpitFaculty)
            contactSet = soup2.findAll("div", {"class": "wpcf-field-wysiwyg wpcf-field-custom-content-contact-2"})
            prefixSplit2 = "+66"
            for r in contactSet:
                if(len(r) > 1):
                    tempContact = find_between_r(str(r), prefixSplit2,10 )
            print( "0" + tempContact)
#-------------------------------------------------
def main():
  pageurl = "https://waiiinta.github.io/"

  print(get_faculty_names(pageurl))

  download_faculty_images(pageurl)

  print_faculty_numbers(pageurl)
#-------------------------------------------------
main()
