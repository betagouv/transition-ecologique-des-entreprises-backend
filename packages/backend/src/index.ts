import express, { Express } from 'express'
import * as dotenv from 'dotenv'
import router from './controller/routes'

dotenv.config()

const environment = process.env

const app: Express = express()
const port: number = 3000

app.use(express.json())

app.use('/api', router)

app.set('env', environment)

app.listen(port)

export default app
