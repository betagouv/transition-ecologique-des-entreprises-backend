import express, { Express } from 'express'
import router from './controller/routes.js'

const app: Express = express()
const port: number = 3000

app.use(express.json())

app.use('/api', router)

app.listen(port)

export default app
