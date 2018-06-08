var firebase = require('firebase')
var ref = require('instagram-id-to-url-segment')

firebase.initializeApp({
	serviceAccount : "./placeness_firebase.json",
	databaseURL : "https://placenessdb.firebaseio.com/"
});

var uid = "ldnhCzFzM7gAU4oxso91hWtEjm72";
var customToken = firebase.auth().createCustomToken(uid); 


function read_once (refpath, callback) { 
	var destref = firebase.database().ref(refpath); 

	destref.once('value').then(function(data) {
		callback(data)
	})
}

function update(refpath, object) {
	firebase.database().ref(refpath).update(object);
}


var postcode = ref.instagramIdToUrlSegment('965007537950924946')
console.log(postcode)

/*
 
firebase.database().ref().child('experiment3').once('value').then(function(data) {	
	for (var place in data.val()) {
		for (var post in data.val()[place]) {
			console.log(place+"/"+post)
			var postid = data.val()[place][post]['id'];
			console.log(postid);
			var postcode = ref.instagramIdToUrlSegment(postid.toString())
			console.log(postcode);
			firebase.database().ref('experiment3/'+place+'/'+post).update({posturl:postcode})
		}
		
	}	
}) 
*/

/*
var refpath = 'experiment3'
var destref = firebase.database().ref().child(refpath); 
destref.once('value').then(function(data) { 
	data.foreach(function(place) {
		console.log(place)
		place.foreach(function(post) {
			console.log(place+"\t"+post)
			 
			console.log(post);
			var postid = post.val()['id'];
			console.log(postid);
			var postcode = ref.instagramIdToUrlSegment(postid.toString())
			console.log(postcode)
			
			firebase.database().ref('experiment/'+place+'/'+post).update({posturl:postcode});

		})
	}) 
}) 
*/

/*
 var refpath = 'experiment/coex/12341234' 
var destref = firebase.database().ref().child(refpath); 
destref.once('value').then(function(data) {
	//console.log(data.val());
	var postid = data.val()['id'];
	//console.log(postid);
	var postcode = ref.instagramIdToUrlSegment(postid.toString())
	//console.log(postcode)
	
	firebase.database().ref(refpath).update({posturl:postcode});


	
}) 

 */

/*
console.log("hello")
 
firebase.database().ref('experiment/coex/964871337132966645').once('value').then(function(data) {
	console.log("1")

	data.foreach(function (exSnapshotChild) {
		console.log("2")
		console.log(exSnapshotChild.val())		
	})
	console.log("3")		
})

console.log("4")
*/

/*
var ref, urlSegmentToInstagramId, instagramIdToUrlSegment;
ref = require('instagram-id-to-url-segment')
instagramIdToUrlSegment = ref.instagramIdToUrlSegment
urlSegmentToInstagramId = ref.urlSegmentToInstagramId;
 
console.log(instagramIdToUrlSegment('1038059720608660215')); // 5n7dDmhTr3 
console.log(urlSegmentToInstagramId('5n7dDmhTr3')); // 1038059720608660215 


console.log(instagramIdToUrlSegment('965102497338184481'));  
 */