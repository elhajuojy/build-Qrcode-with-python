import pyqrcode
import qrcode
from qrcode import QRCode
link= "https://www.facebook.com/SouiriMehdi/"
url=pyqrcode.create(link)
url.png("mehdi.png",scale=6)
