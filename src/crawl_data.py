import requests
from bs4 import BeautifulSoup
import pandas as pd


# Define headers and an empty Dataframe
headers = ['no.', 'id', 'name', 'dob', 'gender', 'note']
df = pd.DataFrame(columns=headers)
# Define list of class
class_list = ['10a1', '10a10', '10a11', '10a2', '10a3', '10a4', '10a5', '10a6', '10a7', '10a8', '10a9', '10c1', '10c2', '11a1', '11a10', '11a11', '11a2', '11a3', '11a4',
              '11a5', '11a6', '11a7', '11a8', '11a9', '11c1', '11c2', '11c3', '12a1', '12a2', '12a3', '12a4', '12a5', '12a6', '12a7', '12a8', '12c1', '12c2', '12c3', '12c4', '12c5', '12c6']

for cls in class_list:
    # Create URL
    url = f'http://thptbinhphu.edu.vn/danh-sach-hoc-sinh-lop-{cls}-nam-hoc-2021-2022.html'
    # Create page object
    page = requests.get(url)
    # HTML page
    soup = BeautifulSoup(page.text, 'lxml')
    # Get HTML table
    table = soup.find('table')
    # Convert HTML table to Pandas Dataframe
    temp_df = pd.DataFrame(columns=headers)
    for idx, rrow in enumerate(table.find_all('tr')[1:]):
        rdata = rrow.find_all('td')
        row = [val.text for val in rdata]
        temp_df.loc[idx] = row

    # Concatenate current Dataframe to the general one
    df = pd.concat([df, temp_df], ignore_index=True, copy=False)

# Save data to disk
df[['name', 'gender']].to_excel('raw_data_sample1.xlsx', index=False)
