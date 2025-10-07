import os;
import byllm;
import google.genai;

glob llm = byllm.Model(model_name=os.getenv("JAC_MODEL", "gemini-2.5-flash"));

def generate_password() -> str by llm();

sem generate_password = """
Generate a strong password (>=12 chars) with upper, lower, digit, and symbol.
""";

with entry {
    print(generate_password());
}

