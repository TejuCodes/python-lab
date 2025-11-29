from datetime import datetime

now = datetime.now()
print("Current Date & Time:", now)
print("Date:", now.date())
print("Time:", now.time())


import os

print("Current Directory:", os.getcwd())
print("Files in Directory:", os.listdir())
os.mkdir("test_folder")    # Creates a folder
print("Folder Created")


import pandas as pd

data = {
    "Name": ["Teju", "Kumar", "Ravi"],
    "Marks": [90, 85, 78]
}

df = pd.DataFrame(data)
print(df)

print("\nAverage Marks:", df["Marks"].mean())
