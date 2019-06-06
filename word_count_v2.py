with open('in.txt', 'r') as f:
    a = f.read(500)
    list = a.split(' ');
    word_list = filter(None, list)
    for x  in word_list :
        print(x)