import tkinter as tk
from tkinter import messagebox

def say_hello():
    messagebox.showinfo("인사말", "안녕하세요, 김선태님! 반가워요!")

# 메인 윈도우 생성
root = tk.Tk()
root.title("Golden Nova Hello App")
root.geometry("300x200")

# 중앙 배치를 위한 프레임
frame = tk.Frame(root)
frame.pack(expand=True)

# 버튼 생성
hello_button = tk.Button(
    frame, 
    text="클릭해보세요!", 
    command=say_hello,
    padx=20,
    pady=10,
    bg="#4CAF50",
    fg="white",
    font=("Malgun Gothic", 12, "bold")
)
hello_button.pack()

# 실행
root.mainloop()
