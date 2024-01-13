import sqlite3 as db
import pandas as pd
import logging as l

class DatabaseManager_SQLite:
    def __init__(self, db_name: str) -> None:
        self.conn = db.connect(db_name)
        l.info('Database Connection Established.')
        self.cur = self.conn.cursor()
        l.info('Cursor Created.')


    def insert_data(self, table_name: str, df:pd.DataFrame):
        l.info('Attempting DataFrame to_sql() method...')
        try:
            df.to_sql(table_name, self.conn, if_exists='append')
            l.info('to_sql succeeded, committing changes...')
            self.conn.commit()
        except Exception as e:
            l.error('to_sql() Failed! Rolling Back Changes...')
            print(e)
            self.conn.rollback()
            l.info('Changes Rolled Back')
        else:
            self.conn.close()
            exit()


    def close_db(self):
        l.info('Committing Changes and Closing...')
        self.conn.commit()
        self.conn.close()
        l.info('Changes Committed, DB Connection Closed.')

"""
# Add Later if Applicable:
        # add code to create the tables here
        pos_create_str = 
        CREATE TABLE IF NOT EXISTS positions(
            shortQuantity type,
            averagePrice type,
            currentDayCost type,
            currentDayProfitLoss type,
            currentDayProfitLossPercentage type,
            longQuantity type,
            settledLongQuantity type,
            settledShortQuantity type,
            marketValue type,
            maintenanceRequirement type,
            previousSessionLongQuantity type,
            symbol type,
            cusip type,
            assetType type,
            agedQuantity type,
            date_accessed type
        )
        
        inst_create_str = 
        CREATE TABLE IF NOT EXISTS instruments(
            symbol type,
            high52 type,
            low52 type,
            dividendAmount type,
            dividendYield type,
            dividendDate type,
            peRatio type,
            pegRatio type,
            pbRatio type,
            prRatio type,
            pcfRatio type,
            grossMarginTTM type,
            grossMarginMRQ type,
            netProfitMarginTTM type,
            netProfitMarginMRQ type,
            operatingMarginTTM type,
            operatingMarginMRQ type,
            returnOnEquity type,
            returnOnAssets type,
            returnOnInvestment type,
            quickRatio type,
            currentRatio type,
            interestCoverage type,
            totalDebtToCapital type,
            ltDebtToEquity type,
            totalDebtToEquity type,
            epsTTM type,
            epsChangePercentTTM type,
            epsChangeYear type,
            epsChange type,
            revChangeYear type,
            revChangeTTM type,
            revChangeIn type,
            sharesOutstanding type,
            marketCapFloat type,
            marketCap type,
            bookValuePerShare type,
            shortIntToFloat type,
            shortIntDayToCover type,
            divGrowthRate3Year type,
            dividendPayAmount type,
            dividendPayDate type,
            beta type,
            vol1DayAvg type,
            vol10DayAvg type,
            vol3MonthAvg type,
            cusip type,
            description type,
            assetType type
        )
        self.cur.execute(pos_create_str)
        print('positions table_created')
        self.cur.execute(inst_create_str)
        print('instruments table created')

dbm = DatabaseManager_SQLite('test')
dbm.close_db()
"""