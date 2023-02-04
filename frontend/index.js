var getJSON = function(url, callback) {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', url, true);
	xhr.responseType = 'json';
	xhr.onload = function() {
		var status = xhr.status;
		if (status === 200) {
			callback(null, xhr.response);
		} else {
			callback(status, xhr.response);
		}
	};
	xhr.send();
};


// hiding the toggle button initially
// when no problem slug is loaded
// this is slow, and displays the button for some time then hides
// TODO: find a better way
document.getElementById('toggle-button').style.visibility = 'hidden'

const next_button = document.getElementById('next-button');
const toggle_button = document.getElementById('toggle-button')

var problem_statement = ''
var solution = ''
var toggle_show = 0

next_button.addEventListener('click', () => {
	const content = document.querySelector('p')
	getJSON('http://localhost:8000/next-problem-slug', function(err, data) {
		if (err !== null) {
			console.log('unable to fetch data from the server')
		} else {
			current_problem_slug = data
			getJSON(`http://localhost:8000/statement/${current_problem_slug}`, function(err, data) {
				if (err !== null) {
					console.log('unable to fetch data from the server')
				} else {
					document.getElementById('toggle-button').style.visibility = 'visible'
					content.innerHTML = data
					problem_statement = data
				}
			})
			getJSON(`http://localhost:8000/solution/${current_problem_slug}`, function(err, data) {
				if (err !== null) {
					console.log('unable to fetch data from the server')
				} else {
					document.getElementById('toggle-button').style.visibility = 'visible'
					solution = data
				}
			})
		}
	})
})

toggle_button.addEventListener('click', () => {
	const content = document.querySelector('p')
	if (toggle_show === 0) {
		content.innerHTML = solution
		toggle_show = 1
	} else {
		content.innerHTML = problem_statement
		toggle_show = 0
	}
})

