import asyncio

async def wait_util_sigint():
    print("브라우저가 멈춘 상태로 유지됩니다. 종료하려면 Ctrl+C를 누르세요.")
    try:
        await asyncio.Event().wait()  # 무기한 대기
    except asyncio.CancelledError:
        print("대기 중이던 작업이 취소되었습니다.")  # 작업이 취소되었을 때의 메시지
    except KeyboardInterrupt:
        print("종료됨")  # Ctrl+C가 눌려 프로그램이 종료될 때의 메시지
    finally:
        print("프로그램이 종료됩니다.")  # 프로그램 종료 후 출력