console.log("script.js")

window.onload = init;

const domElements = {
    // Will be executed from init
    collectDOM: function(){
        this.clearFormButton = document.getElementById("refresh");
        this.formText = document.getElementById("article-create-form")
    }
};

// called when page is fully loaded
function init(){
    console.log("init function called")
    domElements.collectDOM();
    domElements.clearFormButton.addEventListener("click", clearForm);
}

// called by click event listener for 'clear' button
function clearForm(event){
    console.log("Form submission button clicked");
    console.log(event.currentTarget);
    domElements.formText.reset();
}