let all_items = []; 

function viewmore(){
    alert("I WAS CLICKED"); 
}

function get_current(arr){
    current_idx = 0; 
    //get index of current item that being shown to user 
    for(let i = 0; i < arr.length; i++){
        if(!arr[i].classList.contains("hide")){
            current_idx = i; 
        }
    }
    return current_idx; 
}

function criticmore(type){
    alert("I WAS CLICKED"); 
}

function carouselnext(arr){
    current_idx = get_current(arr); 
    //if you're @ the end of the carousel -> go back to the front
    if(current_idx == arr.length -1){
        arr[current_idx].classList.add("hide"); 
        arr[0].classList.remove("hide"); 
    }else{
        arr[current_idx].classList.add("hide"); 
        arr[current_idx + 1].classList.remove("hide"); 
    }
}

function carouselback(arr){
    current_idx = get_current(arr); 
    //if you're @ the start of the carousel -> go to the back 
    if(current_idx == 0){
        arr[current_idx].classList.add("hide"); 
        arr[arr.length -1].classList.remove("hide"); 
    }else{
        arr[current_idx].classList.add("hide"); 
        arr[current_idx - 1].classList.remove("hide"); 
    }
}

window.onload = function(){
    all_comics = (document.getElementById("comics")).querySelectorAll(".carousel_item");
}