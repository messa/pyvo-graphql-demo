import { createProxyMiddleware } from 'http-proxy-middleware'

export default createProxyMiddleware({
  target: 'http://127.0.0.1:5000'
})

export const config = {
  api: {
    bodyParser: false,
    // the http-proxy-middleware doesn't expect the body-parser middleware to be used

    externalResolver: true,
    // to get rid of warnings about "API resolved without sending a response for ..., this may result in stalled requests"
  },
}
