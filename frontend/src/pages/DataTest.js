import React, { useState, useEffect } from "react";
import '../styling/DataTest.css';

function DataTest() {
  const [data, setdata] = useState({
    name: "",
    phrase: ""
  });
  useEffect(() => {
    // Using fetch to fetch the api from
    // flask server it will be redirected to proxy
    fetch("/data").then((res) =>
        res.json().then((data) => {
            // Setting a data from api
            setdata({
                name: data.Name,
                phrase: data.Phrase
            });
        })
    );
  }, []);
  return (
    <div className="Data">
      <header className="Data-test-header">
      <h1>React and flask</h1>
                {/* Calling a data from setdata for showing */}
                <br />
                <p>{data.name}</p>
                <p>{data.phrase}</p>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
      </header>
    </div>
  );
}

export default DataTest;