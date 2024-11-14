// import logo from '../logo.png';
// import '../styling/App.css';

// function Browse() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           A;OSDFHA;LDKFH;ASLDFKH;ASLDFKH;ASLDFKHLAKSJIHAISGH
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default Browse;

import React, { useState } from 'react';

function Browse() {
  // Set initial state for selected options in each dropdown
  const [selectedOption1, setSelectedOption1] = useState('');
  const [selectedOption2, setSelectedOption2] = useState('');
  const [selectedOption3, setSelectedOption3] = useState('');
  const [selectedOption4, setSelectedOption4] = useState('');

  // Sample options for each dropdown
  const dropdownOptions1 = ['Elementary', 'Middle', 'Upper'];
  const dropdownOptions2 = ['English', 'Math', 'History', 'More Subjects'];
  const dropdownOptions3 = ['Course1', 'Coure2', 'Course3'];
  const dropdownOptions4 = ['Teacher1', 'Teacher2', 'Teacher3'];

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
     <h1>Please Select School/Department/Course/Unit</h1>

      {/* Dropdown 1 */}
      <div>
        <label>
          Select School:
          <select
            value={selectedOption1}
            onChange={(e) => setSelectedOption1(e.target.value)}
          >
            <option value="">Select an option</option>
            {dropdownOptions1.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>
      </div>

      {/* Dropdown 2 */}
      <div>
        <label>
          Select Department/Grade:
          <select
            value={selectedOption2}
            onChange={(e) => setSelectedOption2(e.target.value)}
          >
            <option value="">Select a choice</option>
            {dropdownOptions2.map((choice, index) => (
              <option key={index} value={choice}>
                {choice}
              </option>
            ))}
          </select>
        </label>
      </div>

      {/* Dropdown 3 */}
      <div>
        <label>
          Select Course:
          <select
            value={selectedOption3}
            onChange={(e) => setSelectedOption3(e.target.value)}
          >
            <option value="">Select an item</option>
            {dropdownOptions3.map((item, index) => (
              <option key={index} value={item}>
                {item}
              </option>
            ))}
          </select>
        </label>
      </div>

      {/* Dropdown 4 */}
      <div>
        <label>
          Select Teacher:
          <select
            value={selectedOption4}
            onChange={(e) => setSelectedOption4(e.target.value)}
          >
            <option value="">Select an option</option>
            {dropdownOptions4.map((option, index) => (
              <option key={index} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>
      </div>

      {/* Display selected options */}
      <div style={{ marginTop: '20px' }}>
        <h2>Selected Options:</h2>
        <p>Dropdown 1: {selectedOption1 || 'None'}</p>
        <p>Dropdown 2: {selectedOption2 || 'None'}</p>
        <p>Dropdown 3: {selectedOption3 || 'None'}</p>
        <p>Dropdown 4: {selectedOption4 || 'None'}</p>
      </div>
    </div>
  );
}

export default Browse;