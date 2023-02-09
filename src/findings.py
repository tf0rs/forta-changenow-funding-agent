from forta_agent import Finding, FindingType, FindingSeverity
from src.constants import *

class FundingChangenowFindings:

    def funding_changenow(transaction, type, anomaly_score, chain_id):
        if type=="new-eoa":
            finding = Finding({
                'name': 'Changenow Funding',
                'description': f'{transaction.to} received initial funds from ChangeNOW',
                'alert_id': 'FUNDING-CHANGENOW-NEW-ACCOUNT',
                'type': FindingType.Info,
                'severity': FindingSeverity.Low,
                'protocol': PROTOCOLS[chain_id],
                'addresses': list(transaction.addresses.keys()),
                'metadata': {
                    "amount funded": f"{transaction.transaction.value / 10e17} {CURRENCIES[chain_id]}",
                    "receiving address": f"{transaction.to}",
                    "anomaly_score": anomaly_score
                }
            })
        else:
            finding = Finding({
                'name': 'Changenow Funding',
                'description': f'{transaction.to} received a low amount of funds from ChangeNOW',
                'alert_id': 'FUNDING-CHANGENOW-LOW-AMOUNT',
                'type': FindingType.Info,
                'severity': FindingSeverity.Low,
                'protocol': PROTOCOLS[chain_id],
                'addresses': list(transaction.addresses.keys()),
                'metadata': {
                    "agent threshold": f"{CHANGENOW_THRESHOLD[chain_id]} {CURRENCIES[chain_id]}",
                    "amount funded": f"{transaction.transaction.value / 10e17} {CURRENCIES[chain_id]}",
                    "receiving address": f"{transaction.to}",
                    "anomaly_score": anomaly_score
                }
            })
        return finding