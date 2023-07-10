import express, { Express } from 'express'
import { helloWorldRoute } from './routes'

const app: Express = express()
const port: number = 3000

app.get('/', helloWorldRoute)

app.listen(port)

export default app
