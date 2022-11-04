async function fetch_data(data) {

    // API endpoint
    const url = 'https://rijstkoker.pythonanywhere.com/?'

    const response = await fetch(url + new URLSearchParams({input: data}))

        .then(response => response.json())
    
    return console.log(typeof response)

}

fetch_data('ppp')