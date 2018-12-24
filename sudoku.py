

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


if __name__=="__main__":
    #given a partially filled out graph of sudoku create a print out of the graph and steps
    longvector=list('.')*81
    longvector[0]=8
    longvector[1]=7
    longvector[2]=6
    longvector[3]=9
    longvector[10]=1
    longvector[14]=6
    longvector[19]=4
    longvector[21]=3
    longvector[23]=5
    longvector[24]=8
    longvector[27]=4
    longvector[33]=2
    longvector[34]=1
    longvector[37]=9
    longvector[39]=5
    longvector[46]=5
    longvector[49]=4
    longvector[51]=3
    longvector[53]=6
    longvector[55]=2
    longvector[56]=9
    longvector[62]=8
    longvector[65]=4
    longvector[66]=6
    longvector[67]=9
    longvector[69]=1
    longvector[70]=7
    longvector[71]=3
    longvector[77]=1
    longvector[80]=4
    printgraph(longvector)