import { Etablissement } from '../domain/types'
import axios, { AxiosResponse } from 'axios'
import { Result } from 'true-myth'

const makeHeaders = (token: string) => {
  const jsonContentType = 'application/json'
  return {
    accept: jsonContentType,
    'content-type': jsonContentType,
    authorization: `Bearer ${token}`
  }
}

export const requestSireneAPI = async (
  siret: string,
  token: string
): Promise<Result<Etablissement, unknown>> => {
  const api_sirene_url = `https://api.insee.fr/entreprises/sirene/V3/siret/${siret}`

  try {
    const response: AxiosResponse<Etablissement> = await axios.get(api_sirene_url, {
      headers: makeHeaders(token)
    })
    return Result.ok(response.data)
  } catch (error: unknown) {
    return Result.err(error)
  }
}
