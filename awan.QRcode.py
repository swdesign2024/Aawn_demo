import qrcode

# الرابط المراد تحويله
url = "https://swdesign2024.github.io/Aawn_demo/"

# إنشاء كائن الـ QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# إضافة البيانات
qr.add_data(url)
qr.make(fit=True)

# إنشاء الصورة (يمكنك تغيير الألوان هنا)
img = qr.make_image(fill_color="black", back_color="white")

# حفظ الصورة باسم معين
img.save("Aawn_QR.png")

print("تم إنشاء رمز QR بنجاح وحفظه باسم Aawn_QR.png")