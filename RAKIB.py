import requests
x1 = input("EMTER NUMBER:")
x2 = int(input("ENTER LIMIT: "))
for i in range(x2):
api = requests.post(f"https://siamrahman.xyz/sms_bkash.php?phone=+88{x1}").status_code
....print(api)
