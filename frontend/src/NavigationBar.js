import logo from './logo.png';
import './styling/NavigationBar.css';
// import App from './pages/App.js';

// import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

function NavigationBar() {
    return (
        <div className="Nav">
            <div className="rectangle"></div>
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
                <a
                    className="Data-test-link"
                    href="/data-test"
                    rel="noopener noreferrer"
                >Data Testing</a>
                <a
                    className="Course-info-link"
                    href="/course-info"
                    rel="noopener noreferrer"
                >Course Info</a>
                <a
                    className="Edit-course-link"
                    href="/edit-course"
                    rel="noopener noreferrer"
                >Edit Course</a>
                <button id="btn" className="Log-out" onClick={confirmation}>Log out</button>
                {/* <input type="text" className="Search-bar" placeholder="Search..."/> */}
            </header>
        </div>
    );
}

function confirmation() {
    if (window.confirm("Are you sure you want to log out?")) {
        window.open("/", "_self");
    }
    else {

    }
    return 0;
}

export default NavigationBar;