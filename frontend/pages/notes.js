import React from 'react'
import withData from '../util/withData'

function NotesPage({ notes }) {
  const noteNodes = notes.edges.map(edge => edge.node)
  return (
    <div>
      {noteNodes.map(note => <Note note={note} />)}
    </div>
  )
}

function Note({ note }) {
  return (
    <div>
      <h2>Note <code>{note.id}</code></h2>
      {note.text}
    </div>
  )
}

export default withData(NotesPage, {
  query: graphql`
    query notesQuery {
      notes {
        edges {
          node {
            id
            text
          }
        }
      }
    }
  `
})