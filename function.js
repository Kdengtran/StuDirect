let f = function(str, start, end) {

    str = str.value;
    start = start.value;
    end = end.value;
  
    async function fetch_data() {

      // API endpoint
      const url = 'https://rijstkoker.pythonanywhere.com/?'
  
      const response = await fetch(url + new URLSearchParams({input: str}))
  
      .then(response => response.json())
  
      console.log(url)
      console.log(response)
  
      output = JSON.parse(response)
      
      return output['index'];
  
    }
  
    output = fetch_data();

    return output
    // return str.substring(start, end);
  }

// create api request (asynchronous)