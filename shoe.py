from tkinter import *

def extract():
        query=str(input('What shoes are you looking for? '))
        if query=='X':
                exit(0)
        q=query.split(' ')
        q_brand=q[0]
        q_name=q[1]
        
        f=open('shoe.txt','r')
        content=f.read()
        arr=content.split(',')
        for i in range(0,len(arr)):
                if '\n' in arr[i]:
                        new=arr[i].split('\n')
                        arr[i]=new[1]

        for i in range(0,len(arr)):
                if arr[i]==q_brand and arr[i+1]==q_name:
                        shoe=(arr[i],arr[i+1], arr[i+2], arr[i+3], arr[i+4], arr[i+5], arr[i+6], arr[i+7])
                        return shoe

def display(shoe):
        root=Tk()
        root.title('Query Results')

        drop=int(shoe[2])-int(shoe[3])

        Label(root,text=shoe[0]+' '+shoe[1]).pack()
        Label(root,text='Heel to toe drop: '+str(drop)+'mm ('+shoe[2]+'-'+shoe[3]+')').pack()
        Label(root,text='These '+shoe[4]+' are made for '+shoe[5]+' events/workouts').pack()
        Label(root,text='Spikes: '+shoe[6]).pack()
        Label(root,text='Comments: '+shoe[7]).pack()

        root.mainloop()

while True:
        display(extract())
