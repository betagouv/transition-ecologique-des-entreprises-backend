import express, { Express, Request, Response } from 'express'
import { helloWorldRoute } from './routes'

const environment = process.env

const app: Express = express()
const port: number = 3000

app.set('env', environment)

app.get('/', helloWorldRoute)

app.post('/api/insee/get_by_siret', (req: Request, res: Response): void => {
  // fetch request siret parameter
  const siret = req.body.siret
  console.log(siret)

  console.log(req.app.get('env'))

  // get token from environment
  // build header
  // api sirene call
  // send response
})

app.listen(port)

export default app
