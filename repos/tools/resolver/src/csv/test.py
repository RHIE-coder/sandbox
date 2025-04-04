sheet = [
    "L3 Node Config max-revert-gas-reject 설정 값보다 소모된 gas가 많을 때 Tx 통과 및 생성(설정값+30,000,000)",
    "L3 Node Config max-revert-gas-reject 설정 값보다 소모된 gas가 많을 때 Tx 통과 및 생성(설정값+3,000,000)",
    "L3 Node Config max-revert-gas-reject 설정 값보다 소모된 gas가 많을 때 Tx 통과 및 생성(설정값+300,000))",
    "L3 Node Config max-revert-gas-reject 설정 값보다 소모된 gas가 많을 때 Tx 통과 및 생성(설정값+10,000)",
    "L3 Node Config max-revert-gas-reject 설정 값보다 소모된 gas가 많을 때 Tx 통과 및 생성(설정값+1)",
    "L3 Node Config max-tx-data-size 설정 값보다 발생한 Tx 크기(tx size)가 작을 때 성공 확인(설정값-10,000)",
    "L3 Node Config max-tx-data-size 설정 값보다 발생한 Tx 크기(tx size)가 작을 때 성공 확인(설정값-1,000)",
    "L3 Node Config max-tx-data-size 설정 값보다 발생한 Tx 크기(tx size)가 작을 때 성공 확인(설정값-100)",
    "L3 Node Config max-tx-data-size 설정 값보다 발생한 Tx 크기(tx size)가 작을 때 성공 확인(설정값-10)",
    "L3 Node Config max-tx-data-size 설정 값보다 발생한 Tx 크기(tx size)가 작을 때 성공 확인(설정값-1)",
    "Archive Node 최근 데이터 조회",
    "Archive Node 오래된 데이터 조회(Block Number=100)",
    "Archive Node 오래된 데이터 조회(Block Number=10)",
    "Archive Node 오래된 데이터 조회(Block Number=1)",
    "L3 Service Provider(Fullnode)를 통해 L3 트랜잭션 제출",
    "L3 Service Provider(Fullnode) Blockchain 동기화 확인",
    "L3 Node Config Rollup(롤업) > max-delay 설정에 따른 롤업 체크",
    "(*script) Auto Charger 자동충전 설정 수량보다 적을 때 재충전 동작 확인",
    "(*script) Auto Charger 등록된 자동충전 Account 제거로 충전 불가 확인",
    "(*script) Auto Charger 특정 자산 종류(denom) 자동충전 설정 수량보다 적을 때 재충전 동작 확인",
    "(*script) Auto Charger 등록된 특정 자산 종류(denom) 자동 충전 Account 제거로 충전 불가 확인",
    "ARBOS Network L3 현재 가스 가격(gas price) Tx 수수료 적용 여부 확인",
    "ARBOS Network L3 현재 가스 가격(gas price) 최소 가스 가격(min base price)으로 원복 확인",
    "ARBOS Network L3 Network Fee Account Tx 발생 후 수수료를 받았는지 조회",
    "ARBOS Network 수정된 L3 Network Fee Account Tx 발생 후 수수료를 받았는지 조회",
    "Trezor-Metamask를 통해 Network Fee Account 잔액 증가 확인",
    "L2→L3 DKA Deposit(입금) 성공 동작 확인(0 DKA)",
    "L2→L3 DKA Deposit(입금) 성공 동작 확인(0.000000000000000001 DKA)",
    "L2→L3 DKA Deposit(입금) 성공 동작 확인(0.000000001 DKA)",
    "L2→L3 DKA Deposit(입금) 성공 동작 확인(1 DKA)",
    "L2→L3 DKA Deposit(입금) 성공 동작 확인(전량입금)",
    "L3→L2 DKA Withdraw(출금) 성공 동작 확인 (0 DKA)",
    "L3→L2 DKA Withdraw(출금) 성공 동작 확인 (0.000000000000000001 DKA)",
    "L3→L2 DKA Withdraw(출금) 성공 동작 확인 (0.000000001 DKA)",
    "L3→L2 DKA Withdraw(출금) 성공 동작 확인 (1 DKA)",
    "L3→L2 DKA Withdraw(출금) 성공 동작 확인 (잔량-0.01 DKA)",
    "L3→L2 DKA Withdraw(출금) 동작 후 직접 청구(Claim) 성공 동작 확인(0 DKA)",
    "L3→L2 DKA Withdraw(출금) 동작 후 직접 청구(Claim) 성공 동작 확인(0.000000000000000001 DKA)",
    "L3→L2 DKA Withdraw(출금) 동작 후 직접 청구(Claim) 성공 동작 확인(0.000000001 DKA)",
    "L3→L2 DKA Withdraw(출금) 동작 후 직접 청구(Claim) 성공 동작 확인(1 DKA)",
    "L3→L2 DKA Withdraw(출금) 동작 후 직접 청구(Claim) 성공 동작 확인(잔량-0.01 DKA)",
    "L3 Standard ERC20 입금 전 미배포 상태 확인",
    "L2→L3 Standard ERC20 입금 동작 성공 확인(0 amount)",
    "L2→L3 Standard ERC20 입금 동작 성공 확인(0.000000000000000001 amount)",
    "L2→L3 Standard ERC20 입금 동작 성공 확인(0.000000001 amount)",
    "L2→L3 Standard ERC20 입금 동작 성공 확인(1 amount)",
    "L2→L3 Standard ERC20 입금 동작 성공 확인(전량입금)",
    "L3→L2 Standard ERC20 출금 동작 성공 확인(0 amount)",
    "L3→L2 Standard ERC20 출금 동작 성공 확인(0.000000000000000001 amount)",
    "L3→L2 Standard ERC20 출금 동작 성공 확인(0.000000001 amount)",
    "L3→L2 Standard ERC20 출금 동작 성공 확인(1 amount)",
    "L3→L2 Standard ERC20 출금 동작 성공 확인(전량  출금)",
    "L3→L2 Standard ERC20 출금 후 L2 직접 청구(Claim) 성공 동작 확인(0 amount)",
    "L3→L2 Standard ERC20 출금 후 L2 직접 청구(Claim) 성공 동작 확인(0.000000000000000001 amount)",
    "L3→L2 Standard ERC20 출금 후 L2 직접 청구(Claim) 성공 동작 확인(0.000000001 amount)",
    "L3→L2 Standard ERC20 출금 후 L2 직접 청구(Claim) 성공 동작 확인(1 amount)",
    "L3→L2 Standard ERC20 출금 후 L2 직접 청구(Claim) 성공 동작 확인(전량 출금)",
    "L2 & L3 Custom ERC20 배포 및 Bridge 연결 성공 확인",
    "L2→L3 Custom ERC20 입금 동작 성공 확인(0 amount)",
    "L2→L3 Custom ERC20 입금 동작 성공 확인(0.000000000000000001 amount)",
    "L2→L3 Custom ERC20 입금 동작 성공 확인(0.000000001 amount)",
    "L2→L3 Custom ERC20 입금 동작 성공 확인(1 amount)",
    "L2→L3 Custom ERC20 입금 동작 성공 확인(전량 입금)",
    "L3 Custom ERC20 표준 함수 외 사용자 정의 함수 호출",
    "L3→L2 Custom ERC20 출금 동작 성공 확인(0 amount)",
    "L3→L2 Custom ERC20 출금 동작 성공 확인(0.000000000000000001 amount)",
    "L3→L2 Custom ERC20 출금 동작 성공 확인(0.000000001 amount)",
    "L3→L2 Custom ERC20 출금 동작 성공 확인(1 amount)",
    "L3→L2 Custom ERC20 출금 동작 성공 확인(전량 출금)",
    "L3→L2 Custom ERC20 출금 후 L2 직접 청구 성공 동작 확인 (0 amount)",
    "L3→L2 Custom ERC20 출금 후 L2 직접 청구 성공 동작 확인 (0.000000000000000001 amount)",
    "L3→L2 Custom ERC20 출금 후 L2 직접 청구 성공 동작 확인 (0.000000001 amount)",
    "L3→L2 Custom ERC20 출금 후 L2 직접 청구 성공 동작 확인 (1 amount)",
    "L3→L2 Custom ERC20 출금 후 L2 직접 청구 성공 동작 확인 (전량 출금)",
    "L2 WETH→L3 WETH 입금 동작 성공 확인(0 amount)",
    "L2 WETH→L3 WETH 입금 동작 성공 확인(0.000000000000000001 amount)",
    "L2 WETH→L3 WETH 입금 동작 성공 확인(0.000000001 amount)",
    "L2 WETH→L3 WETH 입금 동작 성공 확인(1 amount)",
    "L2 WETH→L3 WETH 입금 동작 성공 확인(전량 입금)",
    "L3 WETH→L2 WETH 출금 동작 성공 확인(0 amount)",
    "L3 WETH→L2 WETH 출금 동작 성공 확인(0.000000000000000001 amount)",
    "L3 WETH→L2 WETH 출금 동작 성공 확인(0.000000001 amount)",
    "L3 WETH→L2 WETH 출금 동작 성공 확인(1 amount)",
    "L3 WETH→L2 WETH 출금 동작 성공 확인(전량 출금)",
    "L3 WETH→L2 WETH 출금 후 L2 Claim 동작 성공 확인 (0 amount)",
    "L3 WETH→L2 WETH 출금 후 L2 Claim 동작 성공 확인 (0.000000000000000001 amount)",
    "L3 WETH→L2 WETH 출금 후 L2 Claim 동작 성공 확인 (0.000000001 amount)",
    "L3 WETH→L2 WETH 출금 후 L2 Claim 동작 성공 확인 (1 amount)",
    "L3 WETH→L2 WETH 출금 후 L2 Claim 동작 성공 확인 (전량 출금)",
    "L3 WETH→L2 WETH 출금 후 L2 Claim 동작 실패 확인",
    "Teleport L1→L3 DKA 입금 정상 동작 확인(0 DKA)",
    "Teleport L1→L3 DKA 입금 정상 동작 확인(0.000000000000000001 DKA)",
    "Teleport L1→L3 DKA 입금 정상 동작 확인(0.000000001 DKA)",
    "Teleport L1→L3 DKA 입금 정상 동작 확인(1 DKA)",
    "Teleport L1→L3 DKA 입금 정상 동작 확인(전량-0.01 DKA)",
    "(*doc) Teleport  L1→L3 ERC20 입금 정상 동작 확인 (0 amount)",
    "(*doc) Teleport  L1→L3 ERC20 입금 정상 동작 확인 (0.000000000000000001 amount)",
    "(*doc) Teleport  L1→L3 ERC20 입금 정상 동작 확인 (0.000000001 amount)",
    "(*doc) Teleport  L1→L3 ERC20 입금 정상 동작 확인 (1 amount)",
    "(*doc) Teleport  L1→L3 ERC20 입금 정상 동작 확인 (전액 입금)",
    "Multicall DKA 다수에게 전송 확인",
    "(*script) ✅ Multicall DKA 441개 account 전송 확인",
    "(*script) Multicall DKA 50개 account 전송 확인",
    "(*script) Multicall DKA 100개 account 전송 확인",
    "(*script) Multicall DKA 300개 account 전송 확인",
    "(*script) Multicall DKA 500개 account 전송 확인",
    "(*script) Multicall DKA 700개 account 전송 확인",
]

import csv
from pathlib import Path
from pprint import pprint
import re
import chardet
import html2text

file_path = Path.home() / "workspace.me/__temp__/csv/testmo2.csv"

with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())
    print(result['encoding'])  # 예: 'utf-8-sig'


def clean_row(row):
    # 각 셀의 값을 순회하며 \x08 같은 제어 문자를 제거
    return {key: re.sub(r'[\x00-\x1F\x7F]', '', value) for key, value in row.items()}


def get_csv_list():
    row_list = []
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = clean_row(row)
            row_list.append(row)
        
    return row_list

def parse(row):
    return dict(
        folder = row['Folder'],
        case_name = row['Case'],
        case_id = row["Case ID"],
        main_cat = row["Main Category"],
        sub_cat = row["Sub Category"],
        detail_cat = row["Detail Category"],
        summ = row["TC Summary"],
    )

def validate():
    rowlist = get_csv_list()
    print(f"sheet : {len(sheet)}")
    print(f"csv: {len(rowlist)}")
    # origin = [parse(x)["case_name"] for x in rowlist]
    filtered_list = [xx for x in rowlist if (xx := parse(x))["case_name"] in sheet]
    filter_only_name = [x['case_name'] for x in filtered_list]
    print(f"filtered_list: {len(filter_only_name)}")
    get_except = [x for x in sheet if x not in filter_only_name]
    print(f"0 이면 성공 = {len(get_except)}")


def main():
    rowlist = get_csv_list()
    filtered_list = [xx for x in rowlist if (xx := parse(x))["case_name"] in sheet]
    converter = html2text.HTML2Text()
    converter.body_width = 0  # 줄바꿈을 하지 않음
    converter.single_line_break = True  # 문단 사이에 한 줄 개행조차 거부

    for row in filtered_list:
        mark = f"{converter.handle(row['summ'])}"
        result = re.sub(r'^\n+|\n+$', '', mark) 
        print(result)



main()