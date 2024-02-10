from googletrans import Translator
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak in an Indic language:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        text = recognizer.recognize_google(audio, language="bn-IN")

        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Error accessing Google Speech Recognition service: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def translate_to_english(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    # Take user voice input in an Indic language
    indic_speech_input = recognize_speech()

    if indic_speech_input:
        # Translate Indic language input to English
        english_translation = translate_to_english(indic_speech_input)

        # Simulated backend processing with the translated text
        backend_processing_result = process_backend(english_translation)

        # Display the result in the user's preferred Indic language
        indic_output = translate_to_indic(backend_processing_result, source_language='en')

        print(f"Input (Indic): {indic_speech_input}")
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
