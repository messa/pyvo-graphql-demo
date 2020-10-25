import React from 'react'
import Link from 'next/link'

const menuItems = [
  { name: 'index',  path: '/', title: 'Index page – Hello World with GraphQL' },
  { name: 'notes1', path: '/notes1', title: 'Notes 1 – GraphQL query demo' },
  { name: 'notes2', path: '/notes2', title: 'Notes 2 – GraphQL fragments demo' },
]

function MainMenu({ activeItem }) {
  return (
    <ul className='MainMenu'>
      {menuItems.map(item => (
        <li key={item.name}>
          {item.name === activeItem ? (
            <strong>{item.title}</strong>
          ) : (
            <Link href={item.path}><a>{item.title}</a></Link>
          )}
        </li>
      ))}
      <style jsx>{`
        ul.MainMenu {
          list-style: none;
          padding-left: 0;
          margin-bottom: 2rem;
        }
      `}</style>
    </ul>
  )
}

export default MainMenu
