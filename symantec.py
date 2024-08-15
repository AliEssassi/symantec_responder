import sys
import json
import requests

# Configuration
symantec_edr_url = 'https://managementapi.symantec.com/v1/policies/deny-list'
symantec_api_key = 'YOUR_SYMANTEC_API_KEY'  # Replace with your actual API key

headers_symantec = {
    'Authorization': f'Bearer {symantec_api_key}',
    'Content-Type': 'application/json'
}

def deny_list_ioc(ioc):
    data = {
        "deviceTypes": ["all"],
        "osFamilies": ["all"],
        "values": [ioc]
    }
    
    response = requests.post(symantec_edr_url, headers=headers_symantec, json=data)
    
    if response.status_code == 200:
        return {"success": True, "message": f"IOC {ioc} has been deny listed."}
    else:
        return {"success": False, "message": f"Failed to deny list IOC {ioc}.", "details": response.json()}

def main():
    input_data = json.load(sys.stdin)
    ioc = input_data['data']['data']
    
    result = deny_list_ioc(ioc)
    
    print(json.dumps(result))

if __name__ == "__main__":
    main()
