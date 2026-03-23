from kiwipiepy import Kiwi

kiwi = Kiwi()

def correct_text(text: str) -> dict:
    corrected = kiwi.space(text, reset_whitespace=False)

    return {
        "original": text,
        "corrected": corrected,
        "changed": text != corrected,
    }
