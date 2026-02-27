# Static QR Code Generator & ID Badge Pro 🚀

A premium, dual-platform QR Code generation utility designed for students and developers. This project features a modern **Web Application** with glassmorphism design and a robust **Python Desktop Tool**.

![Project Preview](https://img.shields.io/badge/Status-Live-success)
![Technology](https://img.shields.io/badge/Tech-Python%20%7C%20JS%20%7C%20CSS-blue)

## 🌐 Live Demo
Check out the live web application here: 
**[https://preethamamin22.github.io/-Code-Generator/](https://preethamamin22.github.io/-Code-Generator/)**

---

## ✨ Features

### 💻 Web Application (Vite + JS)
- **Glassmorphism UI**: Beautiful frosted-glass aesthetic with smooth transitions.
- **ID Badge Mode**: Toggle to a vertical Student ID card view with embedded QR code.
- **Logo Integration**: Automatically centers a professional developer logo in the QR.
- **Theme Switcher**: Supports both high-tech Dark Mode and clean Light Mode.
- **High-Res Export**: Download your QR codes as PNG files instantly.

### 🖥️ Desktop Application (Python + Tkinter)
- **Secure Encoding**: Encodes Name, ID, Phone, Email, and Branch details.
- **Input Validation**: Uses Regex to ensure valid emails and 10-digit phone numbers.
- **Responsive Design**: The background and UI elements scale with the window size.
- **Professional Branding**: Embedded logo support using Pillow's LANCZOS resampling.

---

## 🛠️ Installation & Setup

### 1. Web Version
To run the web app locally for development:
```bash
cd QRcodeWebApp
npm install
npm run dev
```

### 2. Desktop Version
Ensure you have Python installed, then install the dependencies:
```bash
pip install qrcode[pil] Pillow
python QRcodeGen.py
```

---

## 🎨 Project Structure
- `index.html`: Main web structure.
- `style.css`: Modern glassmorphism styling.
- `script.js`: Core QR generation and UI logic.
- `QRcodeGen.py`: Fixed and optimized Python script.
- `logo.png`: Custom branding asset.
- `Project_Synopsis.md`: Comprehensive formal document for school submission.

---

## 👨‍💻 Developer
Developed by **Preetham** for school project submission.

---

## 📜 License
This project is open-source and available under the MIT License.
