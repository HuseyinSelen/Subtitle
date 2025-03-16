import pysrt
import textwrap

def split_long_lines(input_file, output_file, max_length=40):
    subs = pysrt.open(input_file, encoding='utf-8')

    for sub in subs:

        if len(sub.text) > max_length:
            sub.text = "\n".join(textwrap.wrap(sub.text, width=max_length))


    subs.save(output_file, encoding='utf-8')
    print(f"Düzeltilmiş altyazı kaydedildi: {output_file}")


split_long_lines("Wicked_JP_fixed_final.srt", "Wicked_JP_final_fixed.srt")
