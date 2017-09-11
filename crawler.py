import requests
from bs4 import BeautifulSoup


def get_table_value(year_index, month, table):
    """
    Finds a float value from the result table
    """
    rows = [tr for tr in table.find_all('tr')]
    cols = [col for col in rows[month].find_all('td')]
    return cols[year_index].text


def crawler(year, month):
    """
    Scraps the Brazilian's Treasury Office website for the SELIC rate values 
    for every month of every year from 1995 to 2017
    """ 
    url = 'http://idg.receita.fazenda.gov.br/orientacao/' \
          'tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic'

    response = requests.get(url)
    data = response.text

    soup = BeautifulSoup(data, 'html.parser')

    tables = [table for table in soup.find_all('table')]
        
    # The first table have from 2011 to 2017 years values
    if year >= 2011 and year <= 2017:
        year_index = [i for i in range(2011, 2018)].index(year) + 1
        selic = get_table_value(year_index, month, tables[1])
        if selic:
            return selic

    # The first table have from 2003 to 2010 years values
    if year >= 2003 and year <= 2010:
        year_index = [i for i in range(2003, 2011)].index(year) + 1
        selic = get_table_value(year_index, month, tables[2])
        if selic:
            return selic

    # The first table have from 1995 to 2002 years values
    if year >= 1995 and year <= 2002:
        year_index = [i for i in range(1995, 2003)].index(year) + 1
        selic = get_table_value(year_index, month, tables[3])
        if selic:
            return selic

    return "Sem registro"


if __name__ == '__main__':
    print(crawler(2012, 9))