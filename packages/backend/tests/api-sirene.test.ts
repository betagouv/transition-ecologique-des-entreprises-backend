import axios from 'axios'

import golden_file_json from '../data/test_files/golden_file-siret-01.json'

describe('Test that API response format is unchanged', () => {
  test('Compare response data with golden file for siret 83014132100034', async () => {
    // const api_host = 'https://tee-backend-test.osc-fr1.scalingo.io'
    const api_host = 'http://localhost:3000' // local API Express - should be started before testing
    const api_path = '/api/insee/get_by_siret'
    const api_url = `${api_host}${api_path}`

    const request_body = { siret: '83014132100034' }
    const postData = JSON.stringify(request_body)

    const headers = {
      accept: 'application/json',
      'Content-Type': 'application/json'
    }

    const response = await axios(api_url, {
      method: 'post',
      headers: headers,
      data: postData
    })
    const respData = response.data

    expect(respData).toEqual(golden_file_json)
  })
})
