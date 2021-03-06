from bs4 import BeautifulSoup
import download_as_csv

soup = BeautifulSoup (open("beautiful_soup.html"), features="lxml")

final_link = soup.p.a
final_link.decompose()

f = download_as_csv.writer(open("43rd_Congress.csv", "w"))
f.writerow(["Name", "Link"])    # Write column headers as the first line

links = soup.find_all('a')
for link in links:
    names = link.contents[0]
    fullLink = link.get('href')

    f.writerow([names,fullLink])