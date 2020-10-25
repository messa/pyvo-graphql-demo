import { createProxyMiddleware } from 'http-proxy-middleware'

export default createProxyMiddleware({
  target: 'http://127.0.0.1:5000'
})

export const config = {
  api: {
    bodyParser: false,
    externalResolver: true,
  },
}
