import express, { Express, Request, Response } from 'express'
import { helloWorldRoute } from './routes'
import * as dotenv from 'dotenv'
import axios from 'axios'

dotenv.config()

const environment = process.env

const app: Express = express()
const port: number = 3000

app.use(express.json())

app.set('env', environment)

app.get('/', helloWorldRoute)

app.post('/api/insee/get_by_siret', async (req: Request, res: Response): Promise<void> => {
  // fetch request siret parameter
  const siret = req.body.siret
  console.log(siret)

  // get token from environment
  const token = req.app.get('env').SIRENE_API_TOKEN
  console.log(token)

  // build header
  const headers = {
    accept: 'application/json',
    'content-type': 'application/json',
    authorization: `Bearer ${token}`
  }

  const api_siren_url = `https://api.insee.fr/entreprises/sirene/V3/${siret}`

  // api sirene call
  const response = await axios(api_siren_url, {
    method: 'get',
    headers: headers
  })

  // send response
  res.send(response)
})

app.listen(port)

export default app
