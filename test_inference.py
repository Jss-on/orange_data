import numpy as np
from scipy.io import wavfile
from python_speech_features import mfcc
import joblib

# Function to extract MFCC features
def extract_mfcc_features(audio_data, sample_rate=16000):
    mfcc_features = mfcc(audio_data, sample_rate)
    return np.mean(mfcc_features, axis=0).reshape(1, -1)

if __name__ == "__main__":
    # Load the trained model
    model = joblib.load('best_audio_classifier.pkl')
    
    # Read the sample audio file
    sample_rate, audio_data = wavfile.read('8.wav')
    
    # Extract MFCC features
    mfcc_features = extract_mfcc_features(audio_data, sample_rate)
    
    # Make prediction
    predicted_label = model.predict(mfcc_features)[0]
    print(f"Predicted Label: {predicted_label}")
