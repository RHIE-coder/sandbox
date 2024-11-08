#!/bin/bash
# echo -e "\033[0;37;41mThis is white text on red background\033[0m"

# 시작/리셋 코드
COLOR='\033[' # escape=\033, seqence-start=[
_m='m' # control character
RESET='\033[0m'

# 텍스트 스타일
PLAIN="${COLOR}0"
BOLD="${COLOR}0"
DIM="${COLOR}0"
ITALIC="${COLOR}0" # 지원되지 않는 터미널이 많음
UNDERLINE="${COLOR}0"
BLINK="${COLOR}0"
REVERSE="${COLOR}0"
HIDDEN="${COLOR}0"


# 텍스트 색상
BLACK='30'
RED='31'
GREEN='32'
YELLOW='33'
BLUE='34'
MAGENTA='35'
CYAN='36'
WHITE='37'

# 배경 색상
BG_BLACK='40'
BG_RED='41'
BG_GREEN='42'
BG_YELLOW='43'
BG_BLUE='44'
BG_MAGENTA='45'
BG_CYAN='46'
BG_WHITE='47'

