from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Asset
import base64

secret_key = "SBV755LK3VICA5HUEL3WEKI4QWB6UV2XA5QBHK5SU6SWDVPFFSI5RUCU"
destination_address = "GDUWMGMTPLTYQD3GCUVSRQF6P4EL64HD73VBZHGPX6DQKIMTMWFAAPHL"
amount = "50"

keypair = Keypair.from_secret(secret_key)
server = Server(horizon_url="https://horizon.stellar.org")
source_account = server.load_account(keypair.public_key)

texto = "DEV30K"
texto_binario = texto.encode("utf-8")
texto_base_64 = base64.b64encode(texto_binario)

assinatura = keypair.sign(texto_base_64)

transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.PUBLIC_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .add_text_memo("DEV30K")
    .append_manage_data_op(
        data_name="desafio",
        data_value=assinatura)  
    .set_timeout(30)
    .build()
)

transaction.sign(keypair)

try:
    response = server.submit_transaction(transaction)
    print("Transação enviada com sucesso!")
    print(response)
except Exception as e:
    print("Erro ao enviar a transação:", e)



