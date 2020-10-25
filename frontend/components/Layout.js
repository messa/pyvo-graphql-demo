import React from 'react'
import styles from './Layout.module.css'
import MainMenu from './MainMenu'

function Layout({ children, activeItem }) {
  return (
    <div className={styles.Layout}>
      <MainMenu activeItem={activeItem} />
      {children}
      <style global jsx>{`
        body {
          font-family: Arial, sans-serif;
        }
        a {
          color: #03c;
        }
      `}</style>
    </div>
  )
}

export default Layout
