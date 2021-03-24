import time

from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome()
driver.set_page_load_timeout(40)


link = "https://en.wikipedia.org/wiki/List_of_birds_by_common_name"

driver.get(link)
time.sleep(1)


url_soup = BeautifulSoup(driver.page_source, "lxml")


# For getting names starting from all alphabets except Q and X
alphabet_divs = url_soup.select(".div-col")

len(alphabet_divs)


birmd_names = []

for i in range(len(alphabet_divs)):
    curr_div = alphabet_divs[i]
    curr_names = [tag.text for tag in curr_div.find_all("a")]
    birmd_names += curr_names

print(len(birmd_names))


# For getting names starting with Q and X

headings = url_soup.select("h2 span.mw-headline")
qx_links = [
    heading.parent.next_sibling.next_sibling
    for heading in headings
    if heading.text == "Q" or heading.text == "X"
]


for i in range(len(qx_links)):
    curr_link = qx_links[i]
    curr_names = [tag.text for tag in curr_link.find_all("a")]
    birmd_names += curr_names

print(len(birmd_names))


birmd_names = [birmd_name.lower() for birmd_name in birmd_names]
birmd_names.sort()
print(len(birmd_names))


with open("birmds.txt", "w+") as f:
    for birmd in birmd_names:
        f.write(birmd)
        f.write("\n")



