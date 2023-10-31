# This is the Main Program, ver2 is an OOP implementation of a stock for easier sorting
# 	and implementation after pulling the json file from the API

import stock as s
import funcs as f

curr_client = f.ff_login()
f.get_account_positions(curr_client)