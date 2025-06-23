import requests
from bs4 import BeautifulSoup


def get_data_from_table_html(table_html):
  parsed_data = list()

  rows = table_html.find_all("tr")
  for row in rows:
    column = row.find_all(["td", "th"])
    data = [col.get_text(strip=True) for col in column]
    parsed_data.append(data)

  return parsed_data

url = "https://yetiairlines.com/flight-status"

response = requests.get(url)

if response.status_code != 200:
  raise Exception(f"Error Fetching the data {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
table_html_content = soup.find("table", {"id": "flightInfo"})
scrapped_data = get_data_from_table_html(table_html_content)


for record in scrapped_data:
  print(record)