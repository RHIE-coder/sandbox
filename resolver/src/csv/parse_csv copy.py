import csv
import configparser
from pathlib import Path
from pprint import pprint

properties = configparser.ConfigParser()
properties.read('.env.ini')
env = properties['csv']
origin_url = env['TESTMO_URL']
file_path = Path.home() / "workspace.me/__temp__/csv/testmo.csv"

group_ids = {
    'DKA Deposit-Withdraw': 136,
    'L3 Node Config': 137,
    'Sequencer Feed': 138,
    'Relayer': 139,
    'Standard ERC20 Deposit-Withdraw': 140,
    'Custom ERC20 Deposit-Withdraw': 141,
    'Teleport': 142,
    'Network Gas Fee': 143,
    'Network Fee Account': 144,
    'Status Monitor': 145,
    'SQM': 146,
    'Node Interface Check': 147,
    'Retryable Ticket': 148,
    'WETH Deposit-Withdraw': 149,
    'Auto Charger': 150,
    'ETH 기반 Admin / User Validator 구축': 151,
    'ETH 기반 fraud-proof 동작확인 simulator 개발': 152,
    'ETH 기반 Validator Library 개발': 153,
    'Trezor Hardware Wallet': 154,
    'Block Snapshot': 155,
    'Archive Node': 156,
    'Multicall': 157,
    'Delayed Inbox': 158,
    'Tx Simulator': 159,
}

except_to_print = {
    'L3 Node Config': False,
    'Node Interface Check': False,
    # 'Retryable Ticket': False,
    'Delayed Inbox': False,
    'Tx Simulator': False,

    'Trezor Hardware Wallet': True,
    'Network Fee Account': True,
    'WETH Deposit-Withdraw': True,
    'Network Gas Fee': True,
    'Archive Node': True,
    'Teleport': True,
    'Custom ERC20 Deposit-Withdraw': True,
    'Standard ERC20 Deposit-Withdraw': True,
    'DKA Deposit-Withdraw': True,
    'Block Snapshot': True,
    'Multicall': True,
    'Status Monitor': True,
    'Auto Charger': True,
    'SQM': True,
    'Sequencer Feed': True,
    'Relayer': True,
    'ETH 기반 Admin / User Validator 구축': True,
    'ETH 기반 fraud-proof 동작확인 simulator 개발': True,
    'ETH 기반 Validator Library 개발': True,
}

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    folders = set()
    infomap = dict()
    count=0

    print(next(reader).keys())
    print()
    for row in reader:
        count+=1
        folder = row['Folder']
        case_name = row['\ufeff"Case"']
        case_id = row["Case ID"]
        folders.add(folder)
        info = f"{folder} > [{case_name}]({origin_url}?group_id={group_ids[folder]}&case_id={case_id})"
        if not infomap.get(folder):
            infomap[folder] = list()
        infomap[folder].append(info)
    
    for folder in infomap.keys():
        try:
            if not except_to_print[folder]:
                infolist = infomap[folder]
                for info in infolist:
                    print(info)
        except:
            continue
    
    print(f"[총 TC 개수]:{count}")