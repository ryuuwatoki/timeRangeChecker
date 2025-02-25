# 氏名: 劉羽時
# 課題: 時刻が範囲内に含まれるか判定するスクリプト

# 機能説明
# 1. 課題判定（指定された課題が適切かどうかを判断します）
# 2. 誤字判定（入力されたテキストの誤字を検出します）
# 3. 終了後にWindowsOSのpython自動的にウィンドウが閉じないように、ユーザーの入力を待つ機能


# 開始の挨拶と説明
print("\nこれは時間が指定した範囲内に含まれるかどうかを判定するスクリプトです。")
print("次に、ユーザーには2つの値を入力してもらいます。")
print("1つは時刻、もう1つは範囲です。\n")


# 判定
def is_in_range(hour, start, end):
    # 開始時間と終了時間が同じ場合は、その時刻を範囲に含む
    if start == end:
        return True
    # 開始時間が終了時間より小さい（通常の範囲）
    elif start < end:
        return start <= hour < end
    # 開始時間が終了時間より大きい（例えば、22時から5時までの場合）
    else:
        return hour >= start or hour < end

# 時刻入力エラーチェック
while True:
    try:
        print('確認したい時刻')
        hour = int(input('0〜23の間で時刻を入力してください: '))
        if 0 <= hour <= 23:
            break
        else:
            print("無効な入力です。0〜23の間の整数を入力してください。")
    except ValueError:
        print("無効な入力です。整数を入力してください。文字列や小数点は含まれていません。")

# 範囲入力エラーチェック
while True:
    try:
        print('\n確認したい範囲')
        start, end = map(int, input('0〜23の間で開始時刻と終了時刻を空白で区切って入力してください（例: 1 23): ').split())
        if 0 <= start <= 23 and 0 <= end <= 23:
            break
        else:
            print("無効な範囲です。0〜23の間の整数を入力してください。")
    except ValueError:
        print("無効な入力です。開始時刻と終了時刻を空白で区切って2つの整数として入力してください。例: 1 23")

# 結果
if is_in_range(hour, start, end):
    print('')
    print(f"{hour}時は範囲{start}時から{end}時の間に含まれます。")
    print('')
else:
    print('')
    print(f"{hour}時は範囲{start}時から{end}時の間に含まれません。")
    print('')

# 終了メッセージと待機
input("スクリプトを終了するには、Enterキーを押してください")