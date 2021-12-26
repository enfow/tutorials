import { useState } from 'react';
import { Table, Button } from 'antd';

export function TableBoard() { 
  const buyList = [
    {
      key: '1',
      name: 'Mike',
      age: 32,
      address: '10 Downing Street',
    },
  ];

  const boughtList = [
    {
      key: '1',
      name: 'Mike',
      age: 32,
      address: '10 Downing Street',
    },
  ];

  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Age',
      dataIndex: 'age',
      key: 'age',
    },
    {
      title: 'Address',
      dataIndex: 'address',
      key: 'address',
    }
  ];

  return (
    <div>
      <div>
        <p> Buy List </p>
        <Table dataSource={buyList} columns={columns} />;
      </div>
      <div>
        <p> Bought List </p>
        <Table dataSource={boughtList} columns={columns} />;
      </div>
    </div>
    )
};
