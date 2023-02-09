CHANGENOW_ADDRESSES = {
    1: ['0x077d360f11d220e4d5d831430c81c26c9be7c4a4'],
    56: ['0x975d9bd9928f398c7e01f6ba236816fa558cd94b', '0xa96be652a08d9905f15b7fbe2255708709becd09'],
    137: ['0x3a0d24d59af3a3444dc6ef12cdb0c6e38c985288']
}

"""
At the time of deployment, thresholds are at ~$150 based on the value of the tokens. It's difficult to optimize this number, but
it should help interpretability of results to have them standard across all chains. (Based on feedback from Forta TRi participants.)
"""
CHANGENOW_THRESHOLD = {
    1: 0.09,
    56: 0.5,
    137: 115
}

PROTOCOLS = {
    1: 'ethereum',
    56: 'binance smart chain',
    137: 'polygon'
}

CURRENCIES = {
    1: "ETH",
    56: "BSC",
    137: "MATIC"
}