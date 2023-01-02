let articles = [["The Portable Problem", "The Portable Problem 479274.html"], ["Use It or Lose It: Why You Should Vote", "Use It or Lose It Why You Should Vote 962632.html"], ["The Downfall of Shakespeare in the Modern Classroom", "The Downfall of Shakespeare in the ModernClassroom 430624.html"], ["CUPE STRIKE: Looking Back at the Chaos", "CUPE STRIKE Looking Back at the Chaos 886456.html"], ["Women in STEM at Riverdale", "Women in STEM at Riverdale 950665.html"], ["Halloween Book Recommendations: 2022 Edition", "Halloween Book Recommendations 2022 Edition 323397.html"], ["Kingdom of the Feared by Kerri Maniscalco Review", "Kingdom of the Feared Review 145037.html"], ["The Ballad of Never After by Stephanie Garber Review", "The Ballad of Never After by Stephanie Garber Review 030773.html"], ["Riverdale's Favourite Halloween Movies", "Riverdales Favourite Halloween Movies 685826.html"], ["December 2022 Horoscopes", "December 2022 Horoscopes 775327.html"], ["Autumn's Charm", "Autumns Charm 841307.html"], ["Satisfying Art Moments", "Satisfying Art Moments 833277.html"], ["Pop Culture Portraits", "Pop Culture Portraits 475088.html"], ["Happy Halloween", "Happy Halloween 276626.html"], ["Pink Day Cartoon", "Pink Day Cartoon 125872.html"], ["365 Days of Weird", "365 Days of Weird 320258.html"], ["WINTER IN CANADA", "WINTER IN CANADA 122644.html"], ["Social Distance Comic", "Social Distance Comic 066336.html"], ["March 2022 Horoscopes", "March 2022 Horoscopes 776305.html"], ["January 2022 Horoscopes ", "January 2022 Horoscopes  364587.html"], ["March 2022 Edition: Movies to Watch", "March 2022 Edition Movies to Watch 481390.html"], ["Thank You, Mr. Harvey", "Thank You, Mr. Harvey 267798.html"], ["More than a stack of paper", "More than a stack of paper 241943.html"], ["To mask or not to mask", "To mask or not to mask 216412.html"], ["Are the Classics Still Relevant?", "Are the Classics Still Relevant 165281.html"], ["Menstrual products should be free", "Menstrual products should be free 848885.html"], ["Students or Sardines?", "Students or Sardines 340006.html"], ["June 2022 Edition: Movies to Watch", "June 2022 Edition Movies to Watch 935210.html"], ["January 2022 Edition: Movies to Watch", "January 2022 Edition Movies to Watch 114567.html"], ["The Seven Deaths of Evelyn Hardcastle Review", "The Seven Deaths of Evelyn Hardcastle Review 554801.html"], ["Three bingeable beach reads", "Three bingeable beach reads 194961.html"], ["5/5 for The Invisible Life of Addie LaRue", "55 for The Invisible Life of Addie LaRue 507112.html"], ["Iron Widow: A must read", "Iron Widow A must read 345821.html"], ["1000 Cranes for Ukraine", "1000 Cranes for Ukraine 944459.html"], ["Kyi & Boshi", "Kyi  Boshi 701236.html"], ["Turning a Corner with Ms. Chorner", "Turning a Corner with Ms. Chorner 717737.html"], ["Pain", "Pain 350170.html"]];
let article_obj = []; 
var idx = 0; 
var placeholder;

//navigation search bar 
function reset_search(){
    for(let i = 0; i < article_obj.length; i++){
        article_obj[i].remove();
    }

    article_obj.length = 0; 
    idx = 0;
}

function searchbar() {
    reset_search();
    var matches = 0
    var input = document.getElementById("searchbar").value; 

    for(let i = articles.length-1; i > -1; i--){
        if(input == ""){
            break; 
        }
        if((articles[i][0].toUpperCase()).replaceAll(" ", "").includes((input.toUpperCase()).replaceAll(" ", ""))){
            var item = document.createElement("a");
            item.classList.add("search");
            item.classList.add("break-words");
            item.innerHTML = articles[i][0];
            item.href = articles[i][1];
            document.getElementById("searchlist").appendChild(item);

            article_obj[idx] = item; 
            idx++; 
            matches++;
        }

        if(matches == 10){
            break; 
        }
    }
}

//carousel 
let all_comics = []; 
let all_horoscopes = [];  

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

//view more arrays 
let SHOW_AT_TIME = 5; 
let INIT = 5; 
let all_news = [];
let all_op = [];
let all_movie = []; 
let all_book = []

function viewmore(arr){
    //get number of hidden items
    hidden = 0; 
    for(let i = 0; i < arr.length; i++){
        if(arr[i].classList.contains("hide")){
            hidden++; 
        }
    }

    if(hidden == arr.length){
        return
    }else if((arr.length - hidden) > SHOW_AT_TIME){//show next at a time
        for(let i = 0; i < SHOW_AT_TIME; i++){
            arr[hidden - 1 + i].classList.remove("hide");
        }
    }else{//show the rest 
        for(let i = hidden -1; i < arr.length; i++){
            arr[i].classList.remove("hide")
        }
    }
    
}

function init_show(arr){
    for(let i = INIT; i < arr.length; i++){
        arr[i].classList.add("hide"); 
    }
}

function init_carsouel(arr){
    for(let i = 1; i < arr.length; i++){
        arr[i].classList.add("hide"); 
    }
}

window.onload = function(){
    document.getElementById("instagram").href = "#";
    document.getElementById("email").href = "mailto:hamilton.spect@gmail.com";
    document.getElementById("github").href = "https://github.com/ck88889/riverdale-spectator-website";

    //initialize article drop down items 
    if(document.getElementById("news")){ //news page
        INIT = 7; //amount to show at first

        all_news = (document.getElementById("news")).querySelectorAll(".type_card");
        init_show(all_news);
    }else if(document.getElementById("opinion")){ //opinion page
        INIT = 7; //amount to show at first

        all_op = (document.getElementById("opinion")).querySelectorAll(".type_card");
        init_show(all_op);
    }else if(document.getElementById("movie")){//critic's corner
        INIT = 3; //amount to show at first

        all_movie = (document.getElementById("movie")).querySelectorAll(".type_card");
        init_show(all_movie); //amount to show at first
        
        INIT = 5;
        all_book = (document.getElementById("book")).querySelectorAll(".type_card");
        init_show(all_book);
    }else if(document.getElementById("stories")){//c&i page 
        INIT = 3; //amount to show at first

        all_stories = (document.getElementById("stories")).querySelectorAll(".type_card");
        init_show(all_stories);

        INIT = 4;
   
        all_enter = (document.getElementById("entertainment")).querySelectorAll(".type_card");
        init_show(all_enter);
    }

    //initialize carsouel items 
    if(document.getElementById("comic") &&  document.getElementById("horoscopes")){
        all_comics = (document.getElementById("comic")).querySelectorAll(".carousel_item");
        init_carsouel(all_comics);
        all_horoscopes = (document.getElementById("horoscopes")).querySelectorAll(".carousel_item");
        init_carsouel(all_horoscopes);
    }
}
