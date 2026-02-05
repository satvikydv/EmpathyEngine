import sys
import os

# Ensure package path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from empathy_engine.core.tts_engine import TTSEngine

def test_generation():
    print("Initializing TTS Engine...")
    tts = TTSEngine(output_dir="debug_output")
    
    test_cases = [
        ("I am happy", "positive"),
        ("I am sad", "negative"),
        ("I am surprised!", "surprised"),
        ("Really?", "inquisitive"),
        ("I am worried.", "concerned")
    ]
    
    for text, emotion in test_cases:
        print(f"\nTesting: '{text}' with emotion '{emotion}'")
        try:
            filepath = tts.generate_audio(text, emotion)
            print(f"Generated: {filepath}")
            
            # Check file size
            if os.path.exists(filepath):
                size = os.path.getsize(filepath)
                print(f"File size: {size} bytes")
                if size < 100:
                    print("WARNING: File seems too small (silence or error?)")
            else:
                print("ERROR: File not created!")
                
        except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    test_generation()
