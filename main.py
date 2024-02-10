from googletrans import Translator


def translate_to_english(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


def main():
    indic_text_input = input("Enter text in an Indic language: ")

    english_translation = translate_to_english(indic_text_input)

    backend_processing_result = process_backend(english_translation)

    # Display the result in the user's preferred Indic language
    indic_output = translate_to_indic(backend_processing_result, source_language='en')

    print(f"Input (Indic): {indic_text_input}")
    print(f"Translated to English: {english_translation}")
    print(f"Backend Processing Result: {backend_processing_result}")
    print(f"Output (Indic): {indic_output}")


def process_backend(text):
    return f"Processed: {text}"


def translate_to_indic(text, source_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=source_language)
    return translation.text


if __name__ == "__main__":
    main()
