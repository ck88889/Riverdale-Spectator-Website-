let articles = [["The Portable Problem", "The Portable Problem 479274.html"], ["Use It or Lose It: Why You Should Vote", "Use It or Lose It Why You Should Vote 962632.html"], ["The Downfall of Shakespeare in the Modern Classroom", "The Downfall of Shakespeare in the ModernClassroom 430624.html"], ["CUPE STRIKE: Looking Back at the Chaos", "CUPE STRIKE Looking Back at the Chaos 886456.html"], ["Women in STEM at Riverdale", "Women in STEM at Riverdale 950665.html"], ["Halloween Book Recommendations: 2022 Edition", "Halloween Book Recommendations 2022 Edition 323397.html"], ["Kingdom of the Feared by Kerri Maniscalco Review", "Kingdom of the Feared Review 145037.html"], ["The Ballad of Never After by Stephanie Garber Review", "The Ballad of Never After by Stephanie Garber Review 030773.html"], ["Riverdale's Favourite Halloween Movies", "Riverdales Favourite Halloween Movies 685826.html"], ["December 2022 Horoscopes", "December 2022 Horoscopes 775327.html"], ["Autumn's Charm", "Autumns Charm 841307.html"], ["Satisfying Art Moments", "Satisfying Art Moments 833277.html"], ["Pop Culture Portraits", "Pop Culture Portraits 475088.html"], ["Happy Halloween", "Happy Halloween 276626.html"], ["Pink Day Cartoon", "Pink Day Cartoon 125872.html"], ["365 Days of Weird", "365 Days of Weird 320258.html"]];
let article_obj = []; 
var idx = 0; 
var placeholder;

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

window.onload = function(){
    document.getElementById("instagram").href = "#";
    document.getElementById("email").href = "mailto:hamilton.spect@gmail.com";
    document.getElementById("github").href = "https://github.com/ck88889/riverdale-spectator-website";
}
