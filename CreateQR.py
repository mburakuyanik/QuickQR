import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=8,
    border=4,
)

qr.add_data(input("Give anything to convert Qr code: "))
qr.make(fit=True)

quickQR = qr.make_image()
quickQR.show()