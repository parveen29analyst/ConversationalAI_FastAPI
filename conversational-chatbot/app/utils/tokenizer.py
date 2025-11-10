from typing import List
import re

def tokenize_input(user_input: str) -> List[str]:
    """
    Tokenizes the user input into a list of words.
    This function removes punctuation and splits the input by whitespace.
    """
    # Remove punctuation using regex and split by whitespace
    tokens = re.findall(r'\b\w+\b', user_input.lower())
    return tokens

def detokenize_input(tokens: List[str]) -> str:
    """
    Converts a list of tokens back into a single string.
    """
    return ' '.join(tokens)