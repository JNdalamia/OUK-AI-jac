import random;
import os;
import dotenv;
import from byllm.llm { Model }

# glob llm = Model(model_name="gpt-4o",verbose=False);
 glob llm = Model(model_name="gemini/gemini-2.0-flash", verbose=False);

def poem (topic: str) -> str by llm(topic);

walker llm_poet {
    has topic: str;
    has poem: str;

    can start with `root entry;
    can create_poem with turn entry

node turn {
        has poem = llm(topic);
        report poem;
    }
}

with entry {
    spawn llm_poet with {topic: "A serene landscape with mountains"}
}