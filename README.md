# ♟️ Chess2Anki - Generate Anki decks from chessboard images

This project automates the creation of Anki flashcards from chess puzzle images taken from books or screenshots. Each image contains a chessboard and a solution written below it.

---

## 🚀 Features

- Automatically reads chess images (board + solution)
- Recognizes the chessboard and converts it into FEN
- Extracts the textual solution using OCR
- Generates a `.csv` file compatible with Anki:
  - Column 1: image path generated from FEN
  - Column 2: solution extracted from image

---

## 🛠️ Installation

### 📦 1. Clone the repository

```bash
git clone https://github.com/your-user/chess2anki.git
cd chess2anki
```

### 🤖 2. Chessboard Recognizer

The `chessboard-recognizer` (from [linrock](https://github.com/linrock/chessboard-recognizer)) is already integrated in this repository.  
You don't need to install it separately — just make sure the script `recognize.py` and the `nn/` model folder are included.

> If `nn/` is missing, download the release `nn.zip` from the [official releases](https://github.com/linrock/chessboard-recognizer/releases), unzip it, and place it inside the project directory.

### 🔍 3. Install Tesseract OCR

- **Windows**:  
  Download the installer from [UB Mannheim builds](https://github.com/UB-Mannheim/tesseract/wiki).  
  During installation, select the desired languages (e.g., English, French).  
  Default install path: `C:\Program Files\Tesseract-OCR`

- **macOS**:  
  Install via Homebrew:
  ```bash
  brew install tesseract
  ```

- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt install tesseract-ocr
  ```

### 📥 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 📁 Input

- Place all your input images in the `images/` folder.
- Accepted formats: `.png`, `.jpg`, `.jpeg`
- Each image should contain:
  - A chessboard in the upper part
  - An explanation (text) in the lower part

### ⚙️ Run the script

```bash
python script.py
```

### 📤 Output

- The generated FEN-based images are saved in the `generated_images/` folder.
- The Anki-compatible CSV file is saved as `anki_deck.csv` in the project root.

---

## 📂 Project Structure

```
project/
├── images/              # Your input images go here
├── generated_images/    # FEN-generated board images
├── nn/                  # Pretrained model folder from chessboard-recognizer
├── recognize.py         # Chessboard recognizer script
├── script.py            # Main automation script
├── anki_deck.csv        # Final CSV ready to import into Anki
└── requirements.txt     # Python dependencies
```

---

## ✅ Example CSV Output

| Image Path                    | Solution Text                                      |
|------------------------------|----------------------------------------------------|
| generated_images/img1_fen.png| White to play and mate in 2 with Qg7+              |

---

## 📜 License

MIT License — free to use, modify and share!

---

## 👤 Author

Made with ❤️ for chess and Anki lovers.
