# Project Synopsis: Static Quick Response (QR) Code Generator

**Student Name:** Preetham  
**Project Title:** Static Quick Response (QR) Code Generator  
**Programming Language:** Python & JavaScript  

---

## 1. Project Overview
The **Static QR Code Generator** is a dual-platform utility designed to encode personal and institutional information into high-quality Quick Response (QR) codes. The project provides both a **Desktop Application** (built with Python) and a **Modern Web Application** (built with HTML, CSS, and JS). It allows for the integration of custom branding (logos) and provides a unique "Student ID Badge" mode for institutional use.

## 2. Objectives
*   To create a user-friendly interface for generating static QR codes.
*   To implement data validation for critical fields like Email and Phone numbers using Regular Expressions (Regex).
*   To allow professional branding by embedding custom logos within the QR code.
*   To provide cross-platform accessibility via a live web deployment and a local desktop tool.

## 3. Technology Stack
### A. Desktop Application (Python)
*   **GUI Framework:** Tkinter (for the windowing system).
*   **Imaging Library:** Pillow (PIL) for image processing and logo overlay.
*   **QR Logic:** `qrcode` library for high-speed encoding.
*   **Data Validation:** `re` (Regular Expressions) for input sanitization.

### B. Web Application (Frontend)
*   **Styling:** Vanilla CSS3 with **Glassmorphism** aesthetics.
*   **Logic:** Modern JavaScript (ES6+).
*   **Graphics:** HTML5 Canvas API for real-time logo merging.
*   **Icons:** Lucide-React icon set for a premium UI feel.
*   **Deployment:** GitHub Pages for global accessibility.

## 4. Key Features
*   **Multi-Field Encoding:** Stores Name, Student ID, Phone, Email, Location, and Custom Messages.
*   **Institutional ID Mode:** A specialized view that generates a vertical Student ID Badge template with the QR code embedded.
*   **Custom Branding:** Automatically overlays a developer logo (`logo.png`) in the center of the QR code using error correction (Level H).
*   **Dark/Light Mode:** Dynamic theme switching for better user experience.
*   **Instant Export:** Ability to save generated codes as high-resolution PNG files for printing or digital sharing.

## 5. Software Requirements
*   **Operating System:** Windows/macOS/Linux.
*   **Python Version:** Python 3.10 or higher.
*   **Web Browser:** Any modern browser (Chrome, Edge, Firefox).
*   **Libraries:** `qrcode`, `Pillow`.

## 6. Conclusion
This project successfully demonstrates the fusion of data encoding and modern UI design. By providing both a local script and a live web server, it ensures high utility for both developers and non-technical users in a school or college environment.

---
**GitHub Repository:** [https://github.com/preethamamin22/-Code-Generator](https://github.com/preethamamin22/-Code-Generator)  
**Live Demo:** [https://preethamamin22.github.io/-Code-Generator/](https://preethamamin22.github.io/-Code-Generator/ )
