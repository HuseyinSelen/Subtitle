
with open("Wicked_JP.srt", "r", encoding="utf-8") as file:
    content = file.read()

with open("Wicked_JP_utf8.srt", "w", encoding="utf-8-sig") as file:
    file.write(content)

print("Dosya UTF-8 BOM formatında kaydedildi: Wicked_JP_utf8.srt")
