import React from 'react'
import withData from '../util/withData'
import Layout from '../components/Layout'

function IndexPage({ hello }) {
  return (
    <Layout>
      <h1>Hello, {hello}!</h1>
    </Layout>
  )
}

export default withData(IndexPage, {
  query: graphql`
    query pages_indexQuery {
      hello
    }
  `
})
