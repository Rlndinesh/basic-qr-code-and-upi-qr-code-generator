#pip install qrcode
import qrcode as qr
# img=qr.make("https://github.com/Rlndinesh")
# img.save("github_profile.png")

img1=input("Enter link")
image=qr.make(img1)
image.save('img.png')
