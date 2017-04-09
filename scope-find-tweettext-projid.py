from openpyxl import load_workbook

workbook = load_workbook('./IAA-Scope-Test-Sheet-Full-Only.xlsx')

sheet = workbook['Briana']


##--All these are in the get_excel_data function of get_data_excel program
headers = ["str_id", "project_id", "tweet_text", "label"]


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

##--End get_excel_data

##--These two functions get the tweet_text and proj_id and then find the scope
        
# Returns tweet text only
def find_tweet_text(excel_data):
    tuple_tweet_projid = []
    for row_data in excel_data:
        tweet = row_data['tweet_text'], row_data['project_id']
        tuple_tweet_projid.append(tweet)
    return tuple_tweet_projid


#this line should be after  __main__
tuple_tweet_projid = find_tweet_text(excel_data)
#print tuple_tweet_projid

#find scope of negation, between [ ]
def find_scope(tuple_tweet_projid):    
    # retrieve the tweet_text only, firts element in the tuple:
    scope_output = []
    for tweet in tuple_tweet_projid:
        # separate tweet text only

        tweet_text = tweet[0] 

        # ignore tweets with value None, i.e. at end of the list
        if tweet_text != None:

            #find the scope marks( [ ] ):
            if '[' and ']' in tweet_text:
                str1 = '['
                str2 = ']'
                scope_starts = tweet_text.find(str1)
                scope_ends = tweet_text.find(str2)
                    #print scope_starts, scope_ends
                scope = tweet_text[scope_starts : scope_ends +1]
                #print scopes
                proj_id = tweet[1]
                #print proj_id
                scope_with_projid = proj_id, scope#.encode('utf-8')
        scope_output.append(scope_with_projid)                
    return scope_output
                    



#this line should be after  __main__
scope_found = find_scope(tuple_tweet_projid)
print scope_found




