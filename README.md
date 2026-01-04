# PDF to Images Converter

A simple, user-friendly desktop application that converts PDF files (including password-protected ones) to high-quality PNG images.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

## Features

- **Password-Protected PDF Support** - Easily convert encrypted/password-protected PDFs
- **Customizable DPI** - Choose from 72, 100, 150, 200, or 300 DPI for output quality
- **Batch Conversion** - Converts all pages of a PDF in one go
- **Progress Tracking** - Visual progress bar showing conversion status
- **Auto Output Folder** - Automatically creates an output folder in the same directory as the PDF
- **Cross-Platform** - Works on Windows, macOS, and Linux

## Requirements

- Python 3.7 or higher
- PyMuPDF (fitz)
- Tkinter (usually included with Python)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pdf-to-images-converter.git
cd pdf-to-images-converter
```

### Step 2: Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python pdf_to_images.py
```

### How to Use

1. **Select PDF File** - Click "Browse" to select your PDF file
2. **Enter Password** - If the PDF is password-protected, enter the password (optional for non-encrypted PDFs)
3. **Choose Output Folder** - The output folder is auto-set, but you can change it if needed
4. **Select DPI** - Choose the image quality:
   - `72 DPI` - Screen quality, smallest file size
   - `150 DPI` - Good balance (default)
   - `300 DPI` - Print quality, largest file size
5. **Click "Convert to Images"** - Wait for the conversion to complete

### Output

- Images are saved as PNG files in the selected output folder
- Naming format: `{pdf_filename}_page_001.png`, `{pdf_filename}_page_002.png`, etc.

## Project Structure

```
pdf-to-images-converter/
│
├── pdf_to_images.py      # Main application file
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── LICENSE              # MIT License
└── screenshots/         # Application screenshots
    └── app_screenshot.png
```

## Dependencies

| Package | Version | Description |
|---------|---------|-------------|
| PyMuPDF | >=1.23.0 | PDF rendering and manipulation library |

> **Note:** Tkinter is part of Python's standard library and doesn't need separate installation on most systems. If you encounter issues on Linux, install it using:
> ```bash
> # Ubuntu/Debian
> sudo apt-get install python3-tk
> 
> # Fedora
> sudo dnf install python3-tkinter
> 
> # Arch Linux
> sudo pacman -S tk
> ```

## Building Executable (Optional)

To create a standalone executable that doesn't require Python installation:

### Using PyInstaller

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "PDF-to-Images" pdf_to_images.py
```

The executable will be created in the `dist` folder.

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| "Incorrect password" error | Ensure you're entering the correct PDF password |
| Tkinter not found | Install python3-tk package (see Dependencies section) |
| Permission denied | Run as administrator or check folder write permissions |
| Large file sizes | Use lower DPI settings (72 or 100) |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**MOHAMED SADIQ**

- GitHub: [@killurego19](https://github.com/killurego19)

## Acknowledgments

- [PyMuPDF](https://pymupdf.readthedocs.io/) - For the excellent PDF rendering library
- Python Tkinter - For the GUI framework

---

*In God Alone we trust* 🙏
