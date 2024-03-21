import re
from collections import Counter

def contar_palavras(texto):
    palavras = re.findall(r'\b\w+\b', texto.lower())
    return Counter(palavras)
