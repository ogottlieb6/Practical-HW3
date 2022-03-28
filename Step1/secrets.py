from algosdk import mnemonic

# TODO
PINATA_API_KEY = "c878d9475c8c66e35638"
PINATA_API_SECRET = "e1e560f971ae4f5e85eef13c6d9168736fa76fa445135ec2591b21c9c7fb709c"

# TODO
PURESTAKE_API_KEY = "ThUDJJfXvkauV65b58gHwaKu8bpGECgB16UOIoI0"

# TODO
account_mnemonic = "your-mnemonic-here" 
account_private_key = mnemonic.to_private_key(account_mnemonic)
account_address = mnemonic.to_public_key(account_mnemonic)

ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
ALGOD_HEADERS = {"X-API-Key": PURESTAKE_API_KEY}
