import https from 'https'

describe('Test the root path', () => {
  test('It should response the GET method', (done) => {
    // curl -X 'POST' \
    // 'https://tee-backend-test.osc-fr1.scalingo.io/api/insee/get_by_siret' \
    //   -H 'accept: application/json' \
    //   -H 'Content-Type: application/json' \
    //   -d '{
    //   "siret": "83014132100034"
    // }'
    const api_host = 'https://tee-backend-test.osc-fr1.scalingo.io'
    const api_path = '/api/insee/get_by_siret'

    const request_body = { siret: '83014132100034' }
    const postData = JSON.stringify(request_body)

    const options = {
      hostname: api_host,
      // port: 443,
      path: api_path,
      method: 'POST',
      headers: {
        accept: 'application/json',
        'Content-Type': 'application/json'
      }
    }

    const req = https.request(options, (res) => {
      console.log('statusCode:', res.statusCode)
      console.log('headers:', res.headers)

      res.on('data', (d) => {
        process.stdout.write(d)
      })
    })

    req.on('error', (e) => {
      console.error(e)
    })

    req.write(postData)
    req.end()

    expect(true)
    done()
  })
})
