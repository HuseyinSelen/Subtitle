import pysrt

def fix_subtitle_timing_and_durations(input_file, output_file, min_duration=1000, min_gap=200):
    subs = pysrt.open(input_file, encoding='utf-8')
    
    for i in range(len(subs) - 1):
        current_sub = subs[i]
        next_sub = subs[i + 1]
        

        duration = current_sub.end.ordinal - current_sub.start.ordinal
        if duration < min_duration:
            current_sub.end = current_sub.start + min_duration
        

        gap = next_sub.start.ordinal - current_sub.end.ordinal
        

        if gap < min_gap:
            next_sub.shift(milliseconds=(min_gap - gap))


    subs.save(output_file, encoding='utf-8')
    print(f"Düzeltilmiş altyazı kaydedildi: {output_file}")


fix_subtitle_timing_and_durations("Wicked_JP_final.srt", "Wicked_JP_fixed_final.srt")
