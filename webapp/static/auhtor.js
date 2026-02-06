function getCSRF() {
    return document.querySelector("meta[name='csrf-token']").content;
}
async function addAuthor(){
    const data = {
        fname: fname.value,
        lname: lname.value,
        email: email.value
    };

    try {
        const response = await fetch("/api/author/make/", {
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
            fname.value = "";
            lname.value = "";
            email.value = "";
        } else {
            alert("Error: " + JSON.stringify(result.errors));
        }
    } catch (error) {
        alert("Error: " + error.message);
    }
}
const search = document.getElementById("search");
const result = document.getElementById("result");   // ✅ fixed name

search.addEventListener("keyup", async () => {

    if (search.value.length < 3) {
        result.innerHTML = "";
        return;
    }

    const res = await fetch(`/api/author/search/?q=${search.value}`);
    const data = await res.json();

    result.innerHTML = "";

    data.forEach(d => {   
        const li = document.createElement("li");
        li.innerText = `${d.fname} ${d.lname} (${d.email})`;
        result.appendChild(li);
    });

});
