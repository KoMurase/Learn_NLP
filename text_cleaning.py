import mojimoji

#半角文字を全角文字に変換する
def zen_to_han(text):
    text = mojimoji.zen_to_han(text)
    return text

#アルファベットの大文字を小文字に変換
def lower_text(text):
    return text.lower()
#df['target_column'] = df['target_column'].apply(lower_text)

def normalize_number(text):
    # 連続した数字を0で置換
    replaced_text = re.sub(r'\d+', '0', text)
    return replaced_text

def sonota(text):
    text = text.replace('／','')
