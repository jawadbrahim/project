import json
import os
import shutil
import pytesseract
from pdf2image import convert_from_path
from project.feature.auth.config.jwthelper import Config
from project.helpers.date import DateHelper
from project.helpers.jwt import JwtHelper
import uuid
from project.feature.auth.data_classes import AuthCreated
from .abstraction import AbstractionAuthService
from ..exception import PhoneNumberExist

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

class Default(AbstractionAuthService):
    def __init__(self, data_access):
        self.data_access = data_access
        self.date_helper = DateHelper()
        self.jwt = JwtHelper(Config.JWT_SECRET, Config.JWT_SIGN_ALGORITHM)
        
    def generate_token(self):
        token_id = uuid.uuid4()
        exp = self.date_helper.get_expiration_date(Config.JWT_DURATION)
        payload = {
            'token_id': str(token_id),
            'exp': exp
        }
        token_str = self.jwt.encode(payload)
        self.data_access.insert_token(token_id, token_str)
        return token_id, token_str

    def save_phone_numbers_to_file(self, phone_number, replied_phone_number):
        base_directory = 'phone_numbers'
        phone_number_directory = os.path.join(base_directory, phone_number)
        os.makedirs(phone_number_directory, exist_ok=True)
        
        
        index_file_path = os.path.join(phone_number_directory, 'index.json')
        pdf_source_path = r'C:/Python/chatbot/docs/New Text Document (1).pdf'
        pdf_target_path = os.path.join(phone_number_directory, 'jawad')
        
        
        pdf_text = self.extract_text_with_ocr(pdf_source_path)
        
        
        data = {
            'pdf_content': pdf_text
        }
        
        try:
            with open(index_file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error saving index.json: {e}")
        
        
        self.copy_pdf(pdf_source_path, pdf_target_path)

    def extract_text_with_ocr(self, pdf_path):
        try:
            if not os.path.exists(pdf_path):
                raise FileNotFoundError(f"PDF file not found: {pdf_path}")

            images = convert_from_path(pdf_path)
            text = ""
            for image in images:
                page_text = pytesseract.image_to_string(image, lang='ara')
                text += page_text + "\n"
            return text
        except Exception as e:
            print(f"Error extracting text with OCR: {str(e)}")
            return ""

    def copy_pdf(self, source_path, target_path):
        try:
            shutil.copy(source_path, target_path)
            print(f"PDF copied from {source_path} to {target_path}")
        except IOError as e:
            print(f"Error copying PDF: {e}")

    def auth(self, phone_number, replied_phone_number):
        number_exist = self.data_access.number_exists(phone_number)
        if number_exist:
            raise PhoneNumberExist(phone_number=phone_number)
        
        auth = self.data_access.create_auth(phone_number, replied_phone_number)
        token_id, token_str = self.generate_token()
        self.data_access.update_token_id(auth.id, token_id)
        self.save_phone_numbers_to_file(phone_number, replied_phone_number)
        return AuthCreated(
            id=auth.id,
            phone_number=auth.phone_number,
            replied_phone_number=auth.replied_phone_number,
            token=token_str,
            created_at=auth.created_at
        )
