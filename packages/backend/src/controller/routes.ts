import { Router, Request, Response } from 'express'
import { requestSireneAPI } from '../infrastructure/sirene_API'

const router = Router()

router.get('/health', (_req: Request, res: Response): void => {
  res.status(200).send()
})

router.post('/insee/get_by_siret', async (req: Request, res: Response): Promise<void> => {
  const requestedSiret = req.body.siret

  const apiToken = req.app.get('env').SIRENE_API_TOKEN

  const etablissementResult = await requestSireneAPI(requestedSiret, apiToken)

  if (etablissementResult.isErr) {
    const error = etablissementResult.error
    res.send(401).send(error)
  }

  if (etablissementResult.isOk) {
    const etablissement = etablissementResult.value
    res.send(etablissement)
  }
})

export default router