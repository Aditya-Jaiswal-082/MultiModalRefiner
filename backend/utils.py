def is_irrelevant_input(text: str) -> bool:
    irrelevant_keywords = ["hi", "hello", "how are you", "joke", "funny"]
    return any(word in text.lower() for word in irrelevant_keywords)
