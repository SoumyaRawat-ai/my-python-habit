import qrcode

# Create a QR code
img = qrcode.make("Certificate No. - 293202552176 Name - PRINCE SHARMA  Event - TYPE KAR JEET JA-DHAROHAR")

# Save the QR code as an image file
#                             change the file name
img.save("D:/Downloads/qrcode2.png")
