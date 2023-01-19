import boto3

import logging



logging.basicConfig(
    level=logging.INFO,
    force=True
)

SHARE_TO_ACCOUNTS=['618537831167'] #cherry-lab for testing

def get_rds_client():
    return boto3.client('rds')

def share_snapshot_to_accounts(accounts: list,
                               snapshot_id: str,
    ):
    client = get_rds_client()
    response = client.modify_db_snapshot_attribute(
        DBSnapshotIdentifier=snapshot_id,
        AttributeName='restore',
        ValuesToAdd=accounts)


def share_snapshot(event, context):
    pass
