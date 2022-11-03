window.function = function(str) {

  async function fetch_data(data) {

    // API endpoint
    const url = 'https://rijstkoker.pythonanywhere.com/?'

    const response = await fetch(url + new URLSearchParams({input: data}))

    .then(response => response.json())

    return response['index']

    }
  
    return fetch_data(str.value);

  }
