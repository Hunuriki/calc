import tkinter

def click():
    print("多分正常に動いています")
def destroy():
    root.destroy()
def delete_label():
    la.place_forget()
def get_entry():
    entry.get()
def calc():
    a = int(entry.get())
    sum_squares = 0
    b = 2
    for i in range(a):
        sum_squares = sum_squares + pow(i+1, b)
    print(round(sum_squares,3))    

#計算結果
la = tkinter.Label(text = int(sum_squares))
la.place(x = 110, y=20)

#入力欄を作ってる

root = tkinter.Tk()
root.geometry("260x160")
root.title("Test_form")

entry = tkinter.Entry(root, width=3)
entry.place(x = 110, y = 40)

#ボタンを作ってる（２つ）

button_1 = tkinter.Button(text="計算")
button_2 = tkinter.Button(text="閉じる")

button_1.pack()
button_1.grid(row = 0, column = 0)
button_1.place(x = 130, y = 80)

button_2.pack()
button_2.grid(row = 0, column = 0)
button_2.place(x = 90, y = 80)

button_1["command"] = get_entry
button_1["command"] = calc
button_1["command"] = delete_label
button_2["command"] = destroy

root.mainloop()