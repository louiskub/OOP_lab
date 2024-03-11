import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)

# Data to be encoded in the QR code
data = "Why U Scan kub!"

# Add data to the QR code instance
qr.add_data(data)
qr.make(fit = True)

# Create an image from the QR code instance
img = qr.make_image(fill_color = "darkblue", back_color = "white")

# Save the image or display it
img.save("my_qr_code.png")
img.show()
