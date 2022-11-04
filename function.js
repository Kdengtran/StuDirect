import fetch_data from '/flask/api_call.js';

window.function = function(str) {

    str = str.value;

    return fetch_data(str);

  }
