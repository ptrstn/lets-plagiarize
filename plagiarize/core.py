import deepl


def plagiarize(text, source_language="EN", bypass_languages=["DE", "FR", "RU", "ES"]):
    current_language = source_language
    next_language = bypass_languages[0]
    bypassed_text = text

    for index, bypass_language in enumerate(bypass_languages):
        bypassed_text = deepl.translate(current_language, next_language, bypassed_text)
        if index + 1 < len(bypass_languages):
            current_language = next_language
            next_language = bypass_languages[index + 1]

    return deepl.translate(bypass_languages[-1], source_language, bypassed_text)
