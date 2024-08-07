import { expect } from "@playwright/test";
import { RealWorldApp } from "./context.js";

export class SignUp extends RealWorldApp {
  inject() {}

  async goto() {
    await this.page.goto(this.routePath("/signup"));
  }

  /**
   * firstName 입력 확인
   * */
  async firstNameInput(firstName) {
    const id = "TC1";
    this.testcase(id, "firstName 입력 확인");
    try {
      const $firstName = await this.page.locator("#firstName");
      await $firstName.fill(firstName);
      await expect($firstName).toHaveValue(firstName);
      this.ok(id);
    } catch (e) {
      this.fail(id, "firstName 입력 안됨");
    }
  }

  /**
   * firstName 도움말 확인
   * */
  async firstNameHelper() {
    const id = "TC2";
    this.testcase(id, "firstName 도움말 확인");
    try {
      const $title = await this.page.locator("h1", {
        hasText: "Sign Up",
      });
      const $firstName = await this.page.locator("#firstName");
      await $firstName.focus();
      await $title.click();
      const $firstNameHelper = await this.page.locator(
        "#firstName-helper-text"
      );
      expect($firstNameHelper).toBeVisible();
      this.ok(id);
    } catch (e) {
      this.fail(id, "firstName 도움말 없음");
    }
  }

  /**
   * lastName 입력 확인
   * */
  async lastNameInput(lastName) {
    const id = "TC3";
    this.testcase(id, "lastName 입력 확인");
    try {
      const $lastName = await this.page.locator("#lastName");
      await $lastName.fill(lastName);
      await expect($lastName).toHaveValue(lastName);
      this.ok(id);
    } catch (e) {
      this.fail(id, "lastName 입력 안됨");
    }
  }

  /**
   * lastName 도움말 확인
   * */
  async lastNameHelper() {
    const id = "TC4";
    this.testcase(id, "lastName 도움말 확인");
    try {
      const $title = await this.page.locator("h1", {
        hasText: "Sign Up",
      });
      const $lastName = await this.page.locator("#lastName");
      await $lastName.focus();
      await $title.click();
      const $lastNameHelper = await this.page.locator("#lastName-helper-text");
      expect($lastNameHelper).toBeVisible();
      this.ok(id);
    } catch (e) {
      this.fail(id, "lastName 도움말 없음");
    }
  }

  /**
   * username 입력 확인
   * */
  async usernameInput(username) {
    const id = "TC5";
    this.testcase(id, "username 입력 확인");
    try {
      const $username = await this.page.locator("#username");
      await $username.fill(username);
      await expect($username).toHaveValue(username);
      this.ok(id);
    } catch (e) {
      this.fail(id, "username 입력 안됨");
    }
  }

  /**
   * username 도움말 확인
   * */
  async usernameHelper() {
    const id = "TC6";
    this.testcase(id, "username 도움말 확인");
    try {
      const $title = await this.page.locator("h1", {
        hasText: "Sign Up",
      });
      const $username = await this.page.locator("#username");
      await $username.focus();
      await $title.click();
      const $usernameHelper = await this.page.locator("#username-helper-text");
      expect($usernameHelper).toBeVisible();
      this.ok(id);
    } catch (e) {
      this.fail(id, "username 도움말 없음");
    }
  }

  /**
   * password 입력 확인
   * */
  async passwordInput(password) {
    const id = "TC7";
    this.testcase(id, "password 입력 확인");
    try {
      const $password = await this.page.locator('[name="password"]');
      await $password.fill(password);
      await expect($password).toHaveValue(password);
      this.ok(id);
    } catch (e) {
      this.fail(id, "password 입력 안됨");
    }
  }

  /**
   * password 도움말 확인
   * */
  async passwordHelper() {
    const id = "TC8";
    this.testcase(id, "password 도움말 확인");
    try {
      const $title = await this.page.locator("h1", {
        hasText: "Sign Up",
      });
      const $password = await this.page.locator("#password");
      await $password.focus();
      await $title.click();
      const $passwordHelper = await this.page.locator("#password-helper-text");
      expect($passwordHelper).toBeVisible();
      this.ok(id);
    } catch (e) {
      this.fail(id, "password 도움말 없음");
    }
  }

  /**
   * ConfirmPassword 입력 확인
   * */
  async confirmPasswordInput(password) {
    const id = "TC8";
    this.testcase(id, "confirmPassword 입력 확인");
    try {
      const $confirmPassword = await this.page.locator('[name="confirmPassword"]');
      await $confirmPassword.fill(password);
      await expect($confirmPassword).toHaveValue(password);
      this.ok(id);
    } catch (e) {
      this.fail(id, "confirmPassword 입력 안됨");
    }
  }

  /**
   * confirmPassword 도움말 확인
   * */
  async confirmPasswordHelper() {
    const id = "TC9";
    this.testcase(id, "confirmPassword 도움말 확인");
    try {
      const $title = await this.page.locator("h1", {
        hasText: "Sign Up",
      });
      const $confirmPassword = await this.page.locator("#confirmPassword");
      await $confirmPassword.focus();
      await $title.click();
      const $confirmPasswordHelper = await this.page.locator(
        "#confirmPassword-helper-text"
      );
      expect($confirmPasswordHelper).toBeVisible();
      this.ok(id);
    } catch (e) {
      this.fail(id, "confirmPassword 도움말 없음");
    }
  }

  /**
   * 회원가입 버튼 동작 확인
   * */
  async signInButton() {
    const id = "TC10";
    this.testcase(id, "회원가입 버튼 동작 확인");
    try {
      const $signin = await this.page.locator("button", {
        hasText: "SIGN UP",
      });
      await $signin.click();
      this.ok(id);
    } catch (e) {
      this.fail(id, "회원가입 버튼 동작 안함");
    }
  }
}
