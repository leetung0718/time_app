import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.config(font=("Arial", int(window.winfo_width() / 8)))
    time_label.after(1000, update_time)

# 建立視窗
window = tk.Tk()
window.title("時間小工具")

# 建立時間標籤
time_label = tk.Label(window, font=("Arial", 80))
time_label.pack(fill=tk.BOTH, expand=True)

# 更新時間
update_time()

# 執行視窗主迴圈
window.mainloop()