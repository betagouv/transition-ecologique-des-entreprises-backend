import axios from 'axios'

describe('Test the root path', () => {
  test('It should response the GET method', async () => {
    const api_host = 'https://tee-backend-test.osc-fr1.scalingo.io'
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

    const response = axios(api_url, {
      method: 'post',
      headers: headers,
      data: postData
    })
    console.log('respJson : ', (await response).data)

    expect(true)
  })
})
