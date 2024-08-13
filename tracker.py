import requests
import streamlit as st

#선택한 암호화폐 가격
def get_crypto_price(crypto_id):
    url = f"https://api.coinpaprika.com/v1/tickers/{crypto_id}"
    response = requests.get(url)
    data = response.json()
    return data['quotes']['USD']['price']

st.title("암호 화폐 시세")

#선택한 코인
crypto_id = st.selectbox(
    "보고싶은 코인의 종류를 선택하세요.",
    ("btc-bitcoin", "eth-ethereum", "doge-dogecoin"),
)

#가격 가져오기(USD)
coin_data = get_crypto_price(crypto_id)
print(coin_data)

st.write(f"{crypto_id} : ${coin_data}")