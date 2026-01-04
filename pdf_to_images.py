"""
PDF to Images Converter
Converts each page of a PDF (including password-protected) to separate images.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import fitz  # PyMuPDF
from pathlib import Path
import os


class PDFToImagesConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to Images Converter")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        self.pdf_path = None
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # PDF File Selection
        ttk.Label(main_frame, text="PDF File:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        file_frame = ttk.Frame(main_frame)
        file_frame.grid(row=0, column=1, sticky=tk.EW, pady=5)
        
        self.file_entry = ttk.Entry(file_frame, width=35)
        self.file_entry.pack(side=tk.LEFT, padx=(0, 5))
        
        browse_btn = ttk.Button(file_frame, text="Browse", command=self.browse_pdf)
        browse_btn.pack(side=tk.LEFT)
        
        # Password Input
        ttk.Label(main_frame, text="Password:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.password_entry = ttk.Entry(main_frame, width=35, show="*")
        self.password_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Show/Hide Password
        self.show_password_var = tk.BooleanVar()
        show_password_cb = ttk.Checkbutton(
            main_frame, 
            text="Show password", 
            variable=self.show_password_var,
            command=self.toggle_password_visibility
        )
        show_password_cb.grid(row=2, column=1, sticky=tk.W)
        
        # Output Directory
        ttk.Label(main_frame, text="Output Folder:").grid(row=3, column=0, sticky=tk.W, pady=5)
        
        output_frame = ttk.Frame(main_frame)
        output_frame.grid(row=3, column=1, sticky=tk.EW, pady=5)
        
        self.output_entry = ttk.Entry(output_frame, width=35)
        self.output_entry.pack(side=tk.LEFT, padx=(0, 5))
        
        output_btn = ttk.Button(output_frame, text="Browse", command=self.browse_output)
        output_btn.pack(side=tk.LEFT)
        
        # DPI Setting
        ttk.Label(main_frame, text="Image DPI:").grid(row=4, column=0, sticky=tk.W, pady=5)
        
        dpi_frame = ttk.Frame(main_frame)
        dpi_frame.grid(row=4, column=1, sticky=tk.W, pady=5)
        
        self.dpi_var = tk.StringVar(value="150")
        dpi_combo = ttk.Combobox(dpi_frame, textvariable=self.dpi_var, width=10, state="readonly")
        dpi_combo['values'] = ('72', '100', '150', '200', '300')
        dpi_combo.pack(side=tk.LEFT)
        
        ttk.Label(dpi_frame, text="(Higher = better quality, larger files)").pack(side=tk.LEFT, padx=10)
        
        # Convert Button
        convert_btn = ttk.Button(main_frame, text="Convert to Images", command=self.convert_pdf)
        convert_btn.grid(row=5, column=0, columnspan=2, pady=20)
        
        # Status Label
        self.status_var = tk.StringVar(value="Select a PDF file to begin")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, foreground="gray")
        status_label.grid(row=6, column=0, columnspan=2)
        
        # Progress Bar
        self.progress = ttk.Progressbar(main_frame, length=400, mode='determinate')
        self.progress.grid(row=7, column=0, columnspan=2, pady=10)
    
    def browse_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if file_path:
            self.pdf_path = file_path
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
            
            # Auto-set output directory to same folder as PDF
            output_dir = str(Path(file_path).parent / "pdf_images")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, output_dir)
            
            self.status_var.set("PDF selected. Enter password if required.")
    
    def browse_output(self):
        folder_path = filedialog.askdirectory(title="Select Output Folder")
        if folder_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, folder_path)
    
    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
    
    def convert_pdf(self):
        # Validate inputs
        pdf_path = self.file_entry.get().strip()
        if not pdf_path:
            messagebox.showerror("Error", "Please select a PDF file.")
            return
        
        if not os.path.exists(pdf_path):
            messagebox.showerror("Error", "PDF file not found.")
            return
        
        output_dir = self.output_entry.get().strip()
        if not output_dir:
            messagebox.showerror("Error", "Please select an output folder.")
            return
        
        password = self.password_entry.get()
        dpi = int(self.dpi_var.get())
        
        try:
            # Create output directory
            os.makedirs(output_dir, exist_ok=True)
            
            # Open PDF
            self.status_var.set("Opening PDF...")
            self.root.update()
            
            doc = fitz.open(pdf_path)
            
            # Try to decrypt if password provided
            if doc.is_encrypted:
                if not password:
                    messagebox.showerror("Error", "This PDF is password-protected. Please enter the password.")
                    doc.close()
                    return
                
                if not doc.authenticate(password):
                    messagebox.showerror("Error", "Incorrect password.")
                    doc.close()
                    return
            
            total_pages = len(doc)
            self.progress['maximum'] = total_pages
            self.progress['value'] = 0
            
            # Get PDF filename without extension for naming images
            pdf_name = Path(pdf_path).stem
            
            # Convert each page
            zoom = dpi / 72  # 72 is the default DPI
            matrix = fitz.Matrix(zoom, zoom)
            
            for page_num in range(total_pages):
                self.status_var.set(f"Converting page {page_num + 1} of {total_pages}...")
                self.root.update()
                
                page = doc.load_page(page_num)
                pix = page.get_pixmap(matrix=matrix)
                
                # Save as PNG
                output_path = os.path.join(output_dir, f"{pdf_name}_page_{page_num + 1:03d}.png")
                pix.save(output_path)
                
                self.progress['value'] = page_num + 1
                self.root.update()
            
            doc.close()
            
            self.status_var.set(f"Done! {total_pages} images saved to output folder.")
            messagebox.showinfo("Success", f"Successfully converted {total_pages} pages to images!\n\nSaved to:\n{output_dir}")
            
        except Exception as e:
            self.status_var.set("Error occurred during conversion.")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")


def main():
    root = tk.Tk()
    app = PDFToImagesConverter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
