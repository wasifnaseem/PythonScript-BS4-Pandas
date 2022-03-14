from bs4 import BeautifulSoup
import requests
import pandas as pd

dictionary = {}

#hard coding the page number, therefore 35
for i in range(1,35):
    url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/" + str(i)
    #for feedback from the script
    print (f"Scraping: {url}")
    response = requests.get(url)
    webpage = response.text

    soup = BeautifulSoup(webpage, "html.parser")

    collections = soup.find_all(name="td", class_='data-table__cell')
    #collection include the column heading and the data, printing collection.text will give Degree:Mechanical Enginering
    for collection in collections:
        #Degree:MechanicalEngineering will be split by ":" which will give a list of two values "Degree" and
        # "Mechanical Engineering
        word = collection.text.split(':')
        #Checks if key (Degree) is in dictionary, if it exists, it appends the value
        # (mechanical engineering to the list of existing values). If not, it creates a new key/value pair.
        if word[0] in dictionary:
            dictionary[word[0]].append(word[1])
        else:
            dictionary[word[0]]= [word[1]]

    payscale_df = pd.DataFrame.from_dict(dictionary)

    payscale_df = payscale_df.set_index("Rank")

print (payscale_df)









# print (dictionary)

# for row in table.tbody.find_all('tr'):
#     # Find all data for each column
#     columns = row.find_all('td')
#     print (columns)

# print('Classes of each table:')
# for table in soup.find_all('table'):
#     print(table.get('class'))

