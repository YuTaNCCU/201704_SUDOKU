Array_1=[[8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8]]
 
#讀取
def read() :
    InputLine=list(range(0,9))
    InputLine[0] = "002030800"
    InputLine[1] = "039500070"
    InputLine[2] = "800000063"
    InputLine[3] = "000060090"
    InputLine[4] = "300129008"
    InputLine[5] = "090080000"
    InputLine[6] = "970000001"
    InputLine[7] = "080003920"
    InputLine[8] = "003040500"
    
    #2維陣列
    b=[0,0,0,0,0,0,0,0,0]
    c=[]
    for i in range(0,9):
        for j in range(0,9):
            Array_1[i][j]=int(InputLine[i][j])
    print('讀取Array_1=\n',Array_1)

def Remain(i,j) :

    RemainList=[0,1,2,3,4,5,6,7,8,9]
    for i_Remain in range(0,9):
        if Array_1[i_Remain][j] !=0 :   # column中尋找非0
           RemainList[  Array_1[i_Remain][j]  ] =0
        if Array_1[i][i_Remain] !=0 :   # row   中尋找非0
           RemainList[  Array_1[i][i_Remain] ] =0

    # 宮中尋找非0
    gong_i,gong_j=int(i/3)*3,int(j/3)*3 #找宮的起始
    #print(gong_i ,gong_j,'A')

    for i_gong_i in range(gong_i,gong_i+3) :     #宮中3x3
        for j_gong_j in range(gong_j,gong_j+3) :
            #print(i_gong_i ,j_gong_j)
            if Array_1[i_gong_i][j_gong_j] !=0 :
                RemainList[  Array_1[i_gong_i][j_gong_j]  ] =0
    #print('RemainList=',RemainList)       
    return RemainList


def solve() :
    #解數獨
    for i in range(0,9):
        for j in range(0,9):
            if Array_1[i][j] == 0 :
                #print('呼喚RemainList')
                RemainList=Remain(i,j)
                if RemainList.count(0)==9 :
                    for k in range(1,10):
                        if RemainList[k]!=0 :
                            answer=RemainList[k]
                            Array_1[i][j]=answer
                            #print('answer=',answer)

    

read()

for i_solve in range(0,20):
    solve()
    
print('解Array_1=\n',Array_1)












