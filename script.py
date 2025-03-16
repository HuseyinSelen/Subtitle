import srt
from deep_translator import GoogleTranslator
import chardet

def detect_encoding(file_path):
    with open(file_path, "rb") as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def translate_srt(input_file, output_file):
    encoding = detect_encoding(input_file)

    with open(input_file, "r", encoding=encoding) as file:
        srt_content = file.read()

    subtitles = list(srt.parse(srt_content))  
    
    translator = GoogleTranslator(source="en", target="ja") 

    for index, sub in enumerate(subtitles):
        try:
            print(f"Çevriliyor ({index + 1}/{len(subtitles)})...") 
            sub.content = translator.translate(sub.content) 
        except Exception as e:
            print(f"Hata oluştu: {e}") 
            break 

    translated_srt = srt.compose(subtitles)  

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(translated_srt)

    print(f"✅ Çeviri tamamlandı! Çevrilen dosya: {output_file}")

input_srt = "Wicked.srt"  
output_srt = "Wicked_JP.srt"  

print("📂 Çeviri başlıyor...")
translate_srt(input_srt, output_srt)
print("🚀 Çeviri işlemi tamamlandı!")
