import React from 'react'
import withData from '../util/withData'
import Layout from '../components/Layout'
import Note2 from '../components/Note2'

function NotesPage({ notes }) {
  const noteNodes = notes.edges.map(edge => edge.node)
  return (
    <Layout activeItem='notes2'>
      {noteNodes.map(note => <Note2 note={note} />)}
    </Layout>
  )
}

export default withData(NotesPage, {
  query: graphql`
    query notes2Query {
      notes {
        edges {
          node {
            ...Note2_note
          }
        }
      }
    }
  `
})
