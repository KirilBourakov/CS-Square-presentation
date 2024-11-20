document.addEventListener("DOMContentLoaded", (event) => {
    const form = document.getElementById('new_post')
    form.addEventListener('submit', handleForm)


    async function handleForm(event){
        event.preventDefault()
        const title = form.elements['title'].value
        const content = form.elements['content'].value
            
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


