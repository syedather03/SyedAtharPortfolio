
import qrcode
from PIL import Image

Logo_link='Facebook_f_logo_(2019).png'

logo= Image.open(Logo_link)

basewidth=100

wpercent=(basewidth/float(logo.size[0]))
hsize=int((float(logo.size[1])*float(wpercent)))
logo=logo.resize((basewidth,hsize),Image.ANTIALIAS)
QRcode=qrcode.QRcode(error_correction=qrcode.constants.ERROR_CORRECT_H)

url="https://www.facebook.com/Syed.Athar1251/"

QRcode.add_data(url)

QRcode.make()

QRcolor='00BFFF'

QRimg=QRcode.make_image(
    fill_color=QRcolor,back_color="white").convert('RGB')

pos=((QRimg.size[0]-logo.size[0])//2,
        (QRimg.size[1]-logo.size[1])//2)

QRimg.paste(logo,pos)

QRimg.save('FC.png')

print("QRcode Generated")