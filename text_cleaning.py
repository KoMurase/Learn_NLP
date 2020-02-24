import majimoji

#半角文字を全角文字に変換する
def zen_to_han(dataframe):
    dataframe['text'] = dataframe['text'].apply(mojimoji.zen_to_han)
    return dataframe

#アルファベットの大文字を小文字に変換
def lower_text(text):
    return text.lower()
#df['target_column'] = df['target_column'].apply(lower_text)

def sonota(text):
    text = text.replace('／','')
