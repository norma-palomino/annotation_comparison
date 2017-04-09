from __future__ import division

import nltk

annot1 = [(500, u'[they seldom desire anything unless it belongs to others]')]
annot2 = [500, u'[they seldom desire anything (unless it belongs to others!)]']


def scope_match(annot1, annot2):
    tokens1 = annot2[1].strip('[]')  # str(annot2[1])
    #print type(tokens1)
    tokens2 = nltk.word_tokenize(tokens1)
    print('these are my tokens: ', tokens2)


        # print [a[1].strip('[]').encode('utf-8').split() for a in annot1]
        # for part in annot1:
        # briana_string = part[1]
        # print briana_string
        # briana = annot1[1]
        # briana_string = ', '.join([repr(x) for x in annot1[1]]) #''.join(briana)
        # print 'briana join:', briana_string
        ##briana_no_left_bracket= briana_string.replace("[","")
        ###print 'without [:', briana_no_left_bracket
        ##briana_no_right_bracket = briana_no_left_bracket.replace("]","")
        ###print 'without [] :', briana_no_right_bracket
        ##briana_clean = briana_no_right_bracket
        ##print briana_clean


        # norma = annot2[1]
        # norma_string = ''.join(norma)

        # print norma_string
        ##norma_no_left_bracket= norma_string.replace("[","")
        ###print 'without [:', briana_no_left_bracket
        ##norma_no_right_bracket = norma_no_left_bracket.replace("]","")
        ###print 'without [] :', norma_no_right_bracket
        ##norma_clean = norma_no_right_bracket
        ##print norma_clean



        # briana_set = set(briana_string.split(' '))
        # print 'briana split: ', briana_set

        # norma_set = set(norma_string.split(' '))
        ##print 'norma split: ', norma2

        # matched = briana_set.intersection(norma_set)
        # unmatched = briana_set.symmetric_difference(norma_set)
        ##print 'matched tokens list: ', list(matched)
        ##print 'unmatched token list: ', list(unmatched  )

        # if unmatched >0:
        # print 'Proj Id:', annot1[0], 'Partial scope match', 'Unmatched tokens: ', list(unmatched)
        # elif matched>0:
        # print  'Proj Id:', annot1[0], 'Strict scope match'


scope_agr = scope_match(annot1, annot2)
print(scope_agr)
