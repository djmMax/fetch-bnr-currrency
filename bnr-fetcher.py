import csv
from bs4 import BeautifulSoup
import requests
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

def get_exchange_rates(url):
    # Make a GET request to the website
    response = requests.get(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table containing the exchange rates
    table = soup.find('table', {'class': 'table table-bordered table-hover'})
    # Initialize an empty list to store the exchange rates
    exchange_rates = []
    # Iterate through the rows of the table
    for row in table.find('tbody').find_all('tr'):
        # Initialize a dictionary to store the exchange rate data for this row
        data = {}
        # Get the columns of the row
        columns = row.find_all('td')
        # Extract the data from the columns and add it to the dictionary
        data['country'] = columns[0].find('img')['alt']
        data['code'] = columns[1].text
        data['date'] = columns[2].text
        data['buying_value'] = locale.atof(columns[3].text)
        data['average_value'] = locale.atof(columns[4].text)
        data['selling_value'] = locale.atof(columns[5].text)
        # Add the dictionary to the list
        exchange_rates.append(data)
    # Return the list of exchange rates
    return exchange_rates, soup

def main():
    # Initialize the URL of the first page
    base_url = 'https://www.bnr.rw/'
    url = base_url + 'currency/exchange-rate/'
    # Initialize a list to store all the exchange rates
    all_rates = []
    # Loop until there are no more pages
    while True:
        # Get the exchange rates for the current page
        rates, soup = get_exchange_rates(url)
        # Add the exchange rates to the list
        all_rates += rates
        # Find the next page button
        next_button = soup.find('li', {'class': 'next'})
        # If there is no next page button, we have reached the last page
        if next_button is None:
            break
        # Get the URL of the next page
        url = base_url + next_button.find('a')['href']
    # Write the exchange rates to a CSV file
    with open('exchange_rates.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=rates[0].keys())
        writer.writeheader()
        writer.writerows(all_rates)

if __name__ == '__main__':
    main()
