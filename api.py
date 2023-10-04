print('Start api read application')

import requests;

pagina_resultaat = requests.get("https://catfact.ninja/facts")
print(pagina_resultaat)

#met .json kunnen we de inhoud van de pagina lezen
# als een json bericht
feitjes = pagina_resultaat.json()
i = 0

for feit in feitjes:

    print(feitjes["data"][i]["fact"])
    i += 1
    
