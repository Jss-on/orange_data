import subprocess
import numpy as np
import os
from scipy.io import wavfile
from python_speech_features import mfcc
import joblib
import time

# Function to capture audio using native ALSA command
def capture_audio(duration, samplerate, filename):
    command = f'arecord -D hw:0,0 -d {duration} -f S16_LE -r {samplerate} -c1 {filename}'
    subprocess.call(command, shell=True)
    samplerate, audio_data = wavfile.read(filename)
    os.remove(filename)  # Remove the temporary audio file
    return audio_data

# Function to extract MFCC features
def extract_mfcc_features(audio_data, sample_rate=16000):
    mfcc_features = mfcc(audio_data, sample_rate)
    return np.mean(mfcc_features, axis=0).reshape(1, -1)

if __name__ == "__main__":
    # Load the trained model
    model = joblib.load('best_audio_classifier.pkl')

    # Audio settings
    duration = 3  # 3 seconds
    samplerate = 16000  # 16 kHz
    filename = 'temp_audio.wav'  # Temporary audio file name
    
    while True:
        # Capture audio
        print("Capturing audio...")
        audio_data = capture_audio(duration, samplerate, filename)

        # Extract MFCC features
        mfcc_features = extract_mfcc_features(audio_data, samplerate)

        # Make prediction
        predicted_label = model.predict(mfcc_features)[0]
        print(f"Predicted Label: {predicted_label}")

        # Wait before capturing the next audio
        time.sleep(3)  # wait for 3 seconds
