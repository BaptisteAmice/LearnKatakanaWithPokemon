import pykakasi

def japanese_to_romanji(text):
    kks = pykakasi.kakasi()
    result = kks.convert(text)
    return result[0]['hepburn']
