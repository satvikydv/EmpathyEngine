import pyttsx3
import os

def test_sapi5_ssml():
    engine = pyttsx3.init()
    
    print("Testing standard text...")
    engine.say("This is standard text.")
    engine.runAndWait()

    print("Testing Pitch modification (SAPI5 XML)...")
    text_pitch = "This is <pitch middle='5'>higher pitch</pitch> and this is <pitch middle='-5'>lower pitch</pitch>."
    engine.say(text_pitch)
    engine.runAndWait()
    
    print("Testing Rate modification...")
    text_rate = "This is <rate speed='5'>fast text</rate> and this is <rate speed='-5'>slow text</rate>."
    engine.say(text_rate)
    engine.runAndWait()
    
    print("Test Complete.")

if __name__ == "__main__":
    test_sapi5_ssml()
