# The Empathy Engine

**Giving AI a Human Voice**

The Empathy Engine is a service that dynamically modulates Text-to-Speech (TTS) vocal characteristics based on the detected emotion of the input text. It bridges the gap between robotic TTS and expressive human communication.

## Features

*   **Emotion Detection**: Analyzes text to determine:
    *   **Base**: Positive, Negative, Neutral.
    *   **Granular**: Surprised, Inquisitive, Concerned.
*   **Dynamic Voice Modulation**: Adjusts speech Rate and Volume to create distinct emotional personas.
    *   *Positive*: Fast, Energetic.
    *   *Negative*: Very Slow, Soft.
    *   *Surprised*: Rapid, Loud.
    *   *Concerned*: Slow, Soft, Worried.
    *   *Inquisitive*: Slightly faster, engaging.
*   **Smart Voice Selection**: Automatically attempts to select a female voice (e.g., "Zira" on Windows) for a more empathetic tone.
*   **Web Interface**: A clean, modern UI to test the engine with granular feedback.
*   **CLI**: A command-line tool for quick testing.

## Prerequisites

*   Python 3.8+
*   Windows (Recommended for `pyttsx3` default drivers & "Zira" voice), macOS, or Linux.

## Setup

1.  **Clone/Navigate to the directory**:
    ```bash
    cd empathy_engine
    ```

2.  **Create and Activate Virtual Environment**:
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Web Interface (Recommended)

1.  Run the application:
    ```bash
    python main.py
    ```
2.  Open your browser to `http://localhost:8000`.
3.  Type text and click **Analyze** or **Speak**.

### CLI

Run the CLI tool with your text:

```bash
python cli.py "I am so happy to see you!"
python cli.py "This is really frustrating."
```

## Design Choices

*   **Emotion Analysis**: Combined `vaderSentiment` (for base polarity) with **Heuristics** (punctuation, keywords) to detect nuanced states like Surprise and Concern.
*   **TTS Engine**: `pyttsx3` was chosen for offline capabilities. Implemented a **Rate/Volume Modulation** system instead of unstable SSML tags to ensure reliable playback on all systems.
*   **Modulation Logic**:
    *   **Rate**: Effectively conveys energy (fast) or sadness/concern (slow).
    *   **Volume**: Adds emphasis (loud) or intimacy/worry (soft).

## Troubleshooting

*   **No Audio**: Ensure your system volume is up.
*   **Module Not Found**: Ensure you are running commands from the `empathy_engine` directory and the virtual environment is active.

## Examples

Try these phrases to get started:

*   "I cant, I am so worried about this situation."
*   "Wait, really? That happened?"
*   "Oh my god! That is amazing!"

