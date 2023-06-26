import React, { useState } from "react";
import Table from "./Table";

function FileUpload(props) {
  const [file, setFile] = useState(null);
  const [res, setRes] = useState("");
  const [width, setWidth] = useState("");
  const [height, setHeight] = useState("");

  const saveFile = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (event) => {
    let res = [];
    event.preventDefault();
    const formData = new FormData();
    formData.append("file", file);
    const endpoint = "http://127.0.0.1:8000/files/";
    fetch(endpoint, {
      method: "POST",
      body: formData,
      formData,
    }).then((response) => response.json())
      .then((data) => {
        setRes(data.res);
        setHeight(data.height);
        setWidth(data.width);
      });
    console.log(res);
  };

  return (
    <div className="App">
      <form encType="multipart/form-data" onSubmit={handleSubmit}>
        <label className="input-file">
          <input type="file" name="file" onChange={saveFile} />
          <span className="input-file-btn">Выберите файл</span>
        </label>
        <button type="submit" className="waves-effect waves-light btn">
          Сканировать
        </button>
      </form>
      <Table width={width} height={height} res={res} />
    </div>
  );
}

export default FileUpload;
