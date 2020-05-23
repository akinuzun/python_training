import requests
from bs4 import BeautifulSoup

headers_param = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
glassdoor = requests.get("https://www.glassdoor.com/List/Best-Jobs-in-America-LST_KQ0,20.htm", headers=headers_param)

# print(glassdoor.status_code)

jobs = glassdoor.content
soup = BeautifulSoup(jobs, "html.parser")

# print(soup.title)

print(soup.find("h1").text)

all_jobs = soup.find_all("p", {"class":"h2 m-0 entryWinner pb-std pb-md-0"})

for job in all_jobs:
    print(job.a.text)

all_data = soup.find_all("div", {"class":"col-6 col-lg-4 dataPoint"})

for data in all_data:
    print(data.text)
    