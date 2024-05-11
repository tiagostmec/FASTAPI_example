from typing import Tuple
import numpy as np
from scipy import signal

def generate_signal() -> np.ndarray:
    """
    Generate a vibration signal e.g. obtained from an accelerometer

    Input parameters are pre-defined for the purposes of this test
    """

    # Inputs
    fs = 10e3  # Sampling rate
    N = 1e5  # Number of samples
    amp = 2 * np.sqrt(2)  # Tone amplitude
    freq = 1234.0  # Tone frequency
    noise_power = 0.001 * fs / 2  # Noise power

    # Create a time vector based on number of samples and sampling rate
    time = np.arange(N) / fs

    # Create a pure tone signal based on tone frequency and amplitude
    x = amp * np.sin(2 * np.pi * freq * time)

    # Add white noise
    x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)

    # Return the signal
    return x


def get_spectrum(nperseg: int, window: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    Get spectrum from a signal
    """

    # Generate an arbitrary signal
    x = generate_signal()
    fs = 10e3

    # Compute frequency vector and spectrum
    f, Pxx = signal.welch(x, fs, nperseg=nperseg, window=window)

    # Return frequency vector and spectrum
    return f, Pxx