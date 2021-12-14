# Importe ganache account provide by brownie and config yaml
# Brownie can import smart contrat instead of open it with python open()
from brownie import accounts, config, SimpleStorage
import os

# Run script with brownie run "myscript"


def deploySimpleStorage():
    # Display private key from ganache
    account = accounts[0]
    # Deploy directly the contract and specify the owner (MUC QUICKER TAN w3.pyA
    # Return a contract object
    simplestorage = SimpleStorage.deploy({"from": account})
    # Brownie know difference between a Call or a Transaction
    # Retrieve is a view function No transaction
    stored_value = simplestorage.retrieve()
    print(stored_value)
    # Transaction may had a sender
    transaction = simplestorage.store(15, {"from": account})
    transaction.wait(1)
    update_stored_value = simplestorage.retrieve()
    print(update_stored_value)
    """
    Manage account Cli:
        list: brownie accounts list
        create: brownie accounts new "name"
        delete: brownie accounts delete "name"
    """
    # Store private key (more secure way) if work with real keys
    # account = accounts.load("adam-dev")
    # Store key in .env and display it from env by os module
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # Same as up but more effiscient
    # account = accounts.add(config["wallets"]["from_keys"])

    pass


def main():
    deploySimpleStorage()
