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
        // extract the json from the response
        response = await response.json()
        update(response)
    }

    function update(posts){
        // get the element that will hold all the posts
        const post_parent = document.getElementById("posts")

        // remove all childern
        post_parent.innerHTML = '';

        // for every post
        posts.forEach(post => {

            // create a post
            const root = document.createElement('div')
            root.classList.add('center', 'post')

            const title = document.createElement('h1')
            title.innerHTML = post['title']

            const content = document.createElement('p')
            content.innerHTML = post['content']

            root.appendChild(title)
            root.appendChild(content)

            // add it to the parent that holds all posts
            post_parent.appendChild(root)
        });
    }
})


