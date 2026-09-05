import requests
import time
import undetected_chromedriver as uc
from fake_useragent import UserAgent

url="https://www.flipkart.com/mobile-accessories/screen-guards/~cs-058a862f1f1921af2514d0f99ef11c7f/pr?sid=4rr,km5,ipq,lrv&marketplace=FLIPKART&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJVbmRlciDigrkxOTkiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJwcmljZV9yYW5nZSI6eyJyYW5nZVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJwcmljZV9yYW5nZSIsImluZmVyZW5jZVR5cGUiOiJGQUNFVCIsIm1pbiI6bnVsbCwibWF4IjoxOTkuMCwidmFsdWVUeXBlIjoiUkFOR0VfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJBQ0NITkZDSEdZS1BHRk5DIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsiU2NyZWVuIEd1YXJkcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&BU=Mixed"


##static web scraping/ http request:

# session=requests.session()
# headers={
#     "User-Agent":UserAgent().random,
#     "Accept-Language":'en-US,en;q=0.9',
#     "Accept-Encoding":"gzip,deflate,br",
#     "Connection":"keep-alive",
#     "Referer":"https://www.google.com"
# }
# time.sleep(2)
# r=session.get(url,headers=headers)
# with open ("indie.html","w",encoding="utf-8") as f:
#     f.write(r.text)


##stealth scraping/headless browser automation:
 
# options=uc.ChromeOptions()
# driver=uc.Chrome(options=options)
# driver.get(url)
# time.sleep(5)
# with open ("indie.html","w",encoding="utf-8") as f:
#     f.write(driver.page_source)
# driver.quit()