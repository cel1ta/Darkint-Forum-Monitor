import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup  #extraer titulo HTML
import urllib3 #ocultar avisos de certificados

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #Ocultar avisos HTTPS
urls = [
    "http://exiliow4ctlzrvaglkgwqnpxdlvrxmdgvuy2hkbzqoziebfim6q5hwid.onion/login?to=",
    "http://hxnlhmafy242va6sjxcvcu7zq6m2gz75vgncynpeiwqtkjkdv2i6gjad.onion/",
    "http://dna777ucpo4unwxrzw5mzs4iqm5qz3uepw3k5mvwbt7tnufryvsgy5yd.onion/",
    "http://darkfoxaqhfpxkrbt7vxns2z2u2k72sgmqbzeorupaiottw3ecm2wgyd.onion/",
    "https://breachforums.bf/",
    "http://exploitivzcm5dawzhe6c32bbylyggbjvh5dyvsvb5lkuz5ptmunkmqd.onion",
    "http://verified3vr2kdbnza6c3e5ak4z5xmtti4hx36dfg3kbi6pwekztvsqd.onion/",
    "http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/",
    "http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/",
    "http://hidden2hvnijmpz7eapgsawn3ws2zbrt3cbi2awbi3jfmopqiylnfmyd.onion/",
    "http://breachqr3dqbysbq5khaadg5ynnpxn2wrmw5y3rnzesun55l6lkq73yd.onion/"
]

proxies = {  #proxy Tor
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

headers = {"User-Agent": "Mozilla/5.0"}

while True:

    print(f"\n[{datetime.now()}] Comprobando los foros...\n")

    for url in urls: #se recorren las urls de los foros
        try:
            inicio = time.time() #inicia el cronómetro

            peticion = requests.get( #petición HTTP
                url,
                proxies=proxies,
                headers=headers,
                timeout=60,  #si en 60 segundos no responde, da error
                allow_redirects=True,
                verify=False #no verifica certificados HTTPS,  porque algunas .onion usan certificados raros o autofirmados
            )

            tiempo = round(time.time() - inicio, 1) #cálculo del tiempo re despuesta

            time.sleep(15) # Espera 15 segundos antes de analizar el contenido. La idea es dar margen a sitios lentos, colas o protecciones

            html = peticion.text
            html_lower = html.lower() #mismo HTML en minúsculas para buscar palabras como captcha o queue

            try:
                soup = BeautifulSoup(html, "html.parser")
                title = soup.title.text.strip() if soup.title else "Sin título"  #Extrae el contenido de la etiqueta: <title>...</title>
            except:
                title = "Sin título"

            mensaje = f"OK | {peticion.status_code} | {tiempo}s | {title}"

            protecciones = [] #deteccion de protecciones

            if "captcha" in html_lower or "verify humanity" in html_lower:
                protecciones.append("CAPTCHA")

            if "queue" in html_lower or "waiting room" in html_lower:
                protecciones.append("COLA")

            if protecciones:
                mensaje += f" | {'/'.join(protecciones)}" #Si hay protecciones, las añade al final

            print(mensaje)

        #gestion de errores
        except requests.exceptions.ConnectTimeout: #Si no conecta antes de 60 segundos --> timeout
            print(f"TIMEOUT | No responde | {url}")

        except requests.exceptions.ConnectionError: #Si no puede establecer la conexión --> down
            print(f"DOWN | ConnectionError | {url}")

        except Exception as e: #si no es ninguno de los otros dos errores, captura el error y muestra el tipo
            print(f"ERROR | {type(e).__name__} | {url}")
            print(f"   {e}")

    print("\nEsperando 6 horas...\n")
    time.sleep(21600) #21600 segundos son 6 horas

