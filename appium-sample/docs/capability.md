

# Android

```json
{
  "appium:deviceName": "ce10171ab8c35a4004",
  "platformName": "Android",
  "appium:automationName": "uiautomator2",
  "appium:appPackage": "com.sec.android.app.popupcalculator",
  "appium:appActivity": "com.sec.android.app.popupcalculator.Calculator"
}
```

# IOS

```json
{
  "appium:udid":"00008120-001C30263E82201E",
  "platformName":"iOS",
  "appium:automationName":"XCUITest"
}
```

```
devmodectl streaming
xcodebuild -showsdks
xcrun simctl list devices
xcrun -v xcdevice list
xcrun xcdevice list
xcrun xcdevice observe --both
xcrun -v xcdevice list

npm root -g
# /usr/local/lib/node_modules
```

```json

```

## 설정에서 개발자 모드가 안보이면

 - 업데이트 체크(16버전 이상)
 - 강제 재시작

https://www.magfone.com/repair-ios/iphone-developer-mode-not-showing.html

## xcodebuild ERROR

 - 현상
```
xcode-select: error: tool 'xcodebuild' requires Xcode, but active developer directory '/Library/Developer/CommandLineTools' is a command line tools instance
```
 - 해결: active developer 디렉토리 경로 재지정
```
xcode-select -s /Applications/Xcode.app/Contents/Developer
```

 - 추가 정보
https://stackoverflow.com/questions/1480184/how-do-i-determine-which-ios-sdk-i-have