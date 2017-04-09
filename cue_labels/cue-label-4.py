#this coding returns the IOBs for one tweet only

from __future__ import division
import re
import nltk
#from nltk.tokenize import TweetTokenizer
from Tokenizer import tokenize
from openpyxl import load_workbook
import Config
import csv
from TextInstance import TextInstance


def find_IOBs(doc):
    IOB_output = []
    # tknzr = TweetTokenizer()
    # tokenize doc.text from docs
    tokens = tokenize(doc)
    #print('THIS IS TOKENS: ', tokens)

    # go over tokens, generating IOB and omitting [ ]
    # status is out, begin or in
    status = 'out'
    for token in tokens:
        #print(token)
        if status == 'out' and token != '[':
            IOB_output.append('O')
            continue
        if status == 'out' and token == '[':
            status = 'begin'
            continue
        if status == 'begin' and token != '/':
            IOB_output.append('B')
            status = 'in'
            continue
        if status == 'begin' and token == '/':
            status = 'cue'
            continue
        if status == 'cue' and token != '~':
            IOB_output.append('C')
            continue
        if status == 'cue' and token == '~':
            status = 'in'
            continue
        if status == 'in' and token != ']' and token !='/':
            IOB_output.append('I')
            continue
        if status == 'in' and token != ']' and token =='/':
            status = 'cue'
            continue
        if status == 'in' and token == ']':
            status = 'out'
    return IOB_output


def get_labeled_docs(gold_csv="gold.csv"):
    path = "data/" + gold_csv
    print('File:', path)
    csv_reader = csv.DictReader(open(path, 'rU', encoding="latin-1"), delimiter=',')
    labeled_docs = []

    for line in csv_reader:
        #print('Line:', line)
        instance_id = line['project_id']
        text = line['tweet_text']
        # TODO:  save the Date field
        label = line['label']
        
        if label in Config.code_book:
            doc = TextInstance(instance_id, text)
            doc.label = label
            #creating the text line that will be passed through tokenize(docs) in Tokenizer.py
            doc.text = text
            labeled_docs.append(doc)
            
        else:
            print("post: " + instance_id + " label: " + label)

    # adds tokens and pos tags
    labeled_docs = tokenize(labeled_docs)
    return labeled_docs



if __name__ == '__main__':
    docs = get_labeled_docs(Config.labeled_csv)
    #print("total instances: ", len(docs))
    IOBs = find_IOBs(docs)
    #print('this is IOBs: ', IOBs)
    #print('this is docs: ', docs)



    # workbook = load_workbook('./TweetsForTestingScopeCueProgram.xlsx')
    # sheet1 = workbook['Sheet1']
    # sheet_data = get_excel_data(sheet1)
    # tweet_list = []
    # for d in sheet_data:
    #     just_text = d['tweet_text']
    #     #print('This is "just_text" type: ', type(just_text))   
    #     #print('This is just_text: ', just_text.encode('utf-8'))     
    #     tweet_list.append(just_text)
    #     IOB_tokens = find_IOBs(just_text.encode('utf-8'))
    #     print('this is IOBs: ', IOB_tokens)



# getting data from an excel file, Max'es approach:
# def get_excel_data(sheet):
#     headers = ['str_id', 'project_id', 'tweet_text', 'label']
#     excel_data = []  # list of dictionaries ##NAME OF LIST of dict
#     for row_num, row in enumerate(sheet):
#         if row_num is 0:  # skip the first row (don't want headers)
#             continue
#         row_data = {}  # open a dictionary ##NAME OF DICTIONARY OF VALUES IN EACH ROW
#         for col_num, cell in enumerate(
#                 row):  # populating the dictionary with header names as keys and cell content as values# populating the dictionary with header names as keys and cell content as values
#             if col_num > len(headers) - 2: 
#                 continue
#             key = headers[col_num]
#             value = cell.value
#             #print('This is "cell.value" type: ', type(value)) #--> 'value' is a str
#             row_data[key] = value
#             #print('This is "row_data[key]" value: ', type(row_data[key]))
#         excel_data.append(row_data)  # adding each key-value pair to the excel_data list
#     #print('this is excel data', excel_data)
#     #print('This is excel_data`s type: ', type(excel_data))
#     return excel_data