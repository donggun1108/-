# 당사자 사이트에서 코드 내리라고 하면 내릴게요 
import requests

url = "https://www.24gogopin.com/skin/SKIN_ORDER/01/ajax.bank.chk.php"

은행 = input("은행명을 입력해주세요: ")
계좌번호 = input("계좌번호를 입력해주세요: ")

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "X-Requested-With" : "XMLHttpRequest",
    "Host" : "www.24gogopin.com",
    "Origin" : "https://www.24gogopin.com",
    "Referer" : "https://www.24gogopin.com/?gad_source=1&gclid=EAIaIQobChMIlreL-L3hiwMVEtQWBR3ndTNOEAAYAiAAEgKT-fD_BwE"
}

pay_load = {
    "bank_nm" : 은행,
    "bank_num" : 계좌번호
}

response = requests.post(url, headers=headers, data=pay_load)
json = response.json()
print("응답 : ", response.status_code) # 200이면 성공
print("결과 :", json)
