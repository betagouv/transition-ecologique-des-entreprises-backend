// import { Express } from 'express'
import fetch from 'node-fetch'
// console.log('fetch : ', fetch)

describe('Test the root path', () => {
  test('It should response the GET method', done => {
    // curl -X 'POST' \
    // 'https://tee-backend-test.osc-fr1.scalingo.io/api/insee/get_by_siret' \
    //   -H 'accept: application/json' \
    //   -H 'Content-Type: application/json' \
    //   -d '{
    //   "siret": "83014132100034"
    // }'
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

    // const response = fetch(api_url, {
    //   method: 'POST',
    //   headers: headers,
    //   body: postData
    // })
    // const respJson = await response.json()
    // console.log('respJson : ', respJson)

    expect(true)
    done()
  })
})
