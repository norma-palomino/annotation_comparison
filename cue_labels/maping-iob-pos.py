

TI_TEXT=  "It's a sin to fxck up a great song by Sam &amp; Dave \"Thank You\" so bad [I barely recognized it]!"
TI =  ["it's", 'a', 'sin', 'to', 'fxck', 'up', 'a', 'great', 'song', 'by', 'sam', '&', 'dave', '"', 'thank', 'you', '"', 'so', 'bad', '[', 'i', 'barely', 'recognized', 'it]', '!']
TI_IOB=  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B', 'C', 'I', 'I', 'O']
TI_POS=  ['L', 'D', 'N', 'P', 'V', 'T', 'D', 'A', 'N', 'P', '^', '&', '^', ',', 'V', 'O', ',', 'R', 'A', ',', 'O', 'R', 'V', 'O', ',']



iob_pos = []
for elem1, elem2 in zip(TI_IOB, TI_POS):
    #print(elem1, elem2)
    both = elem1+'_'+elem2
    #print(both)
    iob_pos.append(both)
print(iob_pos)
