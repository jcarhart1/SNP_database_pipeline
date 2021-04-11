
import pandas as pd
import os
import logzero
import logging

from logzero import logger

# from genetika_plus.database_connections import postgres_connection
from genetika_plus.lib import step_one_download_unzip_extract

pd.set_option('display.width', 2000)
pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 500)
logzero.loglevel(logging.INFO)
os.environ["CREDENTIALS"] = os.path.expanduser('~/.aws/credentials')
REDSHIFT_PARAMS = {'database': 'genetika',
                   'param_file': 'ORSv2/secrets/appriss_crds.txt',
                   'bucket_name': 'health.datasci.corporate.appriss.com',
                   'profile': 'datasci'}


def pharm_gkb_db_update_run():
    conn = postgres_connection(**REDSHIFT_PARAMS)

    # pass columns in df as parameters in pre and post data pull queries
    # data_pull(df, conn)
    step_one_download_unzip_extract()

    logger.info('\n' + str(df))

    conn.close()


if __name__ == '__main__':
    outcomes_analysis_run()
