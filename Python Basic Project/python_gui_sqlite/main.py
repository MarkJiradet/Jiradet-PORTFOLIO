# นำเข้าโมดูล tkinter สำหรับสร้าง GUI และ sqlite3 สำหรับจัดการฐานข้อมูล
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# สร้างคลาส LibraryApp เพื่อสร้างและจัดการแอปพลิเคชัน
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.resizable(False, False)

        # เชื่อมต่อกับฐานข้อมูล SQLite และสร้างเคอร์เซอร์
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        
        # สร้างและปรับแต่งวิดเจ็ต
        self.create_widgets()
        self.style_widgets()
    
    # จัดการปรับแต่งสไตล์ของวิดเจ็ต
    def style_widgets(self):
        # Font ทั้งหมด
        font_default = ("Tahoma", 12)
        font_label = ("Tahoma", 12)
        
        # ตั้งค่าฟอนต์
        for child in self.root.winfo_children():
            if isinstance(child, (tk.Label, tk.Entry, tk.Button)):
                child.configure(font=font_default)
            if isinstance(child, tk.Label):
                child.configure(font=font_label)
        
        # ปรับปุ่ม
        style = ttk.Style()
        style.configure("TButton", font=font_default, padding=5)
        style.configure("TLabel", background="#f0f0f0", font=font_label)
        style.configure("TEntry", font=font_default, padding=5)

        # ปรับ Treeview
        style.configure("Treeview", font=font_default)
        style.configure("Treeview.Heading", font=font_label)

        # ปรับพื้นหลัง
        self.root.configure(bg="#f0f0f0")
        for child in self.root.winfo_children():
            if isinstance(child, tk.Label):
                child.configure(bg="#f0f0f0")

        # เพิ่ม padding
        for child in self.root.winfo_children():
            child.grid_configure(padx=10, pady=5)

    # ฟังก์ชันนี้สร้างวิดเจ็ตในหน้าต่าง เช่น ปุ่ม, ช่องข้อความ, และรายการหนังสือ
    def create_widgets(self):
        tk.Label(self.root, text="ชื่อหนังสือ : ").grid(row=0, column=0, sticky="e")
        tk.Label(self.root, text="ชื่อผู้แต่ง : ").grid(row=1, column=0, sticky="e")
        
        self.title_var = tk.StringVar()
        self.author_var = tk.StringVar()
        self.title_entry = tk.Entry(self.root, textvariable=self.title_var, width=50)
        self.title_entry.grid(row=0, column=1,sticky="w")
        self.author_entry = tk.Entry(self.root, textvariable=self.author_var, width=50)
        self.author_entry.grid(row=1, column=1,sticky="w")

        self.books_listbox = ttk.Treeview(self.root, columns=("Book ID", "Title", "Author", "Status"))
        self.books_listbox.grid(row=3, column=0, columnspan=2)
        self.books_listbox.heading("Book ID", text="ลำดับหนังสือ")
        self.books_listbox.heading("Title", text="ชื่อหนังสือ")
        self.books_listbox.heading("Author", text="ชื่อผู้แต่ง")
        self.books_listbox.heading("Status", text="สถานะ")
        
        tk.Label(self.root, text="ชื่อผู้ยืม : ").grid(row=4, column=0, sticky="e")
        tk.Label(self.root, text="เบอร์โทรศัพท์ : ").grid(row=5, column=0, sticky="e")
        
        self.borrower_name_var = tk.StringVar()
        self.borrower_phone_var = tk.StringVar()
        self.borrower_name_entry = tk.Entry(self.root, textvariable=self.borrower_name_var, width=50)
        self.borrower_name_entry.grid(row=4, column=1,sticky="w")
        self.borrower_phone_entry = tk.Entry(self.root, textvariable=self.borrower_phone_var, width=50)
        self.borrower_phone_entry.grid(row=5, column=1,sticky="w")

        self.borrowers_listbox = ttk.Treeview(self.root, columns=("Borrower ID", "Name", "Phone Number", "Book ID"))
        self.borrowers_listbox.grid(row=8, column=0, columnspan=2)
        self.borrowers_listbox.heading("Borrower ID", text="ลำดับผู้ยืม")
        self.borrowers_listbox.heading("Name", text="ชื่อผู้ยืม")
        self.borrowers_listbox.heading("Phone Number", text="เบอร์โทรศัพท์")
        self.borrowers_listbox.heading("Book ID", text="ลำดับหนังสือ")
    
        tk.Button(self.root, text="เพิ่มหนังสือ", command=self.add_book).grid(row=2, column=0, sticky="e")
        tk.Button(self.root, text="แก้ไขหนังสือ", command=self.edit_book).grid(row=2, column=1, sticky="w")

        tk.Button(self.root, text="ยืมหนังสือ", command=self.borrow_book).grid(row=6, column=0, sticky="e")
        tk.Button(self.root, text="คืนหนังสือ", command=self.return_book).grid(row=6, column=1, sticky="w")

        self.display_borrowers()
        self.display_books()

    # ฟังก์ชันนี้ใช้เพิ่มหนังสือใหม่เข้าสู่ฐานข้อมูล
    def add_book(self):
        title = self.title_var.get()
        author = self.author_var.get()
        if title and author:
            try:
                self.cursor.execute("INSERT INTO Books (title, author) VALUES (?, ?)", (title, author))
                self.conn.commit()
                self.display_books()
                self.title_var.set('')
                self.author_var.set('')
                messagebox.showinfo("สำเร็จ", "เพิ่มหนังสือสำเร็จ!")
            except Exception as e:
                messagebox.showerror("ล้มเหลว", str(e))
        else:
            messagebox.showerror("ล้มเหลว", "ต้องระบุชื่อหนังสือและชื่อผู้แต่ง!")
    
    # ฟังก์ชันนี้ให้ผู้ใช้ยืมหนังสือ โดยเปลี่ยนสถานะของหนังสือและเพิ่มข้อมูลผู้ยืม
    def borrow_book(self):
        selected_book = self.books_listbox.selection()
        if selected_book:
            book_id, _, _, status = self.books_listbox.item(selected_book)["values"]

            if status == "Borrowed":
                messagebox.showerror("ล้มเหลว", "หนังสือถูกยืมแล้ว!")
                return

            borrower_name = self.borrower_name_var.get()
            borrower_phone = self.borrower_phone_var.get()
            if borrower_name and borrower_phone:
                try:
                    self.cursor.execute("INSERT INTO Borrowers (name, phone_number, book_id) VALUES (?, ?, ?)", 
                                        (borrower_name, borrower_phone, book_id))
                    self.cursor.execute("UPDATE Books SET status='Borrowed' WHERE book_id=?", (book_id,))
                    self.conn.commit()
                    self.display_books()
                    self.display_borrowers()
                    self.borrower_name_var.set('')
                    self.borrower_phone_var.set('')
                    messagebox.showinfo("สำเร็จ", "ยืมหนังสือสำเร็จ!")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("ล้มเหลว", "ต้องระบุชื่อผู้ยืมและเบอร์โทรศัพท์!")
        else:
            messagebox.showerror("ล้มเหลว", "กรุณาเลือกหนังสือที่ต้องการจะยืม!")

    # ฟังก์ชันนี้ให้ผู้ใช้คืนหนังสือ โดยลบข้อมูลผู้ยืมและเปลี่ยนสถานะหนังสือ
    def return_book(self):
        selected_borrower = self.borrowers_listbox.selection()
        if selected_borrower:
            borrower_id, _, _, book_id = self.borrowers_listbox.item(selected_borrower)["values"]
            try:
                self.cursor.execute("DELETE FROM Borrowers WHERE borrower_id=?", (borrower_id,))
                self.cursor.execute("UPDATE Books SET status='Available' WHERE book_id=?", (book_id,))
                self.conn.commit()
                self.display_books()
                self.display_borrowers()
                messagebox.showinfo("สำเร็จ", "คืนหนังสือสำเร็จ!")
            except Exception as e:
                messagebox.showerror("ล้มเหลว", str(e))
        else:
            messagebox.showerror("ล้มเหลว", "กรุณาเลือกผู้ยืมที่ต้องการจะคืน!")

    # ฟังก์ชันนี้ให้ผู้ใช้แก้ไขรายละเอียดหนังสือ
    def edit_book(self):
        selected_book = self.books_listbox.selection()
        if not selected_book:
            messagebox.showerror("ล้มเหลว", "กรุณาเลือกหนังสือที่ต้องการแก้ไข!")
            return
        
        book_id, title, author, status = self.books_listbox.item(selected_book)["values"]
        
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"แก้ไข {title}")

        tk.Label(edit_window, text="ชื่อหนังสือ : ").grid(row=0, column=0)
        tk.Label(edit_window, text="ชื่อผู้แต่ง : ").grid(row=1, column=0)

        title_var = tk.StringVar(value=title)
        author_var = tk.StringVar(value=author)
        title_entry = tk.Entry(edit_window, textvariable=title_var).grid(row=0, column=1)
        author_entry = tk.Entry(edit_window, textvariable=author_var).grid(row=1, column=1)

        def update_book():
            try:
                self.cursor.execute("UPDATE Books SET title=?, author=? WHERE book_id=?", (title_var.get(), author_var.get(), book_id))
                self.conn.commit()
                self.display_books()
                edit_window.destroy()
                messagebox.showinfo("สำเร็จ", "แก้ไขข้อมูลสำเร็จ!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(edit_window, text="", command=update_book).grid(row=2, column=0, columnspan=2)
    
    # แสดงรายการหนังสือทั้งหมดจากฐานข้อมูล
    def display_books(self):
        records = self.cursor.execute("SELECT * FROM Books").fetchall()
        self.books_listbox.delete(*self.books_listbox.get_children())
        for record in records:
            self.books_listbox.insert("", "end", values=record)
            
    # แสดงรายการผู้ยืมทั้งหมดจากฐานข้อมูล
    def display_borrowers(self):
        records = self.cursor.execute("SELECT * FROM Borrowers").fetchall()
        self.borrowers_listbox.delete(*self.borrowers_listbox.get_children())
        for record in records:
            self.borrowers_listbox.insert("", "end", values=record)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
