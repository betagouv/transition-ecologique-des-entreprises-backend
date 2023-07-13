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

function ensureError(value: unknown): Error {
  if (value instanceof Error) return value

  let stringified = '[Unable to stringify the thrown value]'
  try {
    stringified = JSON.stringify(value)
  } catch {}

  const error = new Error(`This value was thrown as is, not through an Error: ${stringified}`)
  return error
}

export const requestSireneAPI = async (
  siret: string,
  token: string
): Promise<Result<Etablissement, Error>> => {
  const api_sirene_url = `https://api.insee.fr/entreprises/sirene/V3/siret/${siret}`

  try {
    const response: AxiosResponse<Etablissement> = await axios.get(api_sirene_url, {
      headers: makeHeaders(token)
    })
    return Result.ok(response.data)
  } catch (err: unknown) {
    const error = ensureError(err)

    return Result.err(error)
  }
}
