import qrcode as qr

image = qr.make(input("Enter the link you want to create QR\n"))
name = input("Enter a name to give name to qr\n")
image.save(name + ".png")
