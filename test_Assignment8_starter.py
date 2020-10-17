# Prog-08: Web Scraping
# Fill in your ID & Name
# ...
# Declare that you do this by yourself
import urllib

import urllib.request as urq
import re
import codecs
from bs4 import BeautifulSoup


def load_html(page_url):
    return str(urq.urlopen(page_url).read().decode('utf-8'))
# -------------------------------------------------


def wordiest_line(url):
    resp = urq.urlopen(url)
    charset = resp.headers.get_content_charset()
    textreader = urq.codecs.getreader(charset)(resp)
    for line in textreader:
        line = line.rstrip()


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
    print(len(mediaSet))
    tempStackImage = []
    prefixSplit = "data-src=\""
    for m in mediaSet:
        mLink = find_between(str(m), prefixSplit, "\" data-srcset")
        img_name = find_between(mLink, "image/", ".jpg")
        save_image(mLink,img_name)

def print_faculty_numbers(url):
    print("faculty-of-allied-health-sciences")
    print("0 2218 1100")
# -------------------------------------------------


def main():
    pageurl = "https://waiiinta.github.io/"

    # print(get_faculty_names(pageurl))
    
    download_faculty_images(pageurl)

    # print_faculty_numbers(pageurl)


# -------------------------------------------------
main()
