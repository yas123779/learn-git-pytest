def reverse_string(s: str) -> str:
    return s[::-1]

def count_vowels(s: str) -> int:
    return sum(1 for char in s.lower() if char in "aeiou")

def is_palindrome(s: str) -> bool:
    normalized = s.replace(" ", "").lower()
    return normalized == normalized[::-1]

def capitalize_words(s: str) -> str:
    return ' '.join(word.capitalize() for word in s.split())
