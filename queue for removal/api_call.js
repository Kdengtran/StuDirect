async function fetch_data(data) {

    // API endpoint
    const url = 'https://rijstkoker.pythonanywhere.com/?'

    const response = await fetch(url + new URLSearchParams({input: data}))

        .then(response => response.json())
    
    return console.log(response)

}

// run the following in the terminal: node api_call.js
fetch_data('Als deze hele zin bestaat uit hoofdletters, dan werkt de functie!')
