import os
import subprocess
import pytesseract
from PIL import Image
import csv
import chess
import chess.svg
import cairosvg
import platform

# Configure tesseract path for Windows if needed
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Folder settings
image_folder = "images"
output_csv = "anki_deck.csv"
output_image_folder = "generated_images"
os.makedirs(output_image_folder, exist_ok=True)

def fen_to_image(fen, output_path):
    board = chess.Board(fen)
    svg = chess.svg.board(board=board, coordinates=True)
    cairosvg.svg2png(bytestring=svg.encode('utf-8'), write_to=output_path)

with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Image", "Solution"])

    for image_name in sorted(os.listdir(image_folder)):
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, image_name)
            print(f"Processing {image_path}...")

            # Step 1: extract FEN using recognize.py
            result = subprocess.run(
                ['python', './recognizer/recognize.py', image_path],
                capture_output=True, text=True
            )
            fen = result.stdout.strip()

            print(f"FEN {fen} extracted from {image_path}")
            if not fen:
                print(f"Failed to extract FEN from {image_path}")
                continue
""" 
            # Step 2: generate image from FEN
            image_output_name = os.path.splitext(image_name)[0] + "_fen.png"
            image_output_path = os.path.join(output_image_folder, image_output_name)
            fen_to_image(fen, image_output_path)

            # Step 3: extract solution text using OCR
            image = Image.open(image_path)
            width, height = image.size
            solution_area = image.crop((0, int(height * 0.75), width, height))
            solution_text = pytesseract.image_to_string(solution_area, lang='eng').strip().replace('\n', ' ')

            # Step 4: write to CSV
            writer.writerow([image_output_path, solution_text]) """
