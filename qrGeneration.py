#pip install qrcode
import qrcode

img = qrcode.make('https://github.com/TheoV22/qrcode')

img.save('filename.png')


