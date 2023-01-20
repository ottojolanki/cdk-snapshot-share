import boto3
import logging
import re



logging.basicConfig(
    level=logging.INFO,
    force=True
)

SHARE_TO_ACCOUNTS=['618537831167'] #cherry-lab for testing

def get_rds_client():
    return boto3.client('rds')

def share_snapshot_to_accounts(accounts: list,
                               snapshot_id: str,
    ) -> None:
    client = get_rds_client()
    response = client.modify_db_snapshot_attribute(
        DBSnapshotIdentifier=snapshot_id,
        AttributeName='restore',
        ValuesToAdd=accounts)

def strip_snapshot_id(snapshot_id: str) -> str:
    return re.sub('^rds\:', '', snapshot_id)

def share_snapshot(event, context):
    print('Hello from sharing snapshot')
    latest_rds_snapshot_id = event['copy_latest_rds_snapshot']
    shareable_id = strip_snapshot_id(latest_rds_snapshot_id)
    print(f'Sharing snapshot: {shareable_id}')
    share_snapshot_to_accounts(
        accounts=SHARE_TO_ACCOUNTS,
        snapshot_id=shareable_id,
    )
    return shareable_id

