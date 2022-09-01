#### pip install pyqrcode 
import pyqrcode
# pip install pypng
import png
# link variable
link = "https://github.com/saqibb/python/"
# Create Link qrcode
qrCode = pyqrcode.create(link)
# convert to png
qrCode.png("link.png",scale=5)
