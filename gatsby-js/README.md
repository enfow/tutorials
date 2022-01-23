# Gatsby

## Installation

- NodeJS

```
# with mac
$ brew install node
```

- Gatsby cli

```
$ npm init
$ npm instal -g gatsby-cli

$ gatsby --version
# Gatsby CLI version: 4.5.2
```

## Make new gatsby site

```
$ gatsby new
```

- interactive prompt가 뜨는데, 적절히 답하면 gatsby app directory가 생성된다.

```
$ cd [GATSBY DIR]
$ npm start develop
```

- localhost 8000으로 접속하면 확인할 수 있다.

```
[localhost 8000](<http://127.0.0.1:8000>)
```

## Add new page

- `src/pages/` directory에 js file을 추가해주기만 하면 된다.

```
# src/pages/about.js

// Step 1: Import React
import * as React from 'react'

// Step 2: Define your component
const AboutPage = () => {
  return (
    <main>
      <title>About Me</title>
      <h1>About Me</h1>
      <p>Hi there! I'm the proud creator of this site, which I built with Gatsby.</p>
    </main>
  )
}

// Step 3: Export your component
export default AboutPage
```

- `localhost:8000/about`으로 접속하면 about page를 확인할 수 있다.

## Create Layout

```
# src/components/layout.js

import * as React from 'react'
import { Link } from 'gatsby'

const Layout = ({ pageTitle, children }) => {
  return (
    <div>
      <title>{pageTitle}</title>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
        </ul>
      </nav>
      <main>
        <h1>{pageTitle}</h1>
        {children}
      </main>
    </div>
  )
}

export default Layout
```

- `iindex.js`에 layout을 추가해준다.

```
# src/pages/index.js

import * as React from 'react'

import Layout from '../components/layout'

const IndexPage = () => {
  return (
    <Layout pageTitle="Home Page">
      ...
    </Layout>
  )
}
export default IndexPage
```

`<Layout>` 의 하위 요소들은 `{children}` 에서 rendering 된다.

## Gatsby Components

### Link

- HyperLink를 생성해주는 컴포넌트

```
import { Link } from 'gatsby'

<Link to="/"> Back to Home </Link>
```

## References

- [GatsbyJS Tutorial](<https://www.gatsbyjs.com/docs/tutorial/part-0/>)
