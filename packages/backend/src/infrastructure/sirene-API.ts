import { Etablissement } from '../domain/types.js'
import axios, { AxiosResponse } from 'axios'
import { Result } from 'true-myth'

/**
 * Populate headers for a call to the "SIRENE" API
 *
 * @arg token - API access token
 */
const makeHeaders = (token: string) => {
  const jsonContentType = 'application/json'
  return {
    accept: jsonContentType,
    'content-type': jsonContentType,
    authorization: `Bearer ${token}`
  }
}

/**
 * Returns a value if it is an Error, or encapsulates it inside an Error otherwise
 *
 * Javascript `throw` keyword can throw anything, not only errors, most of the times we
 * however expect errors when we use `try/catch`.
 *
 * This function helps to ensure that the `catch`ed object is indeed an error.
 *
 * @arg value - expected to be an error, e.g. retrieved with the `catch` keyword.
 */
function ensureError(value: unknown): Error {
  if (value instanceof Error) return value

  let stringified = '[Unable to stringify the thrown value]'
  try {
    stringified = JSON.stringify(value)
  } catch {}

  const error = new Error(`This value was thrown as is, not through an Error: ${stringified}`)
  return error
}

/**
 * requestSireneAPI requests data about companies, given their "siret"
 *
 * @arg siret - siret number of the company to fetch
 * @arg token - API access token
 */
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
