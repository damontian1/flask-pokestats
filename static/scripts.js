// implement type as u search
var pokemonUnorderedList = document.querySelector(".search-bar");
var pokemonList = [];
fetch("https://pokeapi.co/api/v2/pokemon")
  .then(function(data){
    return data.json();
  })
  .then(function(json){
    pokemonList = pokemonList.concat(json.results);
    console.log(pokemonList);
  });