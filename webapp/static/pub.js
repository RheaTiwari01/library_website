function getCSRF() {
    return document.querySelector("meta[name='csrf-token']").content;
}
async function addPub(){
    const data = {
        name: Name.value,
        country: country.value,
        website: website.value
    };

    try {
        const response = await fetch("/api/publisher/make/", {
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
            name.value = "";
            country.value = "";
            website.value = "";
        } else {
            alert("Error: " + JSON.stringify(result.errors));
        }
    } catch (error) {
        alert("Error: " + error.message);
    }
}
search = document.getElementById("search")
res= document.getElementById("result")
search.addEventListener("keyup", async ()=>{

    if(search.value.length < 2){
        result.innerHTML="";
        return;
    }

    const res = await fetch(
        `/api/publisher/search/?q=${search.value}`
    );

    const data = await res.json();

    result.innerHTML="";

    data.forEach(a=>{

        const li = document.createElement("li");

        li.innerText = `${a.name} (${a.email})`;

        result.appendChild(li);

    });
});