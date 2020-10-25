import React from 'react'
import styles from './Layout.module.css'

function Layout({ children }) {
  return (
    <div className={styles.Layout}>
      {children}
      <style global jsx>{`
        body {
          font-family: Arial, sans-serif;
        }
      `}</style>
    </div>
  )
}

export default Layout
