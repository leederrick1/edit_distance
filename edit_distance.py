def get_back(rows, cols):
    matrix = []
    for i in range(len(rows)+1):
        sub = []
        for j in range(len(cols)+1):
            sub.append('0')
        matrix.append(sub)
    for j in range(1,len(cols)+1):
        matrix[0][j] = 'l'
    for i in range(1,len(rows)+1):
        matrix[i][0] = "u"
    matrix[0][0] = "finish"
    return matrix

def getAlignedSequences(x, y, matrix, traceBack):
    xSeq = []
    ySeq = []
    i = len(x)
    j = len(y)
    while(i > 0 or j > 0):
        if traceBack[i][j] == 'd':
            xSeq.append(x[i-1])
            ySeq.append(y[j-1])
            i = i-1
            j = j-1
        elif traceBack[i][j] == 'l':
            xSeq.append('-')
            ySeq.append(y[j-1])
            j = j-1
        elif traceBack[i][j] == 'u':
            xSeq.append(x[i-1])
            ySeq.append('-')
            i = i-1
        elif traceBack[i][j] == 'finish':
            break
    return xSeq,ySeq
def edit_distance(word1, word2):
    #we need to build the matrix
    rows = len(word1) +1
    cols = len(word2) +1
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    trace = get_back(word1,word2)
    
    for i in range(1,rows):
        for j in range(1,cols):
            left = matrix[i][j-1] + 1 
            up = matrix[i-1][j] + 1
            diag = matrix[i-1][j-1]
            if word1[i-1] == word2[j-1]:
                matrix[i][j] = diag
            else:
                matrix[i][j] = min(left,up,diag+1)    
            if matrix[i][j] == left:
                trace[i][j] = 'l'
            elif matrix[i][j] == up:
                trace[i][j] = 'u'
            else:
                trace[i][j] = 'd'




    #used for printing matrix to command line
    if rows > cols:
        size = cols
    else:
        size = max(rows, cols)
    print("   ", end="")
    for i in range(size):
        print(i, end="    ")
    print("\n", end = "")
    print("   ", end="")
    for i in range(size):
        print("-----", end="") 
    print("\n", end = "")          
    for i in range(0 , rows):
        print(i, end=' | ')
        for j in range(0, cols):
            print(matrix[i][j], end="  : ")
        print("\n")
    print("The edit distance is: ", matrix[rows-1][cols-1])
    #used for print the global alignment
    for i in trace:
        print(i)
    word1, word2 = getAlignedSequences(word1, word2, matrix, trace)
    word1 = word1[::-1]
    word2 = word2[::-1]
    print(*word1)
    print(*word2)
    
             
