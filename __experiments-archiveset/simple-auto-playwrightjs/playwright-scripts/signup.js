import { SignUp } from './pages/signup.page.js';
import { chromium } from 'playwright';

(async()=>{
    const browser = await chromium.launch({headless: false, slowMo: 1000});
    const page = await browser.newPage()

    const signup = new SignUp(page);
    await signup.goto()
    await signup.firstNameHelper()
    await signup.lastNameHelper()
    await signup.usernameHelper()
    await signup.passwordHelper()
    await signup.confirmPasswordHelper()

    await page.close();
    await browser.close();
})()