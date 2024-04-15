import requests
import json

def test_get_api(request_id):

    def access_token_call():
        username = 'api@botminds.ai'
        login_url="https://marketplace.uat.lauramac.io/mp/client/authorization?username=api@botminds.ai&password=VP$YlsZzv!lx5uQFY%23gYpU!r"
        #login_url = 'https://marketplace.uat.lauramac.io/mp/client/authorization?username=api%40botminds.ai&password=VP$YlsZzv!lx5uQFY#gYpU!r'
        payload = {
            'username': username
        }

        response = requests.post(login_url, headers=payload, verify=False)

        if response.ok:
            response_data = response.json()
            if 'result' in response_data and response_data['result'] is not None:
                access_token = response_data['result']
                #print("Access token:", access_token)
                return access_token
            else:
                return "Failed to obtain access token."
        else:
            return "Failed to connect or authenticate."

    access_token = access_token_call()
    user_name = 'api@botminds.ai'
    classification_complete_url = f'https://marketplace.uat.lauramac.io/mp/document/getLoanInformation/GTYC3M0GFZ95/{request_id}'
    headers_login = {
            'username': user_name,
            'Authorization': access_token,
            'Content-Type': 'application/json'
        }
    data = {'folderPath': "Output"}
    response = requests.get(classification_complete_url, headers=headers_login,data=json.dumps(data) ,verify=False)
    print(response) 
    print(f'{request_id} classification complete')

    if response.ok:
        json_response = response.json()
            
        loan_number = json_response["Loan Number"]
        seller = json_response["Seller"]
        buyer = json_response["Buyer"]
        request_id = json_response["Request ID"]
        transaction_identifier = json_response["Transaction Identifier"]
        transaction_name = json_response["Transaction Name"]
        request_timestamp = json_response["Request Timestamp"]
        
        return (
            loan_number,
            seller,
            buyer,
            request_id,
            transaction_identifier,
            transaction_name,
            request_timestamp
        )
    else:
        return None

loan_number,seller,buyer,request_id,transaction_identifier,transaction_name,request_timestamp=test_get_api(" E08N8ZS6R67OD2MWP4WTLSAB")
print('loan_number:',loan_number)
print('seller:',seller)
print('buyer:',buyer)
print('request_id:',request_id)
print('transaction_identifier:',transaction_identifier)
print('transaction_name:',transaction_name)
print('request_timestamp:',request_timestamp)