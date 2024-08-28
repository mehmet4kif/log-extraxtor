import uuid
import customtkinter as ctk
import os
import json
import re
import threading
from tkinter import filedialog, messagebox
from flask import Flask, render_template, jsonify

app = Flask(__name__)
scanned_results = []
total_files = 0
total_usernames = 0
total_passwords = 0
total_urls = 0

def scan_directory_for_txt_files(dir_path, progress_callback):
    global scanned_results, total_files, total_usernames, total_passwords, total_urls
    results = []

    files = [os.path.join(root, file_name)
             for root, dirs, files in os.walk(dir_path)
             for file_name in files if file_name.endswith('.txt')]

    total_files = len(files)
    if total_files == 0:
        return results

    for index, file_path in enumerate(files):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()

                email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
                pass_pattern = r'(?i)(password|pass|pw|passwd)[\s:]*([^\s]+)'
                url_pattern = r'(https?://[^\s]+|http://[^\s]+)'

                emails = re.findall(email_pattern, content)
                passwords = re.findall(pass_pattern, content)
                urls = re.findall(url_pattern, content)

                for email, password_tuple, url in zip(emails, passwords, urls):
                    if email and password_tuple[1].strip() and url:
                        total_usernames += 1
                        total_passwords += 1
                        total_urls += 1
                        results.append({
                            'file_name': os.path.basename(file_path),
                            'file_path': file_path,
                            'Username': email,
                            'Passw': password_tuple[1].strip(),
                            'URL': url
                        })
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

        progress = (index + 1) / total_files
        progress_callback(progress)

    scanned_results = results

def save_results_to_json(results):
    with open('results.json', 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, indent=4)

    random_file_name = f"results_{uuid.uuid4().hex}.json"
    with open(random_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, indent=4)

@app.route('/')
def index():
    return render_template('index.html', 
                           data=scanned_results, 
                           total_files=total_files, 
                           total_usernames=total_usernames, 
                           total_passwords=total_passwords, 
                           total_urls=total_urls)

@app.route('/data')
def data():
    return jsonify(scanned_results)

class DirectoryScannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Extractor")
        self.geometry("600x350")

        self.label = ctk.CTkLabel(self, text="Dosya Tarayıcı")
        self.label.pack(pady=20)

        self.select_button = ctk.CTkButton(self, text="Klasör Seç", command=self.select_directory)
        self.select_button.pack(pady=10)

        self.scan_button = ctk.CTkButton(self, text="Tara", command=self.start_scan)
        self.scan_button.pack(pady=10)

        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.pack(pady=10, padx=20, fill="x")
        self.progress_bar.set(0) 

        self.progress_label = ctk.CTkLabel(self, text="İlerleme: 0%")
        self.progress_label.pack(pady=10)

        self.directory_path = None

    def select_directory(self):
        self.directory_path = filedialog.askdirectory()
        if self.directory_path:
            self.progress_label.configure(text=f"Seçilen klasör: {self.directory_path}")

    def start_scan(self):
        if self.directory_path:
            scan_thread = threading.Thread(target=self.scan_directory)
            scan_thread.start()
        else:
            messagebox.showerror("Error", "Klasör seçilmedi.")

    def scan_directory(self):
        scan_directory_for_txt_files(self.directory_path, self.update_progress)
        save_results_to_json(scanned_results)
        self.open_web_results()

    def update_progress(self, progress):
        self.progress_bar.set(progress)
        self.progress_label.configure(text=f"İlerleme: {int(progress * 100)}%")
        self.update_idletasks() 

    def open_web_results(self):
        messagebox.showinfo("Info", "Tarama Tamamlandı! Sonuçlar browserda gösterilecektir.")
        os.system("start http://127.0.0.1:5000")  

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(debug=True, use_reloader=False)).start()
    scanner_app = DirectoryScannerApp()
    scanner_app.mainloop()
