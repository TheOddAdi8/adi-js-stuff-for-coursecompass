import '../styling/Browse.css';
import React, { useState, useEffect } from 'react';

function Browse() {
  const [data, setdata] = useState({
    names: "",
    ids: ""
  });
  const [searchParameters, setSearchParameters] = useState({
    input: ""
  });
  const [dropdowns, setDropdowns] = useState({
    divisions: [],
    subjects: [],
    courses: [],
    teachers: []
  });

  var potato = "";

  useEffect(() => {
    fetch("/populate", {method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }}).then((res) =>
      res.json().then((data) => {
        setDropdowns({
          divisions: data.Divisions.split("'").join("").split(", "),
          subjects: data.Subjects.split("'").join("").split(", "),
          courses: data.Courses.split("'").join("").split(", "),
          teachers: data.Teachers.split("'").join("").split(", ")
        })
      })
    )
  }, [potato])

  // Set initial state for selected options in each dropdown
  const [selectedOption1, setSelectedOption1] = useState('');
  const [selectedOption2, setSelectedOption2] = useState('');
  const [selectedOption3, setSelectedOption3] = useState('');
  const [selectedOption4, setSelectedOption4] = useState('');

  // Sample options for each dropdown
  // const dropdownOptions1 = ['Elementary', 'Middle', 'Upper'];
  // const dropdownOptions2 = ['English', 'Math', 'History', 'More Subjects'];
  // const dropdownOptions3 = ['Course1', 'Course2', 'Course3'];
  // const dropdownOptions4 = ['Marcus Twyford', 'Teacher2', 'Teacher3'];

  const dropdownOptions1 = dropdowns.divisions;
  const dropdownOptions2 = dropdowns.subjects;
  const dropdownOptions3 = dropdowns.courses;
  const dropdownOptions4 = dropdowns.teachers;

  // var searchParameters = selectedOption1 + "," + selectedOption2 + "," + selectedOption3 + "," + selectedOption4;

  // useEffect(() => {
  //   fetch('/search', {
  //     method: 'POST',
  //     headers: {
  //       'Content-Type': 'application/x-www-form-urlencoded'
  //     },
  //     body: 'data=' + encodeURIComponent(JSON.stringify(searchParameters))
  //   })
  //   .then((res) => res.json())
  //   .then(data => {
  //     console.log(data);
  //     setdata({
  //       result: data.Result
  //     })
  //   })
  //   .catch((error) => {
  //     console.error('Error:', error);
  //   });
  // }, []);

  //Search functionality
  const Send = () => {
    if (!(selectedOption1 === '' && selectedOption2 === '' && selectedOption3 === '' && selectedOption4 === '')) {
      setSearchParameters({
        input: (selectedOption1 + "," + selectedOption2 + "," + selectedOption3 + "," + selectedOption4)
      });
    }
    else {
      setSearchParameters({
        input: ''
      });
    }
  };

  useEffect(() => {
    if (!searchParameters.input) {
      return;
    }  // Don't fetch if input is empty

    else if (!data.names) {
      setdata({
        names: 'No results.'
      })
      return;
    }

    fetch('/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: 'data=' + encodeURIComponent(JSON.stringify(searchParameters.input))
    })
    .then((res) => res.json())
    .then(data => {
      setdata({
        names: data.Names,
        ids: data.Ids
      })
    })
    .catch((error) => {
      console.error('Error:', error);
    });
    showResults();
  }, [searchParameters.input, data.names, data.ids, showResults]);

  let text = "<ul>";
  const nameList = (data.names || "").split(",");
  const idList = (data.ids || "").split(",");
  // if (data.ids.length !== 0) {
  //   console.log(data.ids);
  // }
  // text += "<li>sup</li>";
  nameList.forEach(myFunction);
  // text += "<li>{idList}</li>"
  text += "</ul>";

  function showResults() {
    document.getElementById("results").innerHTML = text;
  }

  function myFunction(value) {
    // text += "<li><form method='post' action='/course-info'><input type='hidden' name='extra_submit_param' value='value'><button type='submit' name='submit_param' value={value} class='link-button'>" + {value} + "</button></input></form></li>";
    var idValue = -1;
    for (var i = 0; i < nameList.length; i++) {
      if (nameList[i] === value) {
        idValue = idList[i];
      }
    }
    text += `
    <li>
      <form method="post" action="/course-info">
        <input type="hidden" name="extra_submit_param" value="${idValue}">
        <button type="submit" name="submit_param" value="${idValue}" class="link-button">
          ${value}
        </button>
      </form>
    </li>`;
    // text += <li>{value}</li>
  } 

  return (
    // <div style="height: 2000px">
    <div>
      <div className='Browse' style={{height: '2000 px', padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Please Select School/Department/Course/Teacher</h1>
        <div className='dd-content'>


          {/* Dropdown 1 */}
          <div className='dd1'>
              <select
                value={selectedOption1}
                onChange={(e) => setSelectedOption1(e.target.value)}
              >
                <option value="">Select School</option>
                {dropdownOptions1.map((option, index) => (
                  <option key={index} value={option}>
                    {option}
                  </option>
                ))}
              </select>
          </div>

          {/* Dropdown 2 */}
          <div>
              <select
                value={selectedOption2}
                onChange={(e) => setSelectedOption2(e.target.value)}
              >
                <option value="">Select Department/Grade</option>
                {dropdownOptions2.map((choice, index) => (
                  <option key={index} value={choice}>
                    {choice}
                  </option>
                ))}
              </select>
          </div>

          {/* Dropdown 3 */}
          <div>
              <select
                value={selectedOption3}
                onChange={(e) => setSelectedOption3(e.target.value)}
              >
                <option value="">Select Course</option>
                {dropdownOptions3.map((item, index) => (
                  <option key={index} value={item}>
                    {item}
                  </option>
                ))}
              </select>
          </div>

          {/* Dropdown 4 */}
          <div>
              <select
                value={selectedOption4}
                onChange={(e) => setSelectedOption4(e.target.value)}
              >
                <option value="">Select Teacher</option>
                {dropdownOptions4.map((option, index) => (
                  <option key={index} value={option}>
                    {option}
                  </option>
                ))}
              </select>
          </div>
        </div>
        {/* Display selected options */}
        <div style={{ marginTop: '20px' }}>
          <h2>Selected Options:</h2>
          <p>Dropdown 1: {selectedOption1 || 'None'}</p>
          <p>Dropdown 2: {selectedOption2 || 'None'}</p>
          <p>Dropdown 3: {selectedOption3 || 'None'}</p>
          <p>Dropdown 4: {selectedOption4 || 'None'}</p>
        </div>
        <button id="btn" className="sendBtn" onClick={Send}>Search</button>
        <div className="thing">
          <p id="results"></p>
        </div>
      </div>
    </div>
  );
}

export default Browse;