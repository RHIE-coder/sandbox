import { test, expect } from "@playwright/test";
import { Login } from "./pages/login.page.js";
import { SignUp } from "./pages/signup.page.js";

test("login -> 회원가입 화면 이동", async ({ page }) => {
  const login = new Login(page);
  await login.goto();

  await test.step("회원가입 링크 문구 동작 확인", async () => {
    await login.signUpLink();
  });
});

test("login 실패 시나리오", async ({ page }) => {
  const login = new Login(page);
  await login.goto();

  await test.step("로그인 버튼 활성 상태 확인", async () => {
    await login.signInButtonStatus();
  });

  await test.step("username 입력 확인", async () => {
    await login.usernameInput("hello world");
  });

  await test.step("password 입력 확인", async () => {
    await login.passwordInput("1234");
  });

  await test.step("remeber checkbox 입력 확인", async () => {
    await login.rememberMeCheckbox();
  });

  await test.step("로그인 버튼 동작 확인", async () => {
    await login.signInButton();
  });
});
  
test("signup 도움말 문구 시나리오", async ({ page }) => {
  const signup = new SignUp(page);
  await signup.goto()

  await test.step("firstName 도움말 확인", async () => {
    await signup.firstNameHelper()
  });
  await test.step("lastName 도움말 확인", async () => {
    await signup.lastNameHelper()
  });
  await test.step("username 도움말 확인", async () => {
    await signup.usernameHelper()
  });
  await test.step("password 도움말 확인", async () => {
    await signup.passwordHelper()
  });
  await test.step("confirmPassword 도움말 확인", async () => {
    await signup.confirmPasswordHelper()
  });
});

test("signup 입력 시나리오", async ({ page }) => {
  const signup = new SignUp(page);
  await signup.goto()

  await test.step("firstName 입력 확인", async () => {
    await signup.firstNameInput("edward")
  });
  await test.step("lastName 입력 확인", async () => {
    await signup.lastNameInput("RHIE")
  });
  await test.step("username 입력 확인", async () => {
    await signup.usernameInput("eddie3")
  });
  await test.step("password 입력 확인", async () => {
    await signup.passwordInput("1234")
  });
  await test.step("confirmPassword 입력 확인", async () => {
    await signup.confirmPasswordInput("1234")
  });
  await test.step("회원가입 버튼 동작 확인", async () => {
    await signup.signInButton()
  });
});

// test("login 성공 시나리오", async ({ page }) => {
//   const login = new Login(page);
//   await login.goto();

//   await test.step("로그인 버튼 활성 상태 확인", async () => {
//     await login.signInButtonStatus();
//   });

//   await test.step("username 입력 확인", async () => {
//     await login.usernameInput("eddie2");
//   });

//   await test.step("password 입력 확인", async () => {
//     await login.passwordInput("1234");
//   });

//   await test.step("remeber checkbox 입력 확인", async () => {
//     await login.rememberMeCheckbox();
//   });

//   await test.step("로그인 버튼 동작 확인", async () => {
//     await login.signInButton();
//   });
// });