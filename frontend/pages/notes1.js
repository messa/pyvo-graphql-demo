import React from 'react'
import withData from '../util/withData'
import Note1 from '../components/Note1'

function NotesPage({ notes }) {
  const noteNodes = notes.edges.map(edge => edge.node)
  return (
    <div>
      {noteNodes.map(note => <Note1 note={note} />)}
    </div>
  )
}

export default withData(NotesPage, {
  query: graphql`
    query notes1Query {
      notes {
        edges {
          node {
            id
            created
            text
            wordCount
          }
        }
      }
    }
  `
})