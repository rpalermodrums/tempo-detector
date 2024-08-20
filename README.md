# Tempo Detector

A command-line tool for detecting the tempo of audio files using FFT and autocorrelation methods.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/rpalermodrums/tempo_detector.git
   cd tempo_detector
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line:

```
python tempo_detector.py path/to/your/audio/file.mp3
```

To visualize the results, add the `--plot` flag:

```
python tempo_detector.py path/to/your/audio/file.mp3 --plot
```

## License

This project is licensed under the MIT License.
