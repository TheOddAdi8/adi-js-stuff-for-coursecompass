import React from 'react';
import ReactDOM from 'react-dom/client';

import './styling/index.css';

import NavigationBar from './NavigationBar';
import Home from './pages/Home';
import Browse from './pages/Browse';
import MyCourses from './pages/MyCourses';
import DataTest from './pages/DataTest';

import reportWebVitals from './reportWebVitals';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import CourseInformationPage from './pages/CourseInformationPage';
import Edit from './pages/Edit';

const router = createBrowserRouter([
  {
    path: "",
    element: <Home />,
  },
  {
    path: "/Browse",
    element: <Browse />,
  },
  {
    path: "/my-courses",
    element: <MyCourses />
  },
  {
    path: "/course-info",
    element: <CourseInformationPage />
  },
  {
    path: "/data-test",
    element: <DataTest />
  },
  {
    path: "/edit-course",
    element: <Edit />
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <NavigationBar />
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();