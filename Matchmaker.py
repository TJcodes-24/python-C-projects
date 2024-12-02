#Matchmaking code: This code will pull in data from a google forms query stored in google sheets and rank the answers of people's responses on the form. 
#I will need to determine how to properly store these files on github

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from client_search import client_search

#Call in the file via API
# Step 1: Authenticate using the JSON key file
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("tj-codes-24-matchmaker-0dc7c583a4a7.json", scope)
client = gspread.authorize(credentials)

# Step 2: Open the Google Sheet
sheet = client.open("Queer Women Matchmaking Questionnaire (Responses)").worksheet("Form Responses 1")  # Call to read from the sheet

# Step 3: Fetch data from the sheet
data = sheet.get_all_records()  # Returns a list of dictionaries, one per row
#row11 = sheet.cell(4,4).value
rowlength= len(data)
columnlength = 39
#Store the main person's info in comparison strings
# Assignnment of the clien'ts info to compare
name_to_search = input("What is the client's name?") # Replace with the name you want to search for
client_info, row_index = client_search(name_to_search, data)
if client_info:
    print("Client found at row index:", row_index)
    print("Client details:", client_info)

print(client_info['  What age range are you looking for in a match?  '])



#compare the mains person's lifestyle and values 0-8
#compare their interest & hobbies (9-14)
#compare their personality & preferences (14-18)
#compare their romantic & dating preferences (19-23)
#compare their quirks & fun (24-30)
#compare their astrology - return a score (31-34)
#provide their compatibility score with each person and select the highest score (35-38)
