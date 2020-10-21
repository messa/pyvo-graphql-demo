import React from 'react'
import withData from '../util/withData'
import Note2 from '../components/Note2'

function NotesPage({ notes }) {
  const noteNodes = notes.edges.map(edge => edge.node)
  return (
    <div>
      {noteNodes.map(note => <Note2 note={note} />)}
    </div>
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
