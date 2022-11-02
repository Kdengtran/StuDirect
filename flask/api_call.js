async function fetch_data () {

// hier komt de endpoint API 
const url = 'https://rijstkoker.pythonanywhere.com';

    const response = await fetch(url, {

        method: "Post",
        headers: {

            "Content-Type": "application/json",
            Accept : "application/json"

        },
        body: JSON.stringify({

            input : kaas
            // foo : 0

         })

    })

    return response.json();

};

async function func_caller() {

    const data = await fetch_data();
    return data

}

func_caller()