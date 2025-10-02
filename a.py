# fetch_dizi20.py
import requests

def fetch_full_html(url: str, timeout: float = 10.0) -> str:
    """
    Verilen URL'nin tamamını çekip HTML döner.
    - headers içinde User-Agent, Accept, Referer vb. eklenir.
    - timeout: saniye cinsinden istek zaman aşımı.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        # İstediğiniz referer'ı buraya koyun:
        "Referer": "https://google.com/",
        # isteğe bağlı diğer başlıklar:
        "Connection": "keep-alive",
        "DNT": "1",  # Do Not Track
    }

    # Oturum kullanmak çerezleri korur ve daha gerçekçi istek sağlar
    session = requests.Session()
    session.headers.update(headers)

    try:
        resp = session.get(url, timeout=timeout)
        resp.raise_for_status()  # HTTP hatalarını raise eder

        # Doğru karakter kodlamasını kullanmak için:
        if resp.encoding is None or resp.encoding == 'ISO-8859-1':
            # requests bazen yanlış encoding tahmin eder; apparent_encoding kullanmak genelde iyidir
            resp.encoding = resp.apparent_encoding

        return resp.text

    except requests.exceptions.RequestException as e:
        # Hata mesajını döndür veya tekrar raise et
        raise RuntimeError(f"İstek başarısız: {e}")

if __name__ == "__main__":
    url = "https://dizi20.life/"
    try:
        html = fetch_full_html(url)
        # HTML'i terminale yazdırır (çok büyükse dikkat!)
        print(html)

        # Eğer isterseniz HTML'i dosyaya kaydedebilirsiniz:
        # with open("dizi20_life.html", "w", encoding="utf-8") as f:
        #     f.write(html)

    except RuntimeError as err:
        print(err)
