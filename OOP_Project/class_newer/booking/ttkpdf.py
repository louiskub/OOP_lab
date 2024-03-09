import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import requests

class FileDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Downloader")

        self.url_label = ttk.Label(root, text="Enter URL:")
        self.url_entry = ttk.Entry(root, width=40)
        self.download_button = ttk.Button(root, text="Download", command=self.download_file)
        self.progressbar = ttk.Progressbar(root, mode="indeterminate")

        self.url_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.url_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.download_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.progressbar.grid(row=2, column=0, columnspan=2, pady=10)

    def download_file(self):
        url = self.url_entry.get()
        if not url:
            tk.messagebox.showerror("Error", "Please enter a valid URL.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not save_path:
            return  # User canceled the save dialog

        self.progressbar.start()
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            tk.messagebox.showinfo("Success", f"File downloaded successfully to:\n{save_path}")

        except requests.RequestException as e:
            tk.messagebox.showerror("Error", f"Failed to download file.\nError: {e}")

        finally:
            self.progressbar.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileDownloaderApp(root)
    root.mainloop()
