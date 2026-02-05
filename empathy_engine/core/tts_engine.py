import pyttsx3
import os
import uuid

class TTSEngine:
    def __init__(self, output_dir="static/audio"):
        self.output_dir = output_dir
        
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_audio(self, text: str, emotion: str) -> str:
        """
        Generates audio for the given text, modulating voice parameters based on emotion.
        Returns the path to the generated file.
        """
        engine = pyttsx3.init()
        
        # 1. Select a Female Voice
        # Typical IDs on Windows: 0=David (Male), 1=Zira (Female)
        voices = engine.getProperty('voices')
        voice_selected = False
        for voice in voices:
            # Look for "Zira" (Windows default female) or generic "female"
            if "zira" in voice.name.lower() or "female" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                voice_selected = True
                break
        
        # Fallback if no specific female voice found
        if not voice_selected and len(voices) > 1:
             engine.setProperty('voice', voices[1].id)

        
        # 2. Aggressive Modulation Logic (Rate & Volume Only)
        # SAPI5 SSML injection via pyttsx3.save_to_file is unstable (produces empty files).
        
        # Defaults
        rate = 175
        volume = 1.0
        
        if emotion == "positive":
            rate = 220      # Fast, Energetic
            volume = 1.0    # Loud
        elif emotion == "negative":
            rate = 115      # Very Slow, Sad
            volume = 0.5    # Soft
        elif emotion == "surprised":
            rate = 240      # Very Fast (Excitement)
            volume = 1.0    # Loud
        elif emotion == "inquisitive":
            rate = 185      # Slightly Faster
            volume = 1.0    # Normal-Loud
        elif emotion == "concerned":
            rate = 130      # Slow
            volume = 0.6    # Soft
        else: # neutral
            rate = 175
            volume = 0.9

        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)

        filename = f"{uuid.uuid4()}.wav"
        filepath = os.path.join(self.output_dir, filename)
        
        # Save plain text to file (reliable)
        engine.save_to_file(text, filepath)
        engine.runAndWait()
        
        if engine._inLoop:
             engine.endLoop()
             
        return filepath
