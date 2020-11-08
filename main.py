from bs4 import BeautifulSoup
import requests
import pandas as pd

years_url = list(range(2004, 2020))

income_list = []
income_per_club_list = []
income_per_player_list = []
year_list = []

for year_url in years_url:

    url = 'https://www.transfermarkt.com/premier-league/transfers/wettbewerb/GB1/plus/?saison_id=' + str(year_url) + '&s_w=&leihe=0&leihe=1&intern=0&intern=1'

    response = requests.get(url, headers={'User-Agent': 'Custom5'})
    # print(response.status_code)
    financial_data = response.text
    soup = BeautifulSoup(financial_data, 'html.parser')

    grouped_data = soup.find('div', {'class': 'transferbilanz'})

    income = float(grouped_data.find_all('span', {'class': 'greentext'})[0].text.replace(',', '').replace('€', '')) * 0.89
    income_per_club = float(grouped_data.find_all('span', {'class': 'greentext'})[1].text.replace('€', '').replace(',', '')) * 0.89
    income_per_player = float(grouped_data.find_all('span', {'class': 'greentext'})[2].text.replace('€', '').replace(',', '')) * 0.89
    year = year_url

    income_list.append(income)
    income_per_club_list.append(income_per_club)
    income_per_player_list.append(income_per_player)
    year_list.append(year)


finance_df = pd.DataFrame({'Year': year_list,
                           'Income': income_list,
                           'Income_per_club': income_per_club_list,
                           'Income_per_player': income_per_player_list
                            })

finance_df.to_csv('Income_euro_to_pounds.csv', index=False)
Income2004_18_df = pd.read_csv('Income_euro_to_pounds.csv')
