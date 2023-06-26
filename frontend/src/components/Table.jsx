import { useState } from "react";

function Table(props) {
  
  return (
    <table className="table">
      <thead>
        <tr>
          <th>Результат</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>Ширина</td>
          <td>{props.width}</td>
        </tr>
        <tr>
          <td>Высота</td>
          <td>{props.height}</td>
        </tr>
        <tr>
          <td>Результат</td>
          <td>{props.res}</td>
        </tr>
      </tbody>
    </table>
  );
}

export default Table;
