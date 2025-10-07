# import google.generativeai as genai

#     # Configure your API key
# genai.configure(api_key="AIzaSyAGRLovmdfyHFV-OlCyCD2ZAxW59lirI1M")

# for m in genai.list_models():
#         if "generateContent" in m.supported_generation_methods:
#             print(m.name)

# import os
# import byllm

# MODEL_NAME = 'gemini-flash-latest'
# llm = byllm.Model(model_name=os.getenv("JAC_MODEL", "gemini/gemini-2.5-flash"))

# def generate_password():
#     prompt = "Generate a strong password (>=12 chars) with upper, lower, digit, and symbol."
#     return llm(prompt)

# if __name__ == "__main__":
#     print(generate_password())

