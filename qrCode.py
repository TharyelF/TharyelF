link = input("link: ")

madlib = f"{link}"

print(madlib)

import qrcode 
data = madlib = f"{link}"
qr = qrcode.QRCode(version = 4, 
                   box_size = 20, 
                   border = 2) 
qr.add_data(data) 
  
qr.make(fit = True) 
img = qr.make_image(fill_color = 'black', 
                    back_color = 'White') 
  
img.save('qrCode.jpg')