import tkinter as tk
import psycopg2

app = tk.Tk()
app.title('Промежуточная аттестация. Модуль 2.')
app.geometry('400x500+200+200')


def auth_win():
    win_auth = tk.Toplevel()
    win_auth.title('Окно авторизации')
    win_auth.geometry('400x200+200+200')
    win_auth.grab_set()
    lb_log = tk.Label(win_auth, text='Логин:').pack()
    entry_log = tk.Entry(win_auth).pack()
    lb_pass = tk.Label(win_auth, text='Пароль:').pack()
    entry_pass = tk.Entry(win_auth, show='*').pack()
    but_auth = tk.Button(win_auth, text='Войти').pack(padx=30, pady=15)
    but_auth_can = tk.Button(win_auth, text='Отмена', command=win_auth.destroy).pack(padx=30)

def reg_win():
    win_reg = tk.Toplevel()
    win_reg.title('Окно регистрации')
    win_reg.geometry('400x300+200+200')
    win_reg.grab_set()
    lb_surname = tk.Label(win_reg, text='Фамилия:').pack()
    entry_surname = tk.Entry(win_reg).pack()
    lb_name = tk.Label(win_reg, text='Имя:').pack()
    entry_name = tk.Entry(win_reg).pack()
    lb_patronymic = tk.Label(win_reg, text='Отчество:').pack()
    entry_patronymic = tk.Entry(win_reg).pack()
    lb_log = tk.Label(win_reg, text='Логин:').pack()
    entry_log = tk.Entry(win_reg).pack()
    lb_regpass = tk.Label(win_reg, text='Пароль:').pack()
    entry_regpass = tk.Entry(win_reg).pack()
    but_reg = tk.Button(win_reg, text='Регистрация').pack(padx=30, pady=15)
    but_reg_can = tk.Button(win_reg, text='Отмена', command=win_reg.destroy).pack(padx=30)


button_1 = tk.Button(text='Авторизоваться', bg='#333', fg='#eee', font='18',
                     activebackground='#070', activeforeground='#006',
                     state='normal', command=auth_win)

button_2 = tk.Button(text='Зарегистрироваться', bg='#333', fg='#eee', font='18',
                     activebackground='#070', activeforeground='#006',
                     state='normal', command=reg_win)

quitButton = tk.Button(text='Выход', bg='#333', fg='#eee', font='18', command=app.destroy)


button_1.pack(pady=20)
button_2.pack(pady=2)
quitButton.pack(pady=50)


app.mainloop()