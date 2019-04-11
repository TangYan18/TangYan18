# 该程序示例标准计算器(pack+frame方式)

import tkinter as tk # 导入Python标准GUI界面模块

root = tk.Tk()  # 创建根窗口
root.title("计算器")

displayFrame = tk.Frame(root)
formula = tk.StringVar()
formula1=tk.StringVar()
outputentry = tk.Entry(displayFrame, textvariable=formula1, font = ('Helvetica', 24), justify = tk.RIGHT, relief = tk.SOLID)
outputentry.pack(side=tk.TOP, expand = tk.YES, fill = tk.BOTH)
inputentry=tk.Entry(displayFrame, textvariable=formula, font = ('Helvetica', 24), justify = tk.RIGHT, relief = tk.SOLID)
inputentry.pack(expand = tk.YES, fill = tk.BOTH)
displayFrame.pack(side=tk.TOP, expand = tk.YES, fill = tk.BOTH)
boardFrame = tk.Frame(root)

def f(x,y):
    return x.set(''),y.set('')
def cal(x,y,key):
    return y.set(y.get()+x.get()+key),x.set('')
def result(x,y):
    try:
        return y.set(y.get()+x.get()),y.set(eval(y.get())),x.set('')
    except:
        return y.set('表达式错误'),x.set('')
    
keys = [['CE', 'C', 'DEL', '/'], ['7','8','9', '*'], ['4', '5', '6', '-'], ['1', '2', '3', '+'], ['+/-', '0', '.', '=']]
for line in keys:
    lineFrame = tk.Frame(boardFrame)
    for key in line:
        if '0'<=key<='9' or key == '.':
            tk.Button(lineFrame, text=key, command = lambda x=formula, k=key: x.set(x.get()+k), width=8, font=('Verdana', 16)).pack(side=tk.LEFT)
        elif key=='C' or key =='CE':
            tk.Button(lineFrame, text=key, command = lambda x=formula,y=formula1,k=key:f(x,y), width = 8, font=('Verdana', 16)).pack(side=tk.LEFT)
        elif key=='+' or key=='-' or key=='*' or key=='/' :
            tk.Button(lineFrame, text=key, command = lambda x=formula,y=formula1,k=key: cal(x,y,key=k), width = 8, font=('Verdana', 16)).pack(side=tk.LEFT)
        elif key == '+/-': # 负号
            tk.Button(lineFrame, text=key, command = lambda x=formula, k=key: x.set('-'+x.get()), width=8, font=('Verdana', 16)).pack(side=tk.LEFT)
        elif key=='DEL' :
            tk.Button(lineFrame, text=key, command = lambda x=formula, k=key: x.set(x.get()[:-1]), width = 8, font=('Verdana', 16)).pack(side=tk.LEFT)
        elif key == '=':
            tk.Button(lineFrame, text=key, command = lambda x=formula, y=formula1: result(x,y), width = 8, font=('Verdana', 16)).pack(side=tk.LEFT)
    lineFrame.pack(side=tk.TOP)
boardFrame.pack(side=tk.TOP)
tk.mainloop()