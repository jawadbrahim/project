import json
import os
import pytesseract
from openai import OpenAI
from project.config.development import Development
from .abstraction import AbstractionService
from ..excpetions import WrongQuestion
import tiktoken
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

class Default(AbstractionService):
    def __init__(self, data_access):
        self.data_access = data_access
        self.client = OpenAI(api_key=Development.API_KEY)
        self.index_file = r"C:/Python/chatbot/phone_numbers/7163114/index.json"

    def count_tokens(self, text, model='gpt-3.5-turbo'):
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))

    def calculate_token_cost(self, prompt, response):
        input_tokens = self.count_tokens(prompt)
        output_tokens = self.count_tokens(response)
        
        cost_per_1k_input = 0.0015  
        cost_per_1k_output = 0.002  
        
        token_cost = (input_tokens * cost_per_1k_input / 1_000) + (output_tokens * cost_per_1k_output / 1_000)
        return token_cost

    def Create_Qa(self, question, answer, phone_number, token, replied_phone_number):
       
        
      
        qa = self.data_access.Create_Qa(
            question=question,
            answer=answer,
            token_cost=self.calculate_token_cost(question, answer),
            phone_number=phone_number, 
            token=token,
            replied_phone_number=replied_phone_number
        )

        if not qa:
            raise WrongQuestion(question=question)
        return qa

    def query_openai(self, prompt, texts):
        context = "\n\n".join(texts)
        full_prompt = (f"Context:\n{context}\n\n"
                       f"Based on the above context from the PDF, answer the following question. "
                       f"Do not provide any information that is not present in the context.\n\n"
                       f"User Question:\n{prompt}")

        print("Full Prompt:", full_prompt)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": full_prompt}]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"

    def chatbot(self, question, phone_number, token, replied_phone_number):
     if not os.path.exists(self.index_file) or os.path.getsize(self.index_file) == 0:
        return f"Index file not found or empty: {self.index_file}"

     try:
        with open(self.index_file, 'r', encoding='utf-8') as f:
            index_data = json.load(f)
            texts = [index_data.get('pdf_content', '')]
     except json.JSONDecodeError:
        return "Error reading index.json: Invalid JSON format."

     response = self.query_openai(question, texts)
    # Pass the additional required arguments
     self.Create_Qa(question, response, phone_number, token, replied_phone_number)
     return response

