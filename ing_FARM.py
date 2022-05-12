#%%
from mailbox import NotEmptyError
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#%%
url = 'https://www.farmrio.com.br/moda-feminina?O=OrderByScoreDESC&pg={}&line=0'


# %%
i = 1
ret = requests.get(url.format(i))
soup = bs(ret.text)
# %%
produtos = soup.find_all('div',{'class':'shelf-product'})
qtd_produtos = float(soup.find('span',{'class':'value'}).text.format(float))

# %%
len(produtos)
#%%
qtd_produtos
# %%
produto = produtos[0]

# %%
produto
# %%
df = pd.DataFrame(
    columns=[
        'nome',
        'preco',
        'wlink'
    ]
)
i = 0
#%%
while qtd_produtos > df.shape[0]:
    print(f"valor i: {i}\t\t qtd_produtos: {df.shape[0]}")
    i += 1
    ret = requests.get(url.format(i))
    soup = bs(ret.text)
    produtos = soup.find_all('div',{'class':'shelf-product'})
    for produto in produtos:
        try:
            nome = produto.find('h4',{'class':'shelf-product__title'}).text.strip()
        except:
            nome = None    
        try:
            preco = produto.find('span',{'class':'shelf-product__price-best'}).text.strip()
        except:
            preco = None    
        try:
            wlink = produto['href']
        except:
            wlink = None    

        df.loc[df.shape[0]] = [
            nome,
            preco,
            wlink
        ]

#%%    
print(nome)
print(preco)
print(wlink)
# %%
df
# %%
df.to_csv('banco_de_dados_moda_feminina_farm.csv', sep=';',index=False)
# %%
