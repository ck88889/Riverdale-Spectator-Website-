let articles = [["The Portable Problem", "The Portable Problem 479274.html"], ["Use It or Lose It: Why You Should Vote", "Use It or Lose It Why You Should Vote 962632.html"]];
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
