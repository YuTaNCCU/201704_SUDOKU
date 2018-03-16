import tkinter
root=tkinter.Tk()  #宣告root是類別TK
root.title("SUDOKU Resolve")



#輸入按鈕後執行
def solve_1():
    InputLine=list(range(0,9))
    for i in range(0,9):
        InputLine[i]= entry[i].get() #int()
        print('InputLine',i,'=',InputLine[i])
    
    #2維陣列
    b=[0,0,0,0,0,0,0,0,0]
    c=[]
    Array_1=[]
    for i in range(0,9):
        for j in range(0,9):
            b[j]=int(InputLine[i][j])
        Array_1=Array_1 + b
            
    print('Array_1=\n',Array_1)

    #解數獨
    #for i in range(0,9):
        #for j in range(0,9):
            #if Array_1[i][j] !=0 :
                #for k in range(1,10):




#Entry_1
entry_1=tkinter.Entry(root,width=81,bg='lightskyblue',bd =4)#輸入框
entry_1.pack(side=tkinter.TOP)

#建立 Frame物件1
Frame=list( range(0,9) )
for i in range(0,9): 
    Frame[i]=tkinter.Frame(root)
    Frame[i].pack()
        
#Entry
entry=list( range(0,81) )
for i in range(0,81):
        entry[i]=tkinter.Entry(Frame[int(i/9)],width=1,bg='lightskyblue',bd =3)#輸入框
        entry[i].pack(side=tkinter.LEFT)


def input_1():
 for i in range(0,len(entry_1.get())):
        #顯示數字到表格上
        inputText=entry_1.get()
        entry[i].delete(0,tkinter.END) #END, LEFT, and BOTH all reside in the tkinter namespace
        entry[i].insert(0,inputText[i])
    
#按鈕
Button_1=tkinter.Button(root,text="輸入",command=input_1)
Button_1.pack()

Button_1=tkinter.Button(root,text="解題",command=solve_1)
Button_1.pack()

#主迴圈
root.mainloop  


