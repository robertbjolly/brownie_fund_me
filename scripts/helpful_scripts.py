from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']
DECIMALS = 8
STARTING_PRICE = 200_000_000


def get_account():
    print(network.show_active())
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS 
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
        
        
def deploy_mocks():
    print(f"Active Network is {network.show_active()}")
    print(f"Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from":get_account()})
    print(f"Mocks Deployed!")
