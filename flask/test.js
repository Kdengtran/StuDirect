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

fetch_data()
