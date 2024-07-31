# device 옵션 설정 시 Firefox 에러
 - chromium, webkit은 `isMobile()` 함수가 지원되지만 firefox는 지원되지 않아서 생기는 문제

```sh
ERROR tests/test_example.py::test_has_title[firefox] - playwright._impl._errors.Error: Browser.new_context: options.isMobile is not supported in Firefox
ERROR tests/test_example.py::test_get_started_link[firefox] - playwright._impl._errors.Error: Browser.new_context: options.isMobile is not supported in Firefox
```