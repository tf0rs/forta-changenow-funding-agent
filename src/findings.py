from forta_agent import Finding, FindingType, FindingSeverity
from .constants import *

class FundingChangenowFindings:

    def funding_changenow(transaction, type, chain_id):
        if type=="new-eoa":
            finding = Finding({
                'name': 'Changenow Funding',
                'description': f'{transaction.to} received initial funds from ChangeNow',
                'alert_id': 'FUNDING-CHANGENOW-NEW-ACCOUNT',
                'type': FindingType.Info,
                'severity': FindingSeverity.Low,
                'protocol': PROTOCOLS[chain_id],
                'addresses': list(transaction.addresses.keys()),
                'metadata': {
                    "amount funded": f"{transaction.transaction.value / 10e17} {CURRENCIES[chain_id]}",
                    "receiving address": f"{transaction.to}"
                }
            })
        else:
            finding = Finding({
                'name': 'Changenow Funding',
                'description': f'{transaction.to} received a low amount of funds from ChangeNow',
                'alert_id': 'FUNDING-CHANGENOW-LOW-AMOUNT',
                'type': FindingType.Info,
                'severity': FindingSeverity.Low,
                'protocol': PROTOCOLS[chain_id],
                'addresses': list(transaction.addresses.keys()),
                'metadata': {
                    "agent threshold": f"{CHANGENOW_THRESHOLD[chain_id]} {CURRENCIES[chain_id]}",
                    "amount funded": f"{transaction.transaction.value / 10e17} {CURRENCIES[chain_id]}",
                    "receiving address": f"{transaction.to}"
                }
            })
        return finding