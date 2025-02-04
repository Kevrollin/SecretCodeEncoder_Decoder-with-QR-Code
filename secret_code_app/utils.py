import qrcode
from io import BytesIO
import base64

def encode_message(message):
    """Encodes a message using base64 and generates a QR code."""
    encoded_message = base64.b64encode(message.encode()).decode()
    
    # Generate QR Code
    qr = qrcode.make(encoded_message)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_data = base64.b64encode(buffer.getvalue()).decode()
    
    return encoded_message, qr_data

def decode_message(encoded_message):
    """Decodes a base64 encoded message."""
    try:
        decoded_message = base64.b64decode(encoded_message).decode()
        return decoded_message
    except Exception:
        return "Invalid encoded message!"
