window.function = function(str) {

    str = str.value;
  
    async function fetch_data() {

      // API endpoint
      const url = 'https://rijstkoker.pythonanywhere.com/?'
  
      const response = await fetch(url + new URLSearchParams({input: 'kaas'}))
  
      .then(response => response.json())
  
      console.log(url)
      console.log(response)
  
      output = JSON.parse(response)
      
      return output['index'];
  
    }
  
    output = fetch_data();

    console.log(output)

    return str
    // return str.substring(start, end);
  }

// create api request (asynchronous)