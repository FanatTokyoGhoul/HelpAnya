import qrcode

def generate_qr(data, path='.', file_name = "qr.png"):
    img = qrcode.make(data)
    img.save(path + "/" + file_name)

