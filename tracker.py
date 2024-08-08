import requests
import streamlit as st

#선택한 암호화폐 가격
def get_crypto_price(crypto_id):
    url = f"https://api.coinpaprika.com/v1/tickers/{crypto_id}"
    response = requests.get(url)
    data = response.json()
    return data['quotes']['USD']['price']

#선택한 코인
crypto_id = 'btc-bitcoin'

#가격 가져오기(USD)
coin_data = get_crypto_price(crypto_id)
print(coin_data)