import { Playwright } from "../core/playwright.js";

export class RealWorldApp extends Playwright {
    baseURL() {
        return 'http://localhost:3000'
    }

    routePath(urlPath) {
        return this.baseURL() + urlPath
    }
}
