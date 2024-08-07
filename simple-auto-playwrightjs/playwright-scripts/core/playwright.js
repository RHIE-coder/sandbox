import logger from './logger.js'

export class Playwright {

    #results;

    constructor(page) {
        if(page === undefined) {
            throw new ReferenceError('initialize page variable');
        }
        this.page = page;
        this.inject();
        this.#results = {};
    }

    inject() {
        throw new SyntaxError('override inject() function');
    }

    testcase(id, spec){
        this.#results[id] = {
            spec,
            result: null,
            error: null,
        }
    }

    ok(id){
        this.#results[id].result = "PASS";
        logger.info({
            id,
            spec: this.#results[id].spec,
            result: this.#results[id].result,
            error: this.#results[id].error,
            timestamp: new Date().getTime(),
        })
    }

    fail(id, message) {
        this.#results[id].result = "FAIL";
        this.#results[id].error = message;
        logger.error({
            id,
            spec: this.#results[id].spec,
            result: this.#results[id].result,
            error: this.#results[id].error,
            timestamp: new Date().getTime(),
        })
    }
    
    print() {

    }
}