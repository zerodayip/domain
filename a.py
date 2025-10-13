import requests

def fetch_html(url: str,
               referer: str = None,
               extra_headers: dict = None,
               timeout: int = 10,
               verify_ssl: bool = True) -> str:
    """
    Verilen URL'den özel headerlarla HTML çeker ve döndürür.
    - url: hedef URL (ör. "https://dizirella.com/")
    - referer: istekte göndermek istediğiniz Referer (ör. "https://google.com/")
    - extra_headers: ek headerlar (sözlük)
    - timeout: bağlantı için saniye
    - verify_ssl: SSL sertifika doğrulaması (gerekirse False yapmayın)
    """
    session = requests.Session()

    # Temel header (özelleştirin)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
    }

    if referer:
        headers["Referer"] = referer  # burada Referer eklenir

    if extra_headers:
        headers.update(extra_headers)

    try:
        resp = session.get(url, headers=headers, timeout=timeout, verify=verify_ssl)
        resp.raise_for_status()  # HTTP hatalarını yükseltir
        # Yanıtın encoding'ini requests genelde doğru belirler; gerekirse elle ayarlayın:
        # resp.encoding = 'utf-8'
        return resp.text
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"İstek başarısız: {e}") from e


if __name__ == "__main__":
    url = "https://dizirella.com/"
    referer = "https://www.google.com/"

    try:
        html = fetch_html(url, referer=referer)
        # Tüm HTML'i yazdırmak isterseniz:
        print(html)

        # veya dosyaya kaydetmek isterseniz:
        # with open("dizirella.html", "w", encoding="utf-8") as f:
        #     f.write(html)
        #     print("Kaydedildi: dizirella.html")
    except RuntimeError as err:
        print(err)
