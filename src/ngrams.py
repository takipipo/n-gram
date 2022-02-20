from typing import List, Tuple


def ngrams(list_of_tokens: List[str], n: int) -> List[Tuple]:
    return list(zip(*[list_of_tokens[i:] for i in range(n)]))
