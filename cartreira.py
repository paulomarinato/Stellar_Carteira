from stellar_sdk import Keypair, Server, TransactionBuilder, Network

keypair = Keypair.random()
public_key = keypair.public_key
secret_key = keypair.secret

print(f"Chave Pública (endereço da carteira): {public_key}")
print(f"Chave Secreta (não compartilhe com ninguém): {secret_key}")

server = Server("https://horizon.stellar.org")

try:
    account = server.accounts().account_id(public_key).call()
    print("Conta já existe na mainnet.")
except Exception as e:
    print("Conta não encontrada. Você precisará financiar esta conta com lumens.")

try:
    account = server.accounts().account_id(public_key).call()
    balances = account['balances']
    for balance in balances:
        print(f"Tipo de ativo: {balance['asset_type']}, Saldo: {balance['balance']}")
except Exception as e:
    print("Erro ao verificar o saldo:", str(e))

