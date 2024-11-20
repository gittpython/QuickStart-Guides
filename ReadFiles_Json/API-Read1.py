import requests
import pandas as pd
from icecream import ic

# Step 1: Fetch data from API
url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)
data = response.json()

# Step 2: Parse the data into a DataFrame
'''df = pd.DataFrame(data)'''

# Step 3: Save the DataFrame to a spreadsheet
'''df.to_excel('output.xlsx', index=False)'''

# Step 4: Save the data to a text file
documents_folder = os.path.join(os.path.expanduser('~'), 'Downloads', 'API_Output') 
os.makedirs(documents_folder, exist_ok=True) 
text_file_path = os.path.join(documents_folder, 'output.txt') 
with open(text_file_path, 'w') as file: 
    file.write(str(data))


print("Data has been saved to 'output.xlsx' and 'output.txt'")
