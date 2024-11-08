import { Login } from './pages/login.page.js';
import { chromium } from 'playwright';

(async()=>{
    const browser = await chromium.launch({headless: false, slowMo: 1000});
    const page = await browser.newPage()

    const login = new Login(page);

    await login.goto();
    // await login.signInButtonStatus()
    await login.usernameInput("hello world");
    await login.passwordInput("1234");
    await login.rememberMeCheckbox();
    await login.signInButton();
    await login.signUpLink();
    
    await page.close();
    await browser.close();
})()