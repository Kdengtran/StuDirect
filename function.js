window.function = function(str) {

    str = String(str.value);
  
    async function fetch_data(input) {

      // API endpoint
      const url = 'https://rijstkoker.pythonanywhere.com/?'
  
      const response = await fetch(url + new URLSearchParams({input: input}))
  
      .then(response => response.json());
  
      console.log(url);
      console.log(response);
  
      output = JSON.parse(response);
      
      return output['index'];
  
    }
  
    output = fetch_data(str);

    return String(output)
    // return str.substring(start, end);
  }

// create api request (asynchronous)