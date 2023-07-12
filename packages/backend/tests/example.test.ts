import axios from 'axios'

import golden_file_json from '../data/test_files/golden_file-siret-01.json'

describe('Test golden files', () => {
  test('Test golden files', async () => {
    console.log('golden_file_json : ', golden_file_json)

    // const api_host = 'https://tee-backend-test.osc-fr1.scalingo.io'
    const api_host = 'http://localhost:3000' // local API Express - should be started before testing
    const api_path = '/api/insee/get_by_siret'
    const api_url = `${api_host}${api_path}`
    console.log('api_url : ', api_url)

    const request_body = { siret: '83014132100034' }
    const postData = JSON.stringify(request_body)
    console.log('postData : ', postData)

    const headers = {
      accept: 'application/json',
      'Content-Type': 'application/json'
    }
    console.log('headers : ', headers)

    const response = await axios(api_url, {
      method: 'post',
      headers: headers,
      data: postData
    })
    const respData = response.data
    console.log('respData : ', respData)

    expect(respData).toEqual(golden_file_json)
  })
})
