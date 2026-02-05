import pyttsx3
import os

def create_tts_from_file_offline(text_file, output_audio_file='output.mp3'):
    """
    Reads text from a file and converts it to speech using pyttsx3, 
    saving it to a file.
    
    Args:
        text_file (str): The path to the input text file.
        output_audio_file (str): The name for the output audio file (e.g., .mp3 or .wav).
    """
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Read text from the file
        with open(text_file, 'r', encoding='utf-8') as f:
            text = f.read()

        if not text.strip():
            print(f"Error: Text file '{text_file}' is empty.")
            return

        # Save the speech to a file
        engine.save_to_file(text, output_audio_file)
        engine.runAndWait() # This command processes the save action

        print(f"Successfully created audio file: {output_audio_file}")

    except FileNotFoundError:
        print(f"Error: The file '{text_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    
    input = "C:\\Github/SideProjects/TTS/test.txt"
    
    
    create_tts_from_file_offline(input, 'file_output.mp3')
    
main()
