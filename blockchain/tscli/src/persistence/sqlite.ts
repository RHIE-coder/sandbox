import sqlite3 from 'sqlite3'
import { open, Database } from 'sqlite'

class Sqlite3 {
    private _filepath:string
    private _conn:Database

    private constructor(filepath:string) {
        this._filepath = filepath
    }

    async open() {
        const conn = await open({
            filename: this._filepath,
            driver: sqlite3.Database
        })

        this._conn = conn
    }
    
    static async newConnection(filepath:string) {
        const lite = new Sqlite3(filepath)
        await lite.open()
    }

}