import * as React from 'react'
import { Link } from 'gatsby'

import Layout from '../components/layout'

const AboutPage = () => {
  return (
    <Layout>
      <main>
        <title>About Me</title>
        <h1>About Me</h1>
        <p>Hi there! I'm the proud creator of this site, which I built with Gatsby.</p>
        <Link to="/"> Back to Home </Link>
     </main>
    </Layout>
  )
}

export default AboutPage
