let plus = document.querySelector(".plus")
let tweets = document.querySelector(".tweets")




function add()
{
  let id = makeid(15)
    let tweet = document.createElement("div");
    tweet.className = "entry"
    tweet.id = id
    tweet.innerHTML = `
     <span>L'Etiquette: </span>
    <input type="text"  name="categorie" class="fields tweet_fields" required>
    <button id="${id}"class="minus_btn add_remove" type="button" onclick="remove(this.id)">-</button>`
     tweets.appendChild(tweet)
}

function remove(id)
{
     let tweet_del = document.getElementById(id)
     tweets.removeChild(tweet_del)
}




function makeid(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return result;
}







