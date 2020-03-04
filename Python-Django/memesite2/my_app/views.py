from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.
def base(request):
    site = "https://kwejk.pl"
    urls = []

    s = requests.Session()

    response = s.get(site)

    soup = BeautifulSoup(response.text, "html.parser")

    page_number = soup.find_all(True, {"class": "btn btn-next btn-gold"})
    page_number_href = ""

    for number in page_number:
        page_number_href = str(number["href"])

    page_number_href = page_number_href[24:]

    for _ in range(int(10)):
        s = requests.Session()

        response = s.get(site)

        soup = BeautifulSoup(response.text, "html.parser")
        tags = soup.find_all(True, {"class": "full-image"})

        for content in tags:
            urls.append((content["src"], content["alt"]))

        page_number = soup.find_all(True, {"class": "btn btn-next btn-gold"})
        page_number_href = ""

        for number in page_number:
            page_number_href = str(number["href"])

        page_number_href = page_number_href[24:]

        print(page_number_href, flush=True)

        stuff_for_frontend = {
            "urls": urls,
        }

        site = "https://kwejk.pl/strona/" + page_number_href


    return render(request, "base.html", stuff_for_frontend)