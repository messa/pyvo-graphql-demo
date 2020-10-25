import React from 'react'
import { createFragmentContainer, graphql } from 'react-relay'

function Note2({ note }) {
  return (
    <div>
      <h2>Note <code>{note.created}</code> ({note.wordCount})</h2>
      {note.text}
    </div>
  )
}

export default createFragmentContainer(Note2, {
  note: graphql`
    fragment Note2_note on Note {
      id
      created
      text
      wordCount
    }
  `
})
