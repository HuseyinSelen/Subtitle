# 🎭 Wicked Japanese Subtitles Project

### 📷 
![wicked](Python.png)

## 📌 Project Overview
This project adds Japanese subtitles to the film *Wicked* by using Python. The process involves:
- Translating the English subtitles into Japanese using Python.
- Formatting and adjusting subtitle timings.

## 🔧 Technologies Used
- **Python** (for subtitle translation and integration)
- **Deep Translator** (for accurate subtitle translation)
- **SRT (SubRip Subtitle) format** (for handling subtitle files)

## 🚀 How It Works
1. The script reads the English subtitle (.srt) file.
2. It translates each line into Japanese.
3. The translated subtitles are formatted and adjusted for readability.

## 📂 Installation & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/HuseyinSelen/Subtitle.git
   cd wicked-jp-subtitles
   ```
2. Install the required dependencies:
   ```bash
   pip install deep-translator
   ```
3. Run the script:
   ```bash
   python script.py
   ```

## 📝 Python Script Breakdown
### `script.py`
- Uses **Deep Translator** to translate the `.srt` file from English to Japanese.

### `translate.py`
- Converts the translated subtitle file to **UTF-8 BOM format** to ensure proper display in media players.

### `second.py`
- Adjusts **short gaps** between subtitles to improve readability.

### `fixed.py`
- Ensures that each subtitle stays on screen for **at least 1 second**.
- Adds a **200-millisecond gap** between consecutive subtitles.

### `final.py`
- Splits subtitle lines exceeding **40 characters** into multiple lines for better readability.

## 🎯 Future Improvements
- Improve translation accuracy using a better NLP model.
- Develop a GUI for easier use.
- Add support for multiple languages.

## 🤝 Contributing
Feel free to fork this repository and submit pull requests if you have improvements or suggestions!

## 📜 License
This project is licensed under the MIT License.
