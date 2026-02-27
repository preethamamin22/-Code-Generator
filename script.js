const qrForm = document.getElementById('qr-form');
const qrContainer = document.getElementById('qrcode');
const canvasContainer = document.getElementById('qr-canvas-container');
const emptyState = document.getElementById('empty-state');
const btnSave = document.getElementById('btn-save');

let finalCanvas = null;

qrForm.addEventListener('submit', function(e) {
    e.preventDefault();

    // 1. Gather Data
    const data = {
        name: document.getElementById('name').value,
        id: document.getElementById('student_id').value,
        phone: document.getElementById('phone').value,
        email: document.getElementById('email').value,
        location: document.getElementById('location').value,
        branch: document.getElementById('branch').value,
        message: document.getElementById('message').value
    };

    // Format string similar to Python version
    const qrData = `Name: ${data.name}\nID: ${data.id}\nPhone: ${data.phone}\nEmail: ${data.email}\nLoc: ${data.location}\nBranch: ${data.branch}\nMsg: ${data.message}`;

    // 2. Clear previous
    qrContainer.innerHTML = '';
    
    // 3. Generate QR
    const qrcode = new QRCode(qrContainer, {
        text: qrData,
        width: 256,
        height: 256,
        colorDark: "#ff0000", // Red color as requested in original requirements
        colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.H
    });

    // 4. Wait for QR to be rendered then add logo
    setTimeout(() => {
        const qrImage = qrContainer.querySelector('img');
        const qrCanvas = qrContainer.querySelector('canvas');
        
        // Use canvas if available, otherwise image
        const source = qrCanvas || qrImage;
        
        createFinalImage(source);
    }, 100);
});

function createFinalImage(qrSource) {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = 300;
    canvas.height = 300;

    // Fill white background
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw QR Code
    ctx.drawImage(qrSource, 22, 22, 256, 256);

    // Load and Draw Logo (vishal.png -> logo.png)
    const logo = new Image();
    logo.src = 'logo.png';
    
    logo.onload = () => {
        const logoSize = 60;
        const x = (canvas.width - logoSize) / 2;
        const y = (canvas.height - logoSize) / 2;
        
        // Draw white border for logo
        ctx.fillStyle = "white";
        ctx.fillRect(x - 2, y - 2, logoSize + 4, logoSize + 4);
        
        ctx.drawImage(logo, x, y, logoSize, logoSize);
        
        finalizePreview(canvas);
    };

    logo.onerror = () => {
        console.warn("Logo not found, proceeding without it.");
        finalizePreview(canvas);
    };
}

function finalizePreview(canvas) {
    finalCanvas = canvas;
    
    // Show UI
    canvasContainer.classList.add('visible');
    emptyState.style.display = 'none';
    btnSave.disabled = false;
    
    // Add to container (replace previous)
    qrContainer.innerHTML = '';
    qrContainer.appendChild(canvas);
}

btnSave.addEventListener('click', () => {
    if (!finalCanvas) return;
    
    const link = document.createElement('a');
    link.download = 'QR_Code_Vishal.png';
    link.href = finalCanvas.toDataURL('image/png');
    link.click();
});
