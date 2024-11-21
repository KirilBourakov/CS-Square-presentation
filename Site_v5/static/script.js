// when the page is loaded
document.addEventListener("DOMContentLoaded", (event) => {
    // get the location of the form
    const form = document.getElementById('new_post')
    // listen for submit events, calling the handleForm function when they occur
    form.addEventListener('submit', handleForm)


    // define how we handle the form
    async function handleForm(event){
        // prevent the form from reloading the page
        event.preventDefault()

        // get the form data
        const title = form.elements['title'].value
        const content = form.elements['content'].value
            
        // send a POST request, and wait for the server to respond
        let response = await fetch('http://127.0.0.1:5000', {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify({
                'title': title,
                'content': content,
            }),
        })
        console.log(response)
    }
})


