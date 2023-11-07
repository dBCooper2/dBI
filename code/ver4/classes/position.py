from tda.client import Client
import pandas as pd

# Example Position
""" 
{'shortQuantity': 0.0, 
		'averagePrice': 0.0, 
		'currentDayCost': 0.0, 
		'currentDayProfitLoss': 0.0, 
		'currentDayProfitLossPercentage': 0.0, 
		'longQuantity': 0.0, 
		'settledLongQuantity': 0.0, 
		'settledShortQuantity': 0.0, 
		'instrument': { --------------------------> 2. DELETE
			'assetType': 'EQUITY', ---------------> 3. ADD 1 LAYER HIGHER IN THE DICT
			'cusip': '58933Y105', 
			'symbol': 'MRK' ----------------------> 1. PULL
			}, 
		'marketValue': 0.0, 
		'maintenanceRequirement': 0.0, 
		'previousSessionLongQuantity': 0.0
		}
"""

class Position:
    def __init__(self, position_dict)->pd.DataFrame:
        self.symbol = position_dict['instrument']['symbol']
        position_dict['assetType'] = position_dict['instrument']['assetType'] # Put Asset Type in the dict before deleting the 'instrument' sub-dict
        # add cusip storage here if you need it later

        # delete the instruments sub-dict
        del position_dict['instrument']
