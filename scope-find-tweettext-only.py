from openpyxl import load_workbook

workbook = load_workbook('./HardlyFull.xlsx')

sheet = workbook['HardlyFull']


headers = ["StrId", "Id", "Text", "Label"]


excel_data = []

for row_num, row in enumerate(sheet):
    # skip the first row (don't want headers)
    if row_num is 0:
        continue
    #open a dictionary
    row_data = {}
    # populating the dictionary with header names as keys and cell content as values
    for col_num, cell in enumerate(row):
        if col_num > len(headers) - 1:
            continue
        key = headers[col_num]
        value = cell.value
        row_data[key] = value
    # adding each key-value pair to the excel_data list
    excel_data.append(row_data)
    
#print excel_data

##--WORKS
#def find_tweet_text(excel_data):
    #for row_data in excel_data:
        #print row_data['Text']
        
# Returns tweet text only
def find_tweet_text(excel_data):
    listoftweets = []
    for row_data in excel_data:
        tweet = row_data['Text']
        listoftweets.append(tweet)
    return listoftweets


listoftweets = find_tweet_text(excel_data)
print listoftweets

def find_brackets_indices(listoftweets):
    for tweet in listoftweets:
        if '[' and ']' in tweet:
            str1 = '['
            str2 = ']'
            scope_starts = tweet.find(str1)
            scope_ends = tweet.find(str2)
            #print scope_starts, scope_ends
            scope = tweet[scope_starts : scope_ends +1]
            print scope


scope = find_brackets_indices(listoftweets)
print scope
