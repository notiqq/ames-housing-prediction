import requests
from bs4 import BeautifulSoup

class Spider():
    url = "https://www.century21.com/real-estate-offices/iowa/LSIA/"
    domain = "https://www.century21.com"
    def __init__(self, url = None, domain = None):
        self.url = url if url != None else self.url
        self.domain = domain if domain != None else self.domain

    def scrape_data(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, "html.parser")
        list_items = soup.find("div", class_="infinite-container").find_all("div" , class_ = "infinite-item office-card clearfix")
        results = []
        for item in list_items:
            try:
                link = item.find("a", class_="office-name")
                tp = link.getText().replace("\r\n","").replace("  ", "")
                address = item.find("div", class_ = "office-address-info").getText().replace("\r\n","").replace("  ", "").replace("\n","")
                url = self.domain + link.attrs["href"]
                results.append(dict(type = tp, url = url, address = address))
            except Exception as ex:
                print(ex)
        return results