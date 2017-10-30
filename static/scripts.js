// implement type as u search
var pokemonName = document.querySelector(".pokemon-name")
var pokemonDescription = document.querySelector(".pokemon-description")
var pokemonImage = document.querySelector(".pokemon-image")
var pokemonSkills = document.querySelector(".pokemon-skills")
var pokemonList = document.querySelector(".pokemon-unordered-list")
// fetch("https://pokeapi.co/api/v2/pokemon")
// 25 per page
fetch("https://pokeapi.co/api/v2/pokemon/")
  .then(function(data){
    return data.json();
  })
  .then(function(json){
    pokemonList.innerHTML = json.results.map(function(pokemon){
      // console.log(pokemon.name)
      //http://127.0.0.1:5000/pokemon?pokemon=pika
      return "<li><a href='" + pokemon.url + "'>" + pokemon.name + "</a></li>"
    }).join("")
    // pokemonList = pokemonList.concat(json.results);
    // pokemon image
    // pokemonImage.src = json.sprites.front_default;
    // console.log(json.sprites.front_default)
    // console.log(json)
    // console.log(json)
    // json.stats.map(function(item){
      // skill point
      // console.log(item.base_stat)
      // skill name
      // console.log(item.stat.name)
    // });
    // pokemonName.textContent = json.name;
    // pokemonSkills.textContent = json.name + "'s" + " Skills:";
  });

  // gets pokemon description
  // fetch("https://cors-anywhere.herokuapp.com/https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=pikachu&indexpageids")
  //   .then(res => res.json())
  //   .then(data => {
  //     var pageid = data.query.pageids[0]
  //     pokemonDescription.textContent = data.query.pages[pageid].extract;
  //   })