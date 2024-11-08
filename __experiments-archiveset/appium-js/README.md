# MacOS 전용

---

# [Brew]
 - [Homebrew Page](https://brew.sh/)

## 설치
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'export PATH="/opt/homebrew/opt/bin"' >> ~/.zshrc
source ~/.zshrc
```

## 확인
```sh
brew --version
```

## 삭제
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh)"
```

---

# [JAVA 설치]

## 설치
```sh
brew install openjdk@21
sudo ln -sfn /opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-21.jdk
echo 'export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## 확인
```sh
java --version
javac --version
```

## 삭제
```sh
brew uninstall openjdk@21
```

# [Android Studio 설치]

## 설치
1. 사이트에 들어가서 설치 진행
 - [Android Studio Developer](https://developer.android.com/studio)
2. 설치된 앱 실행
3. Android Studio Setup Wizard를 통해 SDK 구성 요소들 설치
4. 설치 완료되면 닫기
5. 스크립트 실행
```sh
echo 'export ANDROID_HOME=~/Library/Android/sdk' >> ~/.zshrc
echo 'export PATH=$ANDROID_HOME:$PATH' >> ~/.zshrc
echo 'export PATH=$ANDROID_HOME/emulator:$PATH' >> ~/.zshrc
echo 'export PATH=$ANDROID_HOME/tools:$PATH' >> ~/.zshrc
echo 'export PATH=$ANDROID_HOME/platform-tools:$PATH' >> ~/.zshrc
source ~/.zshrc
```

## 확인
```sh
adb --version
```

## 삭제
```sh
# 어플리케이션 삭제
rm -rf /Applications/Android\ Studio.app
# 환경설정 삭제
rm -Rf ~/Library/Preferences/AndroidStudio*
# .plist(프로퍼티 리스트) 파일 삭제
rm -Rf ~/Library/Preferences/com.google.android.*
# 애뮬레이터 .plist 삭제
rm -Rf ~/Library/Preferences/com.android.*
# 플러그인 삭제
rm -Rf ~/Library/Application\ Support/AndroidStudio*
# 로그 삭제
rm -Rf ~/Library/Logs/AndroidStudio*
# 캐시 삭제
rm -Rf ~/Library/Caches/AndroidStudio*
# 이전 버전 삭제
rm -Rf ~/.AndroidStudio*
# AVD 및 키 저장소 삭제
rm -Rf ~/.android
# SDK 도구 삭제
rm -Rf ~/Library/Android*
# 인증 토큰 삭제
rm -Rf ~/.emulator_console_auth_token
```

---

# [Node.js 설치]

## 설치
```sh
brew install node@20
echo 'export PATH="/opt/homebrew/opt/node@20/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## 확인
```sh
node -v
npm -v
```

## 삭제
```sh
brew uninstall node@20
```

---

# [Appium 설치]

## 설치
```sh
sudo npm i -g appium
appium driver list 
```


## 확인
```sh
appium --version
```

## 삭제
```sh
rm -rf ~/.appium
npm uninstall -g appium
```

### Android
 - 설치
```sh
appium driver install uiautomator2
```

 - 확인
```sh
appium driver list
```

### iOS
 - 설치
```sh
appium driver install xcuitest
```

 - 확인
```sh
appium driver list
```

  - 설치중 아래와 같은 에러 발생시 다음 명령어 실행
```sh
sudo chown -R 501:20 ~/.npm"
```
```sh
✖ Installing 'xcuitest' using NPM install spec 'appium-xcuitest-driver'
Error: ✖ Encountered an error when installing package: npm command 'install --save-dev --no-progress --no-audit --omit=peer --save-exact --global-style --no-package-lock appium-xcuitest-driver --json' failed with code 1.

STDOUT:
{
  "error": {
    "code": "EACCES",
    "summary": "\nYour cache folder contains root-owned files, due to a bug in\nprevious versions of npm which has since been addressed.\n\nTo permanently fix this problem, please run:\n  sudo chown -R 501:20 \"/Users/rhiemh/.npm\"",
    "detail": ""
  }
}

STDERR:
npm warn config global-style This option has been deprecated in favor of `--install-strategy=shallow`
npm warn ERESOLVE overriding peer dependency
npm warn While resolving: appium-android-driver@9.8.0
npm warn Found: appium@undefined
npm warn node_modules/appium
npm warn
npm warn Could not resolve dependency:
npm warn peer appium@"^2.0.0" from appium-android-driver@9.8.0
npm warn node_modules/appium-uiautomator2-driver/node_modules/appium-android-driver
npm warn   appium-android-driver@"^9.8.0" from appium-uiautomator2-driver@3.7.4
npm warn   node_modules/appium-uiautomator2-driver
npm error code EACCES
npm error syscall open
npm error path /Users/rhiemh/.npm/_cacache/index-v5/5c/30/7960b75ace61e8a617c892beb3ac4255ca27a18a7137f4a5632a5415e563
npm error errno EACCES
npm error
npm error Your cache folder contains root-owned files, due to a bug in
npm error previous versions of npm which has since been addressed.
npm error
npm error To permanently fix this problem, please run:
npm error   sudo chown -R 501:20 "/Users/rhiemh/.npm"
```

---

# [Appium Inspector 설치]

## 설치
[appium-inspector](https://github.com/appium/appium-inspector/releases)
 - Mac M 시리즈(실리콘 칩): mac-arm64.dmg

## 실행
```
‘Appium Inspector’은(는) Apple에서 악성 소프트웨어가 있는지 확인할 수 없기 때문에 열 수 없습니다.
```
 - Finder에서 보기
 - 오른쪽 마우스 클릭
 - 열기

```
‘Appium Inspector’은(는) Apple에서 악성 소프트웨어가 있는지 확인할 수 없기 때문에 열 수 없습니다.
```
 - 열기

### Android
#### 터미널 실행 후 아래 과정 실행
```sh
appium
```

#### 다른 터미널 실행 후 아래 과정 실행
1. 안드로이드 기기 연결 후 디바이스 정보 확인(개발자 옵션>USB 디버깅)
2. 디바이스 연결 확인
```sh
adb devices
```
3. Appium Inspector 접속
 - 아래 JSON Representation 정보 입력 후 `Start Session`
```json
{
  "appium:deviceName": "<adb devices로 얻은 정보>", 
  "platformName": "Android",
  "appium:automationName": "uiautomator2"
}
```

### iOS
#### 터미널 실행 후 아래 과정 실행(이미 서버가 실행 중이면 SKIP)
```sh
# appium 서버 실행
appium
```

#### 다른 터미널 실행 후 아래 과정 실행
1. iOS 기기 연결 후 디바이스 정보 확인(개인정보 보호 및 보안>개발자 모드>켬)
  - [개발자 모드가 안보이면 Force Restart](https://www.magfone.com/repair-ios/iphone-developer-mode-not-showing.html)
2. SDK 확인
```sh
xcodebuild -showsdks
```
3. iOS 디바이스 연결 확인
  - Xcode 실행: [Window] - [Devices and Simulators]
    - 기다리기 `Copying shared cache symbols from XXX iPhone (XX% completed)`
  - 연결 디바이스 확인
```sh
xcrun xctrace list devices
```
4. WebDriverAgent 설정 에디터 열기
```sh
appium driver run xcuitest open-wda
```
5. 각 Target의 `Signing & Capabilities` 설정
 - WebDriverAgentLib
   - Team -> Add Account...
   - Bundle Identifier 수정
 - WebDriverAgentRunner
   - Team -> Add Account...
   - Bundler Identifier 수정
 - IntergrationApp
   - Team -> Add Account...
   - Bunlde Identifier 수정
6. Targets 선택: WebDriverAgentRuner
  - Product > Test
7. iOS 디바이스 설정
 - 일반 > VPN 및 기기 관리
   - 인증서 클릭 후 신뢰하기
8. codesign 접근 허용
9. Appium Inspector 접속
 - 아래 JSON Representation 정보 입력 후 `Start Session`
```json
{
  "appium:udid": "<Identifier>",
  "platformName": "iOS",
  "appium:automationName": "XCUITest"
}
```

## 삭제
`/Applications/Appium Inspector.app`

---

# [xcode 설치]

## 설치
[AppStore: Xcode](https://apps.apple.com/kr/app/xcode/id497799835?mt=12)

## 설정
```sh
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```
---










































---

# [Python 설치]

## 설치
```sh
brew install python@3.12
```

## 확인
```sh
python3 --version
```

## 삭제
```sh
brew uninstall python@3.12
```


