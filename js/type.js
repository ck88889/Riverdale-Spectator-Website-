let all_comics = []; 
let all_horoscopes = []; 

function viewmore(arr){
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

function init_show(arr){
    for(let i = 1; i < arr.length; i++){
        arr[i].classList.add("hide"); 
    }
}

window.onload = function(){
    all_comics = (document.getElementById("comics")).querySelectorAll(".carousel_item");
    init_show(all_comics);
    all_horoscopes = (document.getElementById("horoscopes")).querySelectorAll(".carousel_item");
}