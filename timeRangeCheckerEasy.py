hour, start, end = map(int, 
input("時刻、範囲開始、範囲終了を0〜23の間で空白で区切って入力してください（例: 0 1 2）：")
.split())

# 判定
def is_in_range(hour, start, end):
    if start == end:
        return True
    elif start < end:
        return start <= hour < end
    else:
        return hour >= start or hour < end

# 結果
if is_in_range(hour, start, end):
    print(f"{hour}時は範囲{start}時から{end}時の間に含まれます。")
else:
    print(f"{hour}時は範囲{start}時から{end}時の間に含まれません。")