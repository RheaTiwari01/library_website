function getCSRF() {
    return document.querySelector("meta[name='csrf-token']").content;
}
const authors = document.getElementById("author");      // <select id="author" multiple>
const publishers = document.getElementById("publisher");
const title = document.getElementById("title");
const date = document.getElementById("date");


window.onload = async () => {

    const res = await fetch("/api/book/search/");
    const data = await res.json();

    console.log("API DATA:", data);   // 🔍 debug

    // Load authors
    data.author.forEach(a => {

        const op = document.createElement("option");

        op.value = a.id;
        op.text = `${a.fname} ${a.lname}`;

        authors.appendChild(op);
    });


    // Load publishers
    data.publisher.forEach(p => {

        const op = document.createElement("option");

        op.value = p.id;
        op.text = p.name;

        publishers.appendChild(op);
    });

};

async function addBook(){
    const selected = [...authors.selectedOptions].map(o => o.value);

    const data = {
        title: title.value,
        publish_date: date.value,
        publisher: publishers.value,
        author: selected
    };

    try {
        const response = await fetch("/api/book/make/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRF()
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.success) {
            alert(result.message);
            // Clear form
            title.value = "";
            date.value = "";
            publishers.selectedIndex = -1;
            authors.selectedIndex = -1;
        } else {
            alert("Error: " + JSON.stringify(result.errors));
        }
    } catch (error) {
        alert("Error: " + error.message);
    }
}