// dom elements from the index page;
var searchInput = document.querySelector('form').pokemon;
var searchResult = document.querySelector(".search-results");
var pokemonList = document.querySelector(".pokemon-unordered-list");
var pages = document.querySelectorAll(".pagination li");
var url = "https://pokeapi.co/api/v2/pokemon/?limit=30";
var pokemonLibrary = [];

// make an ajax call for a json list of pokemon names and put it into an array
fetch("https://pokeapi.co/api/v2/pokemon")
  .then(function(data){
    return data.json();
  })
  .then(function(json){
    json.results.map(function(item){
      pokemonLibrary.push(item.name);
    })
  })

// make an ajax call using fetch api to get 30 pokemons a time
// list each name along with a link to that pokemon's show page
function loadPokemonList(link){
  fetch(link)
    .then(function(data){
      return data.json();
    })
    .then(function(json){
      pokemonList.innerHTML = json.results.map(function(pokemon){
        return (
          "<li><a href='/pokemon?pokemon=" + pokemon.name + "'>" 
          + pokemon.name + "</a></li>"
        );
      }).join("");
    });
}

loadPokemonList(url);

// when query result appears on the page and the user clicks it, autocomplete the input field
searchResult.addEventListener("click", function(e){
  if(e.target.matches("li")){
    searchInput.value = e.target.textContent;
    // hide the list items
    searchResult.style.display = "none";
  }
})

// display an list of names from the pokemon library that matches user input query
searchInput.addEventListener("keyup", function(){
  var query = this.value;
  var regex = new RegExp(query, "gi");
  
  // look for the input query in the pokemon names array
  var match = pokemonLibrary.filter(function(item){
    return item.match(regex);
  })

  var resultString = match.map(function(item){
    return "<li>" + item + "</li>";
  }).join("")

  searchResult.innerHTML = resultString;
})

// grab each page list item and put a listener on each so when user clicks, it will run
// a new ajax call with an updated url that has the updated offset amount
pages.forEach(function(page){
  page.addEventListener("click", function(e){
    e.preventDefault();
    var selectedPage = e.target.textContent;
    // the url parameter "limit" decides how many pokemon will display each time 
    // while the url parameter "offset" represents the next group of results
    // each offset can be calculated by multiplying the current page times the limit
    selectedPage =  selectedPage * 30;
    loadPokemonList("https://pokeapi.co/api/v2/pokemon/?limit=30&offset=" + selectedPage);
  });
})
