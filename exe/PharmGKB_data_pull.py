
import pandas as pd
import os
import logzero
import logging
import click

from logzero import logger

from apprissml.apprissml.utils.redshift_connections import redshift_connection
from health.analyses.outcomes_analyses_pdmps.lib.data_pull_queries import *
from genetika_plus.lib import *

pd.set_option('display.width', 2000)
pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 500)
logzero.loglevel(logging.INFO)
os.environ["CREDENTIALS"] = os.path.expanduser('~/.aws/credentials')
REDSHIFT_PARAMS = {'database': 'appriss',
                   'param_file': 'ORSv2/secrets/appriss_crds.txt',
                   'bucket_name': 'health.datasci.corporate.appriss.com',
                   'profile': 'datasci'}


@click.command()
@click.option('--state', default='va', help='')
@click.option('--product', default='Gateway', help='')
# @click.option('--interval', default='730', help='')
@click.option('--schema', default='health_metadata', help='')
def outcomes_analysis_run(product=None, state=None, schema=None):
    conn = redshift_connection(**REDSHIFT_PARAMS)

    # set search path to health_metadata to obtain requested analysis parameters
    set_search_path(schema=schema, conn=conn)

    # output requested analysis parameters as a data frame
    df = pull_user_params(product=product, state=state, conn=conn)

    # pass columns in df as parameters in pre and post data pull queries
    # data_pull(df, conn)
    step_one(df, conn)

    logger.info('\n' + str(df))

    conn.close()


if __name__ == '__main__':
    outcomes_analysis_run()
