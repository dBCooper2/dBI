#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Positions Object: Contains Data from get_account() API calls
class Position:
    def __init__(self, position_data: dict):
        self.symbol = position_data['instrument']['symbol']
        self.cusip = position_data['instrument']['cusip']
        self.type = position_data['instrument']['assetType']

        self.shortQuantity = position_data['shortQuantity'] # exclude when --no-balances == True
        self.averagePrice = position_data['averagePrice'] # exclude when --no-balances == True
        self.currentDayCost = position_data['currentDayCost']
        self.currentDayProfitLoss = position_data['currentDayProfitLoss'] # exclude when --no-balances == True
        self.currentDayProfitLossPercentage = position_data['currentDayProfitLossPercentage']
        self.longQuantity = position_data['longQuantity'] # exclude when --no-balances == True
        self.settledLongQuantity = position_data['settledLongQuantity'] # exclude when --no-balances == True
        self.settledShortQuantity = position_data['settledShortQuantity'] # exclude when --no-balances == True
        self.marketValue = position_data['marketValue'] # exclude when --no-balances == True
        self.maintenanceRequirement = position_data['maintenanceRequirement']
        self.previousSessionLongQuantity = position_data['previousSessionLongQuantity'] # exclude when --no-balances == True

