pos_values = ('this', 'DT') ("'prediction", 'NN') ("'", "''") ('moving', 'VBG') ('forward', 'RB') ('is', 'VBZ') ('seldom', 'RB') ('100', 'CD') ('%', 'NN')


for elem in pos_values:
    pos_tag = [tag[0] for tag in tweet_tokens]
    print(*pos_tag)