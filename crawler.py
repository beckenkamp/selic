import requests
from bs4 import BeautifulSoup


def get_table_value(year_index, month, table):
    rows = [tr for tr in table.find_all('tr')]
    cols = [col for col in rows[month].find_all('td')]
    return float(cols[year_index].text.replace('%', '').replace(',', '.'))


def crawler(year, month):
    url = 'http://idg.receita.fazenda.gov.br/orientacao/' \
          'tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic'

    response = requests.get(url)
    data = response.text

    soup = BeautifulSoup(data, 'html.parser')

    tables = [table for table in soup.find_all('table')]
        
    if year >= 2011 and year <= 2017:
        year_index = [i for i in range(2011, 2018)].index(year) + 1
        return get_table_value(year_index, month, tables[1])

    if year >= 2003 and year <= 2010:
        year_index = [i for i in range(2003, 2010)].index(year) + 1
        return get_table_value(year_index, month, tables[2])

    if year >= 1995 and year <= 2002:
        year_index = [i for i in range(1995, 2002)].index(year) + 1
        return get_table_value(year_index, month, tables[3])


if __name__ == '__main__':
    print(crawler(2012, 9))