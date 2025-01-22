from rich.console import Console

console = Console()

class Mediator:
    def __init__(self):
        self.testcases = {}  # 테스트케이스와 precondition 매핑
        self.results = {}    # 테스트케이스 실행 결과 저장
        self.status = {}     # 각 테스트케이스 상태: "pending", "running", "completed"

    def register_testcase(self, name, testcase, preconditions=None):
        """테스트케이스를 등록한다."""
        if name in self.testcases:
            raise ValueError(f"Testcase '{name}' is already registered.")
        self.testcases[name] = {
            "testcase": testcase,
            "preconditions": set(preconditions or [])
        }
        self.results[name] = None
        self.status[name] = "pending"  # 초기 상태

    def run_testcase(self, name):
        console.print(f"{name}")
        """단일 테스트케이스를 실행."""
        if self.status[name] == "completed":
            return  # 이미 완료된 테스트
        if self.status[name] == "running":
            print(f"Skipping: {name} (Already in progress to avoid infinite loop)")
            return  # 순환 참조 방지

        print(f"Checking preconditions for: {name}")
        self.status[name] = "running"

        # Precondition 실행
        for pre in self.testcases[name]["preconditions"]:
            self.run_testcase(pre)

        # 현재 테스트케이스 실행
        print(f"Running: {name}")
        self.results[name] = self.testcases[name]["testcase"]()
        self.status[name] = "completed"
        print('='*30)

    def run(self):
        """모든 테스트케이스를 실행."""
        for name in self.testcases:
            if self.status[name] == "pending":
                self.run_testcase(name)
                
def testcase_1():
    print("Executing Testcase 1")
    return True  # 성공

def testcase_2():
    print("Executing Testcase 2")
    return True  # 성공

def testcase_3():
    print("Executing Testcase 3")
    return True  # 성공

def testcase_4():
    print("Executing Testcase 4")
    return True  # 성공

# Mediator 사용
mediator = Mediator()

# 테스트케이스 등록
mediator.register_testcase("Testcase 1", testcase_1, preconditions=["Testcase 4", "Testcase 3"])
mediator.register_testcase("Testcase 2", testcase_2, preconditions=["Testcase 1"])
mediator.register_testcase("Testcase 3", testcase_3, preconditions=["Testcase 1", "Testcase 2"])
mediator.register_testcase("Testcase 4", testcase_4)

# 테스트 실행
mediator.run()