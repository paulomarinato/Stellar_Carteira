from stellar_sdk import Server

def verificar_saldo(public_key):
    try:
        server = Server("https://horizon.stellar.org")
        account = server.accounts().account_id(public_key).call()
        
        print("Saldo da conta:")
        for balance in account['balances']:
            print(f"Tipo: {balance['asset_type']}, Saldo: {balance['balance']}")
    
    except Exception as e:
        print("Erro ao carregar a conta:", e)

public_key = "GBVQXJ3DAQ236ULCMWOVLCSF5HFCQ7UCPQAPMHTQUN2DWK2AM7ZMS3H6"
verificar_saldo(public_key)

