import pysrt

def fix_subtitle_durations(input_file, output_file, min_duration=1000):
    subs = pysrt.open(input_file, encoding='utf-8')
    
    for sub in subs:
        duration = sub.end.ordinal - sub.start.ordinal
        

        if duration < min_duration:
            sub.end = sub.start + min_duration


    subs.save(output_file, encoding='utf-8')
    print(f"Düzeltilmiş altyazı kaydedildi: {output_file}")


fix_subtitle_durations("Wicked_JP_fixed.srt", "Wicked_JP_final.srt")
