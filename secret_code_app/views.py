import base64
from io import BytesIO
import qrcode
from django.shortcuts import render
from django.utils import timezone

# Function to generate QR code image
def generate_qr_code(message):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    # Base64 encode the image
    qr_code_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
    return qr_code_base64

# Caesar Cipher for encoding/decoding
def encode_message(message, shift=3):
    result = ""
    for char in message:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

def decode_message(encoded_message, shift=3):
    return encode_message(encoded_message, -shift)

# View for handling encoding, decoding and displaying QR code
def home(request):
    encoded_message = ''
    decoded_message = ''
    time_sent = ''
    qr_code_img = None

    if request.method == 'POST':
        message = request.POST.get('message', '')
        if 'encode' in request.POST:
            encoded_message = encode_message(message)
            qr_code_img = generate_qr_code(encoded_message)
            time_sent = timezone.now()
        elif 'decode' in request.POST:
            decoded_message = decode_message(message)

    return render(request, 'home.html', {
        'encoded_message': encoded_message,
        'decoded_message': decoded_message,
        'qr_code_img': qr_code_img,
        'time_sent': time_sent,
    })
