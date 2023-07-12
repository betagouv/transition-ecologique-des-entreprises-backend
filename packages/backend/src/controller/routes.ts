import { Router, Request, Response } from 'express'
import axios from 'axios'

const router = Router()

router.get('/health', (_req: Request, res: Response): void => {
  res.status(200).send()
})

router.post('/insee/get_by_siret', async (req: Request, res: Response): Promise<void> => {
  const requested_siret = req.body.siret

  const api_token = req.app.get('env').SIRENE_API_TOKEN

  const jsonContentType = 'application/json'
  const headers = {
    accept: jsonContentType,
    'content-type': jsonContentType,
    authorization: `Bearer ${api_token}`
  }

  const api_siren_url = `https://api.insee.fr/entreprises/sirene/V3/siret/${requested_siret}`

  try {
    const response = await axios.get(api_siren_url, {
      headers: headers
    })
    res.send(response.data)
  } catch (error: any) {
    res.status(401).send(error.message)
  }
})

export default router
