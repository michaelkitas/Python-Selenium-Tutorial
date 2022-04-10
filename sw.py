from seleniumwire import webdriver 
from seleniumwire.utils import decode
import json
import time

driver = webdriver.Chrome()

def intercept(request):
    if request.url.startswith("https://encrypted-tbn0.gstatic.com/images?q="):
        # request.abort()
        request.create_response(
            status_code=200,
            headers={'Content-Type': 'image/jpeg'},
            body=open('download.jpg', 'rb').read()
        )


driver.request_interceptor = intercept

driver.get('https://www.google.com/search?q=mountain&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj0ssffh4f3AhXjUOUKHeT0CVAQ_AUoAXoECBcQAw&biw=2133&bih=1121&dpr=1.8')

# for request in driver.requests:
#     if request.response:
#         if request.url.startswith("https://www.google.com/log?format=json"):
#             response = request.response
#             body = decode(response.body, response.headers.get('Content-Encoding', 'identity'))
#             decoded_body = body.decode('utf-8')
#             json_data = json.loads(decoded_body)
#             print(json_data)

time.sleep(120)