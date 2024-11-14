import logo from './logo.png';
import './styling/NavigationBar.css';
// import App from './pages/App.js';

// import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

function NavigationBar() {
    return (
        <div className="Nav">
            <div class="rectangle"></div>
            <header className="Nav-header">
                <img src={logo} className="Nav-logo" alt="logo" />
                <a
                    className="Home-link"
                    href="/"
                    rel="noopener noreferrer"
                >Home</a>
                <a
                    className="Browse-link"
                    href="/Browse"
                    rel="noopener noreferrer"
                >Browse</a>
                <a
                    className="My-courses-link"
                    href="/my-courses"
                    rel="noopener noreferrer"
                >My Courses</a>
                {/* <input type="text" className="Search-bar" placeholder="Search..."/> */}
            </header>
        </div>
    );
  }
  
  export default NavigationBar;