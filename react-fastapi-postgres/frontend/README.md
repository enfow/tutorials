# REACT

## Initialize React app

```bash
$ npx create-react-app frontend
```

## Function or Class

- 아래 두 구현은 동일하다.

```javascript
// function
export function TableBoard() {

  return (
    <div>
      <p> hello </p>
      <p> world </p>
    </div>
  )
}
```

```javascript
// class
import React, { Component } from 'react';

export class TableBoardClass extends Component {

  render() { return (
      <div>
        <p> hello </p>
        <p> world </p>
      </div>
    )
  }
}
```

## antd

- React UI Library
- [Ant Design](<https://ant.design/docs/react/introduce>)

### Usage

- 다음과 같이 필요한 Component를 Import 한다.

```javascript
import {Button, Table} from 'antd';
```

- 사용하기 위해서는 우선 `App.css`에 다음을 추가해 주어야 한다.

```javascript
@import '~antd/dist/antd.css';
```
