# ChangeNow Funding Agent

## Description

This agent detects transactions in the native currency from ChangeNow hot wallets to new EOA addresses, and to any address when the amount sent is under a certain threshold.

## Supported Chains

- Ethereum
- Binance Smart Chain
- Polygon

## Alerts

Describe each of the type of alerts fired by this agent

- FUNDING-CHANGENOW-NEW-ACCOUNT
  - Fired when a transaction from the ChangeNow hot wallet is to a new EOA address
  - Severity is always set to "low"
  - Type is always set to "info"
  - Metadata includes the amount funded, and the receiving address

- FUNDING-CHANGENOW-LOW-AMOUNT
  - Fired when a transaction from the ChangeNow hot wallet is under a certain threshold
  - Severity is always set to "low"
  - Type is always set to "info"
  - Metadata includes the threshold for this agent, the amount funded, and the receiving address

## Test Data

The agent behaviour can be verified with the following transactions:

- 0xc4af34bc84bbdda599ccf915a9c6cb62481899086767480212a4b28f4636c0f7 (new EOA address)
- 0x25678c1fd55f14c6a04e6c54c21bf13b51d84974db8299dafe86dd755d3a6b64 (low funding amount)
