

def printgraph(longvector):
    horizontal="-"*37+'\n'
    i=0
    picture=horizontal
    for j in longvector:
        if(i==0):
            picture+='| '+str(j)
            i+=1
        elif(i==8):
            i=0
            picture=picture+' | '+str(j)+' |\n'+horizontal
        else:
            i+=1
            picture=picture+' | '+str(j)
    print(picture)


if __name__=="__main__":
    #given a partially filled out graph of sudoku create a print out of the graph and steps
    longvector=list('.')*81
    longvector[0]=8
    longvector[1]=7
    longvector[2]=6
    longvector[3]=9
    printgraph(longvector)