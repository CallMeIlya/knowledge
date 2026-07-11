with open("file.txt") as r, open("final.txt", 'a') as w:

    for line in r:
        arr = arr.replace('\t', ' ')
        arr = line.split(" ")

        #print(arr[0].split('\t'))
        
        end = "## "+arr[0]('\t',' ')+"\n"
        #end=end+arr[1].replace('\t', '')

        for i in range(1,len(arr)):
            end=end+" "+arr[i]
        
        #addedLine = f"## {arr[0].split('\t')[0]}\n{arr[0].split('\t')[1]} {end}"
        addedLine=end
        #addedLine.replace('\t', ' ')
        w.write(addedLine)

