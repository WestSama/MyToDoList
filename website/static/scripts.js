// Dark/Light Theme change
const btnToggle = document.getElementById("toggleDark");
const body = document.querySelector("body");
const table = document.getElementById("table")
const navBar = document.getElementById("navBar")
const footer = document.getElementById("footer")
const table2 = document.getElementById("table2")

body.style.background = "rgb(29 29 30)"

btnToggle.addEventListener("click", function() {
    this.classList.toggle("bi-sun");
    if (this.classList.toggle("bi-moon-fill"))
    {
        btnToggle.style.background = "white"
        body.style.background = "rgb(29 29 30)"
        body.style.color = "white"
        body.style.transition = "2s"
        navBar.classList.remove("navbar-light", "bg-light")
        navBar.classList.add("navbar-dark", "bg-dark")
        footer.classList.remove("bg-light")
        footer.classList.add("bg-dark")
        navBar.style.transition = "2s"
        footer.style.transition = "2s"    
        if (table == null)
        {
            table2.classList.remove("table-primary")
            table2.classList.add("table-dark")
        }
        else
        {
            table.classList.remove("table-primary")
            table.classList.add("table-dark")   
        }  
    }
    else
    {
        btnToggle.style.background = "grey"
        body.style.background = "white"
        body.style.color = "black"
        body.style.transition = "2s"
        navBar.classList.remove("navbar-dark", "bg-dark")
        navBar.classList.add("navbar-light", "bg-light")
        footer.classList.remove("bg-dark")
        footer.classList.add("bg-light")
        navBar.style.transition = "2s"
        footer.style.transition = "2s"   
        if (table == null)
        {
            table2.classList.remove("table-dark")
            table2.classList.add("table-primary")
        }
        else
        {
            table.classList.remove("table-dark")
            table.classList.add("table-primary")  
        }
    }    
 });

// In progress (Button)
function myTest(element) 
{
    if(element.classList.contains("btn-warning"))
    { 
        element.innerText = "On Hold";
        element.classList.remove("btn-warning")
        element.classList.add("btn-secondary")
        window.localStorage.setItem("btn", "btn-secondary")            
    }
    else
    {
        element.innerText = "In Progress";
        element.classList.remove("btn-secondary")
        element.classList.add("btn-warning")
        window.localStorage.setItem("btn", "btn-warning")
    }  
};
localStorage.getItem("btn")

