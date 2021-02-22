import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Ninja from './Ninja';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
    <Ninja/>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
