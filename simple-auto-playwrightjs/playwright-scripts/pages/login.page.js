import { expect } from "@playwright/test"
import { RealWorldApp } from "./context.js";

export class Login extends RealWorldApp {

    inject(){}

    async goto() {
        await this.page.goto(this.routePath('/signin'));
    }

    /**
     * 로그인 버튼 활성 상태 확인
     * */
    async signInButtonStatus() {
        const id = "TC1"
        this.testcase(id, "로그인 버튼 활성 상태 확인")
        try {
            const $signin = await this.page.locator('button[type=submit]', {
                hasText: "SIGN IN"
            })
            // console.log(await $signin.getAttribute('disabled'))
            // const tagName = await $signin.evaluate(el => el.tagName);
            // console.log('Tag Name:', tagName);
            expect($signin).toBeEnabled()
            this.ok(id)
        } catch (e) {
            this.fail(id, "로그인 버튼이 비활성화 됨");
        }
    }

    /**
     * username 입력 확인
     * */
    async usernameInput(username) {
        const id = "TC2"
        this.testcase(id, "username 입력 확인")
        try {
            const $username = await this.page.locator('#username');
            await $username.fill(username);
            await expect($username).toHaveValue(username)
            this.ok(id)
        } catch (e) {
            this.fail(id, "username 입력 안됨");
        }
    }

    /**
     * password 입력 확인
     * */
    async passwordInput(password) {
        const id = "TC3"
        this.testcase(id, "password 입력 확인")
        try {
            const $password = await this.page.locator('[name="password"]');
            await $password.fill(password);
            await expect($password).toHaveValue(password);
            this.ok(id)
        } catch (e) {
            this.fail(id, "password 입력 안됨");
        }
    }

    /**
     * remember checkbox 입력 확인
     * */
    async rememberMeCheckbox() {
        const id = "TC4"
        this.testcase(id, "remeber checkbox 입력 확인")
        try {
            // const $remember = await this.page.getByRole('checkbox', { name: 'remember' });
            const $remember = await this.page.locator('input[type="checkbox"][name="remember"]')
            await $remember.setChecked(true)
            await expect($remember).toBeChecked(true)
            this.ok(id)
        } catch (e) {
            this.fail(id, "remember checkbox 비활성");
        }
    }

    /**
     * 로그인 버튼 동작 확인
     * */
    async signInButton() {
        const id = "TC5"
        this.testcase(id, "로그인 버튼 동작 확인")
        try {
            const $signin = await this.page.locator('button', {
                hasText: "SIGN IN"
            })
            await $signin.click()
            this.ok(id)
        } catch (e) {
            this.fail(id, "로그인 버튼 동작 안함");
        }
    }

    /**
     * 회원가입 링크 문구 동작 확인
     * */
    async signUpLink() {
        const id = "TC6"
        this.testcase(id, "회원가입 링크 문구 동작 확인")
        try {
            const $link = await this.page.locator('a[href="/signup"]', {
                hasText: `Don't have an account? Sign Up`
            });
            const info = await $link.evaluate(el => el.innerText);
            console.log(info);
            await $link.click(); 
            await $link.click(); 
            // console.log(await this.page.url())
            await expect(page).toHaveURL(this.routePath('/signup'))
            this.ok(id)
        } catch (e) {
            this.fail(id, "회원가입 링크 동작 안함");
        }
    }
}
