import tkinter

Array_1=[[8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 8]]
#inputText='000000000006370048000050009079000015600705000530000760401030000860024500300008000'

#1簡單040250008030409170000081200006000720000604000012000300003810000064902010700045090    
#2簡單010230708000800605009100040090081056000000000540390020020003400904008000301042080
#某許000100000006370048000050009079000015600705000530000760401030000860024500300008000

#讀取
def read(inputText) :
    InputLine=list(range(0,9))
    InputLine[0] = "000100000"
    InputLine[1] = "006370048"
    InputLine[2] = "000050009"
    InputLine[3] = "079000015"
    InputLine[4] = "600705000"
    InputLine[5] = "530000760"
    InputLine[6] = "401030000"
    InputLine[7] = "860024500"
    InputLine[8] = "300008000"

    for i_IL in range(0,9) :
         InputLine[i_IL] = inputText[(i_IL)*9:(i_IL+1)*9]
    #print(inputText)
    ##################
    
    #2維陣列
    b=[0,0,0,0,0,0,0,0,0]
    c=[]
    for i in range(0,9):
        for j in range(0,9):
            Array_1[i][j]=int(InputLine[i][j])
    print('讀取Array_1=\n',Array_1)

def Remain(i,j) :

    RemainList=[0,1,2,3,4,5,6,7,8,9]
    ### 行列中尋找非0
    for i_Remain in range(0,9):
        if Array_1[i_Remain][j] !=0 :   # column中尋找非0
           RemainList[  Array_1[i_Remain][j]  ] =0
        if Array_1[i][i_Remain] !=0 :   # row   中尋找非0
           RemainList[  Array_1[i][i_Remain] ] =0

    ### 宮中尋找非0
    gong_i,gong_j=int(i/3)*3,int(j/3)*3 #找宮的起始
    #print(gong_i ,gong_j,'A')

    for i_gong_i in range(gong_i,gong_i+3) :     #宮中3x3
        for j_gong_j in range(gong_j,gong_j+3) :
            #print(i_gong_i ,j_gong_j)
            if Array_1[i_gong_i][j_gong_j] !=0 :
                RemainList[  Array_1[i_gong_i][j_gong_j]  ] =0
    #print('RemainList=',RemainList)       
    

    ###再用宮摒餘(GBC)法
    
    #1.找宮的起始
    gong_i,gong_j=int(i/3)*3,int(j/3)*3
    
    #2.計算本格可能的數 ex:0100400080 -> 1 4 8
    R_L_C=[0,1,2,3,4,5,6,7,8,9]
    for j_R_L_C in range(0,10) :  #複製 RemainList 到 R_L_C
        R_L_C[j_R_L_C]=RemainList[j_R_L_C]    
    for i_R_L_C in range(R_L_C.count(0)) :
        R_L_C.remove(0)
        #print(rt)
        R_L_C_clr0 = R_L_C
        
    #3.一一嘗試本格可能的數  ex:1 4 8
    for i_R_L_C_clr0 in R_L_C_clr0 :

        #3.1 計算自己宮中，已有解的格子
        GBC3x3=[[0,0,0],[0,0,0],[0,0,0]]
        for i_gong_i in range(gong_i,gong_i+3) :     #宮中3x3
            for j_gong_j in range(gong_j,gong_j+3) :
                if Array_1[i_gong_i][j_gong_j] !=0  :
                    GBC3x3[i_gong_i%3  ][j_gong_j%3]=1       

    
        #3.2計算剩下的格子，是否都不可能放1         
        for i_gong_i in range(gong_i,gong_i+3) :     #宮中3x3
            for j_gong_j in range(gong_j,gong_j+3) :
                
                if i==i_gong_i and j==j_gong_j :   #自己格子不要管
                    a=True
                elif Array_1[i_gong_i][j_gong_j] == 0 : #只管空格
                    for i_Remain in range(0,9):  #行列上只要有 1 ，此格即不可能出現1
                        if Array_1[i_Remain][j_gong_j] == i_R_L_C_clr0 :   # column中尋找非0
                               GBC3x3[i_gong_i%3  ][j_gong_j%3 ]=1
                        if Array_1[i_gong_i][i_Remain] == i_R_L_C_clr0 :   # row   中尋找非0
                               GBC3x3[i_gong_i%3  ][j_gong_j%3 ]=1

                    """  
                    if i==4 and j==1  :
                            print(i_gong_i,j_gong_j,i_R_L_C_clr0,'\n',GBC3x3) """ 

        """ print('GBC3x3=',GBC3x3)""" 

        #3.3計算GBC3x3是否有唯一解了，有就修改RemainList
        a=0
        for i_GBCCC in range(0,3) :
            for j_GBCCC in range(0,3) :
                if GBC3x3[i_GBCCC][j_GBCCC]==1 :
                    a=a+1
            if a==8 :
                answer_GBC3=i_R_L_C_clr0
                RemainList=[0,0,0,0,0,0,0,0,0,0]
                RemainList[ answer_GBC3 ] =answer_GBC3

        
     
                
            
    """ print(RemainList)      """    
    return RemainList
                    
                    



def solve() :
    #解數獨
    for i in range(0,9):
        for j in range(0,9):
            if Array_1[i][j] == 0 :
                """ print('呼喚RemainList')""" 
                RemainList=Remain(i,j)
                if RemainList.count(0)==9 :
                    for k in range(1,10):
                        if RemainList[k]!=0 :
                            answer=RemainList[k]
                            Array_1[i][j]=answer
                            """ print('answer=',answer)""" 


#輸入按鈕後執行
def solve_1():
    #read()

    #計算剩下幾格
    a=0
    for i in range(0,9):
        for j in range(0,9):
            if Array_1[i][j] == 0 :
             a=a+1
    print('剩下',a,'格')

    #主程式
    for i_solve in range(0,17):
        solve()
        
    print('解Array_1=\n',Array_1)


    #計算剩下幾格
    a=0
    for i in range(0,9):
        for j in range(0,9):
            if Array_1[i][j] == 0 :
             a=a+1
    print('剩下',a,'格')

    for i_e_s in range(0,9)  :
        for j_e_s in range(0,9)  :
            i_e_2=i_e_s*9+j_e_s
            entry_2[i_e_2].delete(0,tkinter.END) #END, LEFT, and BOTH all reside in the tkinter namespace
            entry_2[i_e_2].insert(0,Array_1[i_e_s][j_e_s])
            
            entry_2[i_e_2].pack()
    

#視窗
root=tkinter.Tk()  #宣告root是類別TK
root.title("SUDOKU Resolve")

#Entry_0
entry_0=tkinter.Entry(root,width=81,bg='lightskyblue',bd =4)#輸入框
entry_0.pack(side=tkinter.TOP)

#建立 Frame物件1
Frame_1=list( range(0,3) )

Frame_1[0]=tkinter.Frame(root)
Frame_1[0].pack(side=tkinter.LEFT)

Frame_1[1]=tkinter.Frame(root)
Frame_1[1].pack(side=tkinter.RIGHT)

Frame_1[2]=tkinter.Frame(root)
Frame_1[2].pack(side=tkinter.BOTTOM)
    
#建立 Frame物件2
Frame_2=list( range(0,9) )
for i in range(0,9): 
    Frame_2[i]=tkinter.Frame(Frame_1[0])
    Frame_2[i].pack()
                


#建立 Frame物件3
Frame_3=list( range(0,9) )
for i in range(0,9): 
    Frame_3[i]=tkinter.Frame(Frame_1[1])
    Frame_3[i].pack()
        
#Entry1
entry_1=list( range(0,81) )
for i in range(0,81):
        entry_1[i]=tkinter.Entry(Frame_2[int(i/9)],width=1,bg='lightskyblue',bd =3)#輸入框
        entry_1[i].pack(side=tkinter.LEFT)
#Entry2
entry_2=list( range(0,81) )
for i in range(0,81):
        entry_2[i]=tkinter.Entry(Frame_3[int(i/9)],width=1,bg='lightskyblue',bd =3)#輸入框
        entry_2[i].pack(side=tkinter.LEFT)

def input_1():
    for i in range(0,len(entry_0.get())):
        #顯示數字到表格上
        inputText='000000000006370048000050009079000015600705000530000760401030000860024500300008000'
        inputText=entry_0.get()
        
        entry_1[i].delete(0,tkinter.END) #END, LEFT, and BOTH all reside in the tkinter namespace
        entry_1[i].insert(0,inputText[i])
    read(inputText)

    
    
#按鈕
Button_1=tkinter.Button(Frame_1[2],text="輸入",command=input_1)
Button_1.pack()

Button_1=tkinter.Button(Frame_1[2],text="解題",command=solve_1)
Button_1.pack()

#主迴圈
root.mainloop  


