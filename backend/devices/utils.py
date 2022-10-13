import base64
from io import BytesIO
from uuid import uuid4
import string
import numpy as np
import cv2
from django.core.files.base import ContentFile


def decode_base64_to_numpy(str: str) -> np.ndarray:
    """
    Decode a base64 string to a numpy array.
    From Openchaver/image_utils/encoder.py
    """
    return cv2.imdecode(np.frombuffer(base64.b64decode(str), np.uint8), -1)

def deobfuscate_text(text:str) -> str:
    # From Openchaver/models.py
    a = string.ascii_letters
    b = string.ascii_letters[-1] + string.ascii_letters[:-1]
    table = str.maketrans(b, a)
    return text.translate(table)

def numpy_to_content_file(img: np.ndarray) -> ContentFile:
    """
    Convert a numpy array to a content file.
    """
    # Save cv image to buffer
    buffer = BytesIO()
    img_bytes = cv2.imencode(".png", img)[1]
    buffer.write(img_bytes)
    buffer.seek(0)
    return ContentFile(buffer.getvalue(), name=f'{uuid4().hex}.png')

