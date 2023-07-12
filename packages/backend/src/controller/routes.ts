import { Router, Request, Response } from 'express'
import axios from 'axios'

const router = Router()

router.get('/health', (_req: Request, res: Response): void => {
  res.status(200).send()
})

router.post('/insee/get_by_siret', async (req: Request, res: Response): Promise<void> => {
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

  const api_siren_url = `https://api.insee.fr/entreprises/sirene/V3/siret/${siret}`

  // api sirene call
  try {
    const response = await axios.get(api_siren_url, {
      headers: headers
    })
    // send response
    res.send(response.data)
  } catch (error: any) {
    console.log(error)
    res.status(401).send(error.message)
  }
})

export default router
