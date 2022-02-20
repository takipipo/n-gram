from typing import List, Tuple


def bigrams(list_of_tokens: List[str]) -> List[Tuple[str, str]]:
    return list(zip(list_of_tokens, list_of_tokens[1:]))
