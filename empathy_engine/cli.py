import argparse
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from empathy_engine.core.emotion_analyzer import EmotionAnalyzer
from empathy_engine.core.tts_engine import TTSEngine

def main():
    parser = argparse.ArgumentParser(description="The Empathy Engine CLI")
    parser.add_argument("text", type=str, help="The text to speak")
    args = parser.parse_args()

    print(f"Input Text: {args.text}")

    # Analyze
    analyzer = EmotionAnalyzer()
    emotion = analyzer.analyze(args.text)
    print(f"Detected Emotion: {emotion.upper()}")

    # Generate Audio
    print("Generating Audio...")
    tts = TTSEngine()
    try:
        output_path = tts.generate_audio(args.text, emotion)
        print(f"Success! Audio saved to: {output_path}")
    except Exception as e:
        print(f"Error generating audio: {e}")

if __name__ == "__main__":
    main()
