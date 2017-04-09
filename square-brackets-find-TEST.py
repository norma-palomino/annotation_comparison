mylist = ['abc123', 'dx1[scope]56', 'gh[scope]9', 'AB33[scope]7', 'aBc654']
#sub = '['

##print "\n".join(s for s in mylist if sub.lower() in s.lower())


##-WORKS
# Returns indices for beginning and end of scope:
def find_brackets_indices(mylist):
    for tweet in mylist:
        if '[' and ']' in tweet:
            str1 = '['
            str2 = ']'
            scope_starts = tweet.find(str1)
            scope_ends = tweet.find(str2)
            #print scope_starts, scope_ends
            scope = tweet[scope_starts : scope_ends +1]
            print scope


scope = find_brackets_indices(mylist)
print scope

        
    





##--WORKS
#def has_brackets(mylist):
    #for var in mylist:
        #if '[' and ']' in var:
            #print var

#scope = has_brackets(mylist)
#print scope
