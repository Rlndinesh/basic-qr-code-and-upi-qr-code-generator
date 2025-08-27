import qrcode as qr
# import pil 
#upi id
upi_id=input("Enter your UPI ID: ")

#UPI QR format
#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# merchent_code=input()

#defing the payment url based on the UPI ID and the payment app


# phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc={merchent_code}'


phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR codes for each payment app

phonepe_qr=qr.make(phonepe_url)
paytm_qr=qr.make(paytm_url)
google_qr=qr.make(google_pay_url)

#saving the QR CODE to image file 

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_qr.save('google_pay_qr.png')

#Displaying the QR codes (I'm using PIL/Pillow library)

phonepe_qr.show()
# paytm_qr.show()
# google_qr.show()
