import React from 'react'

function Note2({ note }) {
  return (
    <div>
      <h2>Note <code>{note.created}</code></h2>
      {note.text}
    </div>
  )
}

export default Note2
