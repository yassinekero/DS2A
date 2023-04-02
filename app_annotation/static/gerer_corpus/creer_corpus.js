let plus = document.querySelector(".plus")
let tweets = document.querySelector(".tweets")

let id = 0

function add()
{
  
    let tweet = document.createElement("div");
    tweet.className = "entry"
    tweet.id = id
    tweet.innerHTML = `
     <span>Tweet: </span>
    <input type="text" name="tweet" class="fields tweet_fields" required>
    <button id="${id}"class="minus_btn add_remove" type="button" onclick="remove(this.id)">-</button>`
     tweets.appendChild(tweet)
     id ++;
}

function remove(id)
{
     let tweet_del = document.getElementById(id)
     tweets.removeChild(tweet_del)
}



