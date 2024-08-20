# Tempo Detector

Tempo Detector is a command-line tool for accurately detecting the tempo of audio files using Fast Fourier Transform (FFT) and autocorrelation methods. This tool is designed for music producers, DJs, and audio engineers who need to quickly and accurately determine the tempo of a track.

## Features

- Accurate tempo detection using both FFT and autocorrelation methods
- Command-line interface for easy integration into workflows
- Optional visualization of onset envelope, FFT, and autocorrelation results
- Support for various audio file formats (wav, mp3, etc.)
- Dockerized for easy setup and consistent environment

## Installation

### Using Docker (Recommended)

1. Clone this repository:
   ```
   git clone https://github.com/rpalermodrums/tempo_detector.git
   cd tempo_detector
   ```

2. Build the Docker image:
   ```
   docker-compose build
   ```

### Traditional Method

If you prefer not to use Docker, follow these steps:

1. Clone this repository:
   ```
   git clone https://github.com/rpalermodrums/tempo_detector.git
   cd tempo_detector
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Using Docker

To detect the tempo of an audio file using Docker:

1. Place your audio files in the `audio` directory in the project root.

2. Run the following command:
   ```
   docker-compose run --rm tempo-detector audio/your_audio_file.mp3
   ```

   This will output the estimated tempo in beats per minute (BPM).

3. To visualize the results, add the `--plot` flag:
   ```
   docker-compose run --rm tempo-detector audio/your_audio_file.mp3 --plot
   ```

   Note: Visualization might not work properly in all environments when using Docker. If you encounter issues, try the traditional method.

### Traditional Method

To detect the tempo of an audio file without Docker:

1. Run the script from the command line:
   ```
   python tempo_detector.py path/to/your/audio/file.mp3
   ```

2. To visualize the results, add the `--plot` flag:
   ```
   python tempo_detector.py path/to/your/audio/file.mp3 --plot
   ```

This will display a plot with three subplots:
1. Onset Strength
2. FFT of Onset Strength
3. Autocorrelation of Onset Strength

## How It Works

The Tempo Detector uses the following process to estimate the tempo:

1. Load the audio file and compute the onset strength envelope.
2. Perform FFT on the onset envelope to identify dominant frequencies.
3. Compute the autocorrelation of the onset envelope to find periodicities.
4. Combine the results from FFT and autocorrelation for a robust tempo estimate.

## Contributing

Contributions to the Tempo Detector project are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [librosa](https://librosa.org/) - The library used for audio and music processing
- [numpy](https://numpy.org/) - For numerical computing
- [scipy](https://www.scipy.org/) - For signal processing functions
- [matplotlib](https://matplotlib.org/) - For plotting and visualization
- [Docker](https://www.docker.com/) - For containerization

## Contact

For any queries or suggestions, please open an issue on the GitHub repository.
