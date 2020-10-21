import React from 'react'
import withData from '../util/withData'

function IndexPage({ hello }) {
  return (
    <div>
      <h1>Hello, {hello}!</h1>
    </div>
  )
}

export default withData(IndexPage, {
  query: graphql`
    query pages_indexQuery {
      hello
    }
  `
})