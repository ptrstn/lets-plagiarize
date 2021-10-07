import deepl


def plagiarize(text, source_language="EN", bypass_language="DE"):
    translated_text = deepl.translate(source_language, bypass_language, text)
    return deepl.translate(bypass_language, source_language, translated_text)
