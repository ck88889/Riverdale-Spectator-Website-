let articles = [["No result", "#"], ["The Portable Problem", "The Portable Problem 479274.html"], ["Use It or Lose It: Why You Should Vote", "Use It or Lose It Why You Should Vote 962632.html"]];
let article_obj = []; 
var idx = 0; 
var placeholder;

function show(){
    document.getElementById("searchlist").classList.remove("hidden");
}

function hide(){
    document.getElementById("searchlist").classList.add("hidden");
}

function init_drop(){
    for(let i = articles.length-1; i > -1; i--){
        var item = document.createElement("a");
        item.classList.add("search");
        item.classList.add("break-words");
        item.innerHTML = articles[i][0];
        item.href = articles[i][1];
        document.getElementById("searchlist").appendChild(item);

        article_obj[idx] = item; 
        idx++;
    }
}

function searchbar() {
    var input = document.getElementById("searchbar").value;
    num_matches = 0; 

    for(let i = 0; i < articles.length-1; i++){
        if(article_obj[i].textContent.includes(input)){
            article_obj[i].classList.remove("hide");
            article_obj[articles.length - 1].classList.add("hide"); 
            num_matches++; 
        }else{
            article_obj[i].classList.add("hide");
            article_obj[articles.length - 1].classList.remove("hide"); 
        }
    }

    show();
}

window.onload = function(){
    idx = 0;
    document.getElementById("instagram").href = "#";
    document.getElementById("email").href = "mailto:hamilton.spect@gmail.com";
    document.getElementById("github").href = "https://github.com/ck88889/riverdale-spectator-website";
    init_drop(); 
}
