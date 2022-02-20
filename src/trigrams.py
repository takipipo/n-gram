from typing import List, Tuple


def trigrams(list_of_tokens: List[str]) -> List[Tuple[str, str, str]]:
    return list(zip(list_of_tokens, list_of_tokens[1:], list_of_tokens[2:]))
