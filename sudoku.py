import sys

def printgraph(longvector):
    topandbottom=" "*15+'|'+" "*11+"|\n"
    horizontal="   "+"-"*37+'\n'
    modified_horizontal="-"*43+'\n'
    i=0
    k=0
    picture=topandbottom+horizontal
    for j in longvector:
        if(i==0):
            i+=1
            picture+="   | "+str(j)
        elif(i==8):
            i=0
            if(k==2 or k==5):
                picture+=' | '+str(j)+' |\n'+modified_horizontal
            else:
                picture+=' | '+str(j)+' |\n'+horizontal
            k+=1
        else:
            i+=1
            picture+=' | '+str(j)
    picture+=topandbottom
    print(picture)

def isinsquare(number,squarenum,graph): #squarenum = range(9)    //if there is a place to insert number then insert it
    URC=(squarenum//3)*27+(squarenum%3)*3 #UpperRightCorner
    countdots=0
    lastindex=82
    for i in range(3):
        for j in range(3):                     # 0, 3, 6,
            if(graph[URC+(i*9)+j])==number:    # 27, 30, 33,
                return True                    # 54, 57, 60
            if(graph[URC+(i*9)+j])=='.':
                countdots+=1
                lastindex=URC+(i*9)+j
    if(countdots>1):#if there exists more than one place this number can be
        return True
    graph[lastindex]=number
    return False

def isinrow(number,rownum,graph): #rownum is range(9)
    FRN = rownum*9 #First Row Number
    countdots=0
    lastindex=82
    for i in range(9):
        if(graph[FRN+i]==number):
            return True
        if(graph[FRN+i]=='.'):
            countdots+=1
            lastindex=FRN+i
    if(countdots>1):
        return True
    graph[lastindex]=number
    return False

def isincol(number,colnum,graph): #colnum = range(9)
    FCN = colnum #First Column Number
    i=0
    countdots=0
    lastindex=82
    while(i+FCN<81):
        if(graph[i+FCN]==number):
            return True
        if(graph[i+FCN]=='.'):
            countdots+=1
            lastindex=FCN+i
        i+=9
    if(countdots>1):
        return True
    graph[lastindex]=number
    return False

def insertdashhelper(i,graph):
    colnum=i%9
    rownum=i//9
    squarenum=(i//27)*3+(i%9//3)
    FRN = rownum*9
    URC=(squarenum//3)*27+(squarenum%3)*3
    j=0
    while(j+colnum<81):
        if graph[j+colnum]=='.':
            graph[j+colnum]='-'
        j+=9
    for j in range(9):
        if graph[j+FRN]=='.':
            graph[j+FRN]='-'
    for j in range(3):
        for k in range(3):
            if(graph[URC+(j*9)+k]=='.'):
                graph[URC+(j*9)+k]='-'

def insertdash(number,graph): #void function
    didgraphchange=False
    for i in range(len(graph)):
        if graph[i]==number:
            insertdashhelper(i,graph)
    #isincol, isinrow, isinsquare
    truth1=True
    truth2=True
    truth3=True
    i=0
    while i<len(graph):
        if(graph[i]=='.'):
            colnum=i%9
            rownum=i//9
            squarenum=(i//27)*3+(i%9//3)
            truth1=isincol(number,colnum,graph) 
            truth2=isinrow(number,rownum,graph)
            truth3=isinsquare(number,squarenum,graph)
            if(not truth1 or not truth2 or not truth3):
                insertdashhelper(i,graph)
                i=0
                didgraphchange=True
        i+=1
    return didgraphchange

def turnbackdots(graph):
    for i in range(len(graph)):
        if(graph[i]=='-'):
            graph[i]='.'

def solve(graph):
    truth=False
    numvalue=1
    while numvalue < 10:
        truth=insertdash(numvalue,graph)
        turnbackdots(graph)
        if(truth):
            numvalue=0
        numvalue+=1

if __name__=="__main__":
    #given a partially filled out graph of sudoku print solution
    if(len(sys.argv)!=2):
        sys.exit("wrong number of arguments")
    filename=sys.argv[1]
    try:
        file1 = open(filename,'r')
        file1 = file1.read()
        longvector=file1.split(',')
        for i in range(len(longvector)):
            if(longvector[i]>='0' and longvector[i]<='9'):
                longvector[i]=int(longvector[i])
        printgraph(longvector)
        solve(longvector)
        printgraph(longvector)
    except:
        sys.exit("file not found")