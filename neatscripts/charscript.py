with open("file.txt") as r, open("final.txt", 'a') as w:

    for line in r:
        arr = line.split(" ")

        #print(arr[0].split('\t'))
        
        end = ""
        for i in range(1,len(arr)):
            end=end+" "+arr[i].replace('\t', ' ')
        #print(end)
        #print(end.encode().hex())
        #print(arr[0].split('\t'))
        #print(arr)
        addedLine = f"## {arr[0].split('\t')[0]}\n{arr[0].split('\t')[1]} {end}"
        w.write(addedLine)
        #print(arr)

