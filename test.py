def blyat(string:str,splitter=' '):
    s = []
    gay = ''
    for i in string:
        if i == splitter:
            s.append(gay)
            gay = ''
        else:
            gay += i
    s.append(gay)
    print(s)

blyat('What are you doing')