// main.js
var React = require('react');
var ReactDOM = require('react-dom');

var sales = require('./sales_tic.js');

if (document.getElementById('example')) {
  ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('example')
  );
}
