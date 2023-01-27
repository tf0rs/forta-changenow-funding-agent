import logging
import sys

from forta_agent import get_json_rpc_url, Web3
from hexbytes import HexBytes

from src.constants import *
from src.findings import FundingChangenowFindings


#Initialize web3.
web3 = Web3(Web3.HTTPProvider(get_json_rpc_url()))

# Logging set up.
root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)


def initialize():
    """
    Reset global variables - used in tests.
    """


def is_contract(w3, address):
    """
    this function determines whether address is a contract
    :return: is_contract: bool
    """
    if address is None:
        return True
    code = w3.eth.get_code(Web3.toChecksumAddress(address))
    return code != HexBytes('0x')


def detect_changenow_funding(w3, transaction_event):
    findings = []

    chain_id = w3.eth.chain_id
    native_value = transaction_event.transaction.value / 10e17

    logging.info(f"Analyzing transaction {transaction_event.transaction.hash} on chain {chain_id}")
    logging.info(f"Raw value: {transaction_event.transaction.value}")
    logging.info(f"Value: {native_value}")
    logging.info(f"Changenow address: {CHANGENOW_ADDRESSES[chain_id]}")
    logging.info(f"Sending address: {transaction_event.from_}")
    logging.info(f"Address transaction count: {w3.eth.get_transaction_count(Web3.toChecksumAddress(transaction_event.to))}")
    """
    if the transaction is from Changenow, and not to a contract: check if transaction count is 0, 
    else check if value sent is less than the threshold
    """
    if (transaction_event.from_ in CHANGENOW_ADDRESSES[chain_id] and not is_contract(w3, transaction_event.to)):
        if w3.eth.get_transaction_count(Web3.toChecksumAddress(transaction_event.to)) == 0:
            findings.append(FundingChangenowFindings.funding_changenow(transaction_event, "new-eoa", chain_id))
        elif native_value < CHANGENOW_THRESHOLD[chain_id]:
            findings.append(FundingChangenowFindings.funding_changenow(transaction_event, "low-amount", chain_id))
    return findings


def provide_handle_transaction(w3):
    def handle_transaction(transaction_event):
        return detect_changenow_funding(w3, transaction_event)

    return handle_transaction


real_handle_transaction = provide_handle_transaction(web3)


def handle_transaction(transaction_event):
    return real_handle_transaction(transaction_event)
