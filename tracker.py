import requests

api_key = "ftdtZqgZMRnlxUbD0bL0hMOutS4Q21z7"

def get_exchange_rate(date):
    url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate=20180102&data=AP01"
    response = requests.get(url)
    return response

# def get_crypto_price(crypto_id):
#     url = f"https://api.coinpaprika.com/v1/tickers/{crypto_id}"
#     response = requests.get(url)
#     data = response.json()
#     return data['quotes']['USD']['price']


# crypto_id = 'btc-bitcoin'  # 비트코인 가격을 USD로 조회
# coin_data = get_crypto_price(crypto_id)
# print(coin_data)

get_exchange_rate(20240807, "USD")