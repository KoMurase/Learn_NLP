import emoji
import nagisa
import unicodedata

KAOMOJI_PH = "<Kaomoji>"
URL_PH = "<URL>"
EMOJI_PH = "<Emoji>"
KAOMOJI_LEN = 5

def extract_kaomoji(text):
    """ 与えられたテキストから抽出した顔文字リストを返却する。
        → ＼(^o^)／, m(_ _)m などの 手を含む顔文字があれば、それも抽出する
    """
    results = nagisa.extract(text, extract_postags=['補助記号'])
    words = results.words
    kaomoji_words = []
    kaomoji_idx = [i for i, w in enumerate(words) if len(w) >= KAOMOJI_LEN]
    kaomoji_hands = ['ノ', 'ヽ', '∑', 'm', 'O', 'o', '┐', '/', '\\', '┌']
    # 顔文字と手を検索
    for i in kaomoji_idx:
        kaomoji = words[i] # 顔文字列
        try:
            # 顔文字の左手
            if words[i-1] in kaomoji_hands and 0 < i:
                kaomoji = words[i-1] + kaomoji
            # 顔文字の右手
            if words[i+1] in kaomoji_hands:
                 kaomoji = kaomoji + words[i+1]
        except IndexError:
            pass
        finally:
            kaomoji_words.append(kaomoji)
    return kaomoji_words

def extract_url(words):
    results = nagisa.extract(text, extract_postags=['URL'])
    return results.words

def extract_emoji(text):
    results = nagisa.tagging(text) # 形態素解析
    words = results.words
    return [w for w in words if w in emoji.UNICODE_EMOJI]

def replace(text, target_list, PH):
    for trg in target_list:
        text = text.replace(trg, PH)
    return text

def delete(text, target_list):
    for trg in target_list:
        text = text.replace(trg, "")
    return text

text = "今日は渋谷スクランブルスクエアに行ってきた＼(^o^)／ 夜景🏙サイコー❗️ https://hogehogehogehoge.jpg"
text = unicodedata.normalize('NFKC', text) # NFKC正規化

# 入力
print("対象テキスト: {}\n".format(text))

# 抽出
kaomoji_list = extract_kaomoji(text)
url_list = extract_url(text)
emoji_list = extract_emoji(text)

# 抽出結果
print("顔文字: {}".format(kaomoji_list))
print("URL: {}".format(url_list))
print("絵文字: {}\n".format(emoji_list))


# 削除
deleted_text = delete(text, kaomoji_list + url_list + emoji_list)
print("削除: {} \n".format(deleted_text))

# 置換
replaced_text = replace(text, kaomoji_list, KAOMOJI_PH)
replaced_text = replace(replaced_text, url_list, URL_PH)
replaced_text = replace(replaced_text, emoji_list, EMOJI_PH)
print("置換: {} \n".format(replaced_text))
