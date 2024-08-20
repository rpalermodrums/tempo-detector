import librosa
import numpy as np
import argparse
from scipy.signal import find_peaks
from pydub import AudioSegment

class TempoDetector:
    def __init__(self, file_path, sr=22050, hop_length=512):
        self.file_path = file_path
        self.sr = sr
        self.hop_length = hop_length
        self.y = None
        self.onset_env = None

    def load_audio(self):
        if self.file_path.lower().endswith('.m4a'):
            audio = AudioSegment.from_file(self.file_path, format="m4a")
            audio = audio.set_channels(1)  # Convert to mono
            samples = audio.get_array_of_samples()
            self.y = np.array(samples).astype(np.float32) / 32768.0  # Normalize to [-1, 1]
        else:
            self.y, _ = librosa.load(self.file_path, sr=self.sr)


    def compute_onset_envelope(self):
        self.onset_env = librosa.onset.onset_strength(y=self.y, sr=self.sr, hop_length=self.hop_length)

    def compute_fft(self):
        fft = np.fft.fft(self.onset_env)
        magnitudes = np.abs(fft[:len(fft)//2])
        frequencies = np.linspace(0, self.sr / (2 * self.hop_length), len(magnitudes))
        return frequencies, magnitudes

    def compute_autocorrelation(self):
        return librosa.autocorrelate(self.onset_env, max_size=self.sr // self.hop_length)

    def detect_tempo(self):
        if self.y is None:
            self.load_audio()
        if self.onset_env is None:
            self.compute_onset_envelope()

        # FFT-based tempo estimation
        frequencies, magnitudes = self.compute_fft()
        fft_tempo_range = np.where((frequencies >= 0.5) & (frequencies <= 5))[0]  # 30-300 BPM range
        fft_peak = frequencies[fft_tempo_range[np.argmax(magnitudes[fft_tempo_range])]]
        fft_tempo = fft_peak * 60

        # Autocorrelation-based tempo estimation
        ac = self.compute_autocorrelation()
        ac_tempo_range = np.where((60 / (self.sr / self.hop_length / np.arange(len(ac))) >= 30) & 
                                  (60 / (self.sr / self.hop_length / np.arange(len(ac))) <= 300))[0]
        ac_peak = ac_tempo_range[np.argmax(ac[ac_tempo_range])]
        ac_tempo = 60 / (ac_peak * self.hop_length / self.sr)

        # Combine estimates
        if abs(fft_tempo - ac_tempo) < 5:  # If estimates are close, take the average
            final_tempo = (fft_tempo + ac_tempo) / 2
        else:  # Otherwise, prefer the autocorrelation estimate
            final_tempo = ac_tempo

        return final_tempo

    def plot_results(self):
        import matplotlib.pyplot as plt

        plt.figure(figsize=(12, 8))

        # Plot onset strength
        plt.subplot(3, 1, 1)
        librosa.display.specshow(librosa.amplitude_to_db(self.onset_env.reshape(1, -1), ref=np.max),
                                 sr=self.sr, hop_length=self.hop_length, x_axis='time')
        plt.title('Onset Strength')

        # Plot FFT
        plt.subplot(3, 1, 2)
        frequencies, magnitudes = self.compute_fft()
        plt.plot(frequencies, magnitudes)
        plt.title('FFT of Onset Strength')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')

        # Plot Autocorrelation
        plt.subplot(3, 1, 3)
        ac = self.compute_autocorrelation()
        plt.plot(ac)
        plt.title('Autocorrelation of Onset Strength')
        plt.xlabel('Lag')
        plt.ylabel('Autocorrelation')

        plt.tight_layout()
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="Detect tempo of an audio file.")
    parser.add_argument("file_path", help="Path to the audio file")
    parser.add_argument("--plot", action="store_true", help="Plot the results")
    args = parser.parse_args()

    detector = TempoDetector(args.file_path)
    tempo = detector.detect_tempo()
    print(f"Estimated tempo: {tempo:.2f} BPM")

    if args.plot:
        detector.plot_results()

if __name__ == "__main__":
    main()

