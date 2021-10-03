// Initialize button with user's preferred color
let changeColor = document.getElementById("changeColor");

chrome.storage.sync.get("color", ({ color }) => {
  changeColor.style.backgroundColor = color;
});


// When the button is clicked, inject setPageBackgroundColor into current page
changeColor.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: setPageBackgroundColor,
  });
});

// The body of this function will be executed as a content script inside the
// current page
function setPageBackgroundColor() {
  chrome.storage.sync.get("color", ({ color }) => {
    document.body.style.backgroundColor = color;
  });
}


// Lettcode
// let signIn = document.getElementById("signin");

// signIn.addEventListener("click", async () => {
//   let leetCodeId = document.getElementById("leetcodeId").value;
//   document.getElementById("leetCodeStats").innerHTML= `Hey, welcome ${leetCodeId}`; 
//   const url = 'https://salty-waters-49462.herokuapp.com/leetcode.com/graphql';
//   // const url = 'https://swapi-graphql.netlify.app/.netlify/functions/index';
//   console.log('I was here: ' + url);
//   fetch(url, {
//     method: 'POST',
//     headers: { 
//       'Access-Control-Allow-Origin': '*',
//       'Content-Type': 'application/json'
//       // 'Access-Control-Allow-Credentials': 'true',
//       // 'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS'
//     },
//     body: JSON.stringify({
//       query: `
//         matchedUser($username: YOUR_USERNAME!) {
//           username
//           submitStats: submitStatsGlobal {
//             acSubmissionNum {
//             difficulty
//             count
//             submissions
//             }
//           }
//         }
//       `,
//       variables: {
//         username: 'akumar5'
//       }
//     })
//   })
//   .then((res) => res.json())
//   .then((result) => {
//     console.log(result);
//     document.getElementById("test").innerHTML='chuchu is here'; 
//   }).catch((err) => {
//     document.getElementById("test").innerHTML='error chuchu is here, '+ err;
//     console.log('error: ', err);
//   });
// });


// Leetcode stats global
// signIn.addEventListener("click", async () => {
//   let leetCodeId = document.getElementById("leetcodeId").value;
//   console.log('username: ' + leetCodeId);
//   fetch(`https://salty-waters-49462.herokuapp.com/leetcode-stats-six.vercel.app/api?username=${leetCodeId}&theme=dark`, {'Access-Control-Allow-Origin': '*'})
//       .then(response => response.text())
//       .then(data => {
//         console.log(data);
//         document.getElementById("stats").innerHTML=data; 
//       }).catch((err) => {
//         document.getElementById("stats").innerHTML=err; 
//         console.log('error: ', err);
//       });
// });

//generate random question
let getQuestion = document.getElementById("getQuestion");
getQuestion.addEventListener("click", async () => {
  var e = document.getElementById("topic");
  var topic = e.value;

  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  var graphql = JSON.stringify({
    query: `query getTopicTag($slug: String!) {topicTag(slug: $slug){name translatedName questions{status title difficulty titleSlug }} }`,
    variables: {"slug":`${topic}`}
  })
  var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: graphql
  };

  fetch("https://salty-waters-49462.herokuapp.com/leetcode.com/graphql", requestOptions)
    .then(response => response.json())
    .then(result => {
      var array = ["Easy", "Medium", "Hard"]
      let difficulty = document.querySelector('input[name="difficulty"]:checked').value;
      if(difficulty === "Random"){
        difficulty = array[Math.floor(Math.random() * array.length)];
      }
      
      let questionsArray = result.data.topicTag.questions || [];
      let filteredquestions = questionsArray.filter(item => item.difficulty===difficulty);
      let size = filteredquestions.length;
      let randomQuestion = Math.floor(Math.random() * size);
      var problemURL = `https://leetcode.com/problems/${filteredquestions[randomQuestion].titleSlug}`;
      document.getElementById("problemURL").setAttribute("href", problemURL);
      document.getElementById("problemURL").style.display = "";
      document.getElementById("question").innerHTML=filteredquestions[randomQuestion].titleSlug;
      document.getElementById("difficulty").innerHTML=difficulty;
    })
    .catch(error => {
      document.getElementById("question").innerHTML=error; 
    });
});

console.clear();

const loginBtn = document.getElementById('login');
const signupBtn = document.getElementById('signup');

loginBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode.parentNode;
	Array.from(e.target.parentNode.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			signupBtn.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});

signupBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode;
	Array.from(e.target.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			loginBtn.parentNode.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});

// signUp Button
const signupBtn1 = document.getElementById('submit-btn-signup');

signupBtn1.addEventListener('click', (e) => {
  var signupDiv = document.getElementById("signupDiv");
  var loginDiv = document.getElementById("loginDiv");
  signupDiv.classList.add("slide-up");
  loginDiv.classList.remove("slide-up");

  // display the problem solved status
  let leetCodeId = document.getElementById("leetcodeId").value;
  console.log('username: ' + leetCodeId);
  fetch(`https://salty-waters-49462.herokuapp.com/leetcode-stats-six.vercel.app/api?username=${leetCodeId}&theme=dark`, {'Access-Control-Allow-Origin': '*'})
      .then(response => response.text())
      .then(data => {
        console.log(data);
        document.getElementById("stats").innerHTML=data; 
      }).catch((err) => {
        document.getElementById("stats").innerHTML=err; 
        console.log('error: ', err);
      });
  
	// let parent = e.target.parentNode.parentNode;
	// Array.from(e.target.parentNode.parentNode.classList).find((element) => {
	// 	if(element !== "slide-up") {
	// 		parent.classList.add('slide-up')
	// 	}else{
	// 		signupBtn.parentNode.classList.add('slide-up')
	// 		parent.classList.remove('slide-up')
	// 	}
	// });
});