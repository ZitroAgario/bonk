lol=input("file name pls:");
with open(lol, 'r+') as myfile:
    file=myfile.read().replace('\n', ' ') 
    list = file.split();
    g='';
    while g!='done':
        g=input("Guest name");
        list.append(g.upper());
    list=list[:-1]
    list.sort();
    myfile.write('\n'.join(list));
    print(list);
    myfile.close();
