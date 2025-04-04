# context = await browser.new_context(
#     screen=dict(
#         width=1920,
#         height=1080,
#     ),
#     viewport=dict(
#         width=1920,
#         height=1080,
#     )
# )

# page = await context.new_page()


###########################################################################

# async def has_before(clickable):
#     is_included_before = await clickable.evaluate("""
#     (element) => {
#         const style = window.getComputedStyle(element, '::before');
#         return style.content !== 'none' && style.content !== '';  // ::before의 content 확인
#     }
#     """)
#     return is_included_before

###########################################################################

# async def wait_for_no_overlay():
#     overlay = page.locator('.blockUI.blockOverlay')
#     await overlay.wait_for(state="detached", timeout=5000)

###########################################################################

import sys
import importlib

def reload_all(module_names):
    """
    특정 모듈 및 하위 의존 모듈을 재귀적으로 reload합니다.
    """
    for module_name in list(sys.modules.keys()):
        if any(module_name.startswith(name) for name in module_names):
            try:
                importlib.reload(sys.modules[module_name])
                print(f"Reloaded: {module_name}")
            except Exception as e:
                print(f"Failed to reload {module_name}: {e}")

# 사용 예시: 'runtime' 패키지 및 관련 모듈 재로드
reload_all(["testmo_automation"])

###########################################################################

import sys
from pathlib import Path

# Add the 'src' directory to the Python path
sys.path.append(str(Path().resolve().parent / 'src'))
print(sys.path)

###########################################################################

async def wait_for_difference(stale_data_id):
    print("wait_for_difference")
    retries = 10
    interval = 0.5
    print(await not_expanded_list.count())
    while await not_expanded_list.first.get_attribute('data-id')  == stale_data_id:
        print(await not_expanded_list.first.get_attribute('data-id'), stale_data_id)
        await asyncio.sleep(interval)
        retries-=1
        if retries == 0:
            raise Exception("retry over")