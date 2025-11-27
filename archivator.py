import os;
import tkinter as tk;
from tkinter import filedialog, messagebox
from tkinter.ttk import Entry, Button, Frame;
import shutil;
import threading;

def create_zip(folder, subfolder):
    shutil.make_archive(os.path.join(folder, subfolder), 'zip', os.path.join(folder, subfolder));
    messagebox.showinfo("Архивирирование папки", f"{subfolder} заархивирована")



def select_folder():
    folder = filedialog.askdirectory();

    if len(folder) >0:
        ed_fld_name.delete(0, tk.END);
        ed_fld_name.insert(0, folder);

def archivate_fld():
    fld_name = ed_fld_name.get().strip();
    if len(fld_name) == 0:
        messagebox.showerror("Ошибка", "Папка не выбрана");
        return;

    if not os.path.exists(fld_name):
        messagebox.showerror("Ошибка", "Такая папка не найдена");
        return;
    #Папка выбрана и даже существует. теперь получим ее субдиректории
    nest_items = os.listdir(fld_name);
    #messagebox.showinfo("nest_items", str(nest_items));
    sub_folders = [];
    for item in nest_items:
        if os.path.isdir(os.path.join(fld_name, item)):
            sub_folders.append(item);
            #messagebox.showinfo("Вложенные папки", str(sub_folders));
    #Список вложенных папок мы получили, теперь начнем архивировать
    if len(sub_folders) == 0:
        messagebox.showinfo("Вложенные папки", "Вложенных папок нет")
        return;
    #теперь можно архивировать
    for sub_folder in sub_folders:
        #create_zip(fld_name, sub_folder);
        zip_thread = threading.Thread(target=create_zip, args = (fld_name, sub_folder));
        zip_thread.start();


if __name__=='__main__':
    root = tk.Tk()
    root.title("Архивирование")
    root.resizable(True, True)

    # Рамка всередині вікна
    frame = Frame(root, padding=12)
    frame.pack(fill="both", expand=True)
    #--------------------------------------------------------------------------
    #тут создадим 2 кнопки и редактор типа однострочное текстовое поле
    ed_fld_name = Entry(frame, justify='center', width=50);
    ed_fld_name.grid(row=0,column=0,columnspan=2,padx=5,pady=5);
    #2 кнопки снизу
    bt_sel_folder = Button(frame,text="Выбор папки",command=select_folder);
    bt_sel_folder.grid(row=1,column=0,padx=5,pady=5);
    #далее кнопка архивировать
    bt_arch_execute = Button(frame, text = "Архивировать", command = archivate_fld);
    bt_arch_execute.grid(row=1,column=1,padx=5,pady=5);
    #--------------------------------------------------------------------------
    root.mainloop();


