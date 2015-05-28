// TODO loading icon

$(document).ready(function(){
	documentReady();
});

// $(window).unload(function(){
// 	resetPage();
// });

// Listen for hash changes
window.addEventListener("hashchange", dealWithHash);

// Variable containing the div which always gets updated

// Ignore hash changes
var _ignoreHashChangeOnce = false;
var _currentSection = "";

// Function to send GET Ajax request
function sendAjaxRequest (url, callback) {
	window.location.hash = url;
	var xmlhttp;
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }

	// Has the request finished?
	xmlhttp.onreadystatechange=function(){
	  
	  if (xmlhttp.readyState==4 && xmlhttp.status==200) { //The 0 is just because it seemed to not like it when run locally..
	  	hideProgressBar();
	  	callback(xmlhttp.responseText);
	  }else{
	  	// console.log('readyState: '+xmlhttp.readyState+', code: '+xmlhttp.status);
	  }

	}

	// Build request
	xmlhttp.open("GET",url,true);

	// Show the loading bar
	showLoadingAjax();
	
	// Finally submit the request
	xmlhttp.send();
}

// Helper method to replace an element's HTML
function replaceHTMLOfPage (content) {

	var json = $.parseJSON(content)

	// Set the new content
	console.log(json)
	$('body').html(json['body'].replace('<script src="../../js/timeline/js/storyjs-embed.js" type="text/javascript"></script>', ''));

    $('#topicMain img').each(function () {
    	if ($(this).attr('src') != "/arrow.png") {
    		$(this).attr('src', json['section']+"/"+$(this).attr('src'));
    	};
    });
	document.title = json['title'].toTitleCase();

	_currentSection = json['section']
	console.log("_currentSection: "+_currentSection)

	// Intercept clicks on links - new watcher has to be made to apply to the new links
	$('a:not(.ext)').click(function(event){
		event.preventDefault();
		var theLink = $(this).attr('href')
		if (theLink.indexOf('#') !=-1) {
			return false;
		};
		if (theLink.indexOf('/') == -1) {
			setupAndSendAjaxRequest("/"+_currentSection+"/"+theLink);
		}else{
			setupAndSendAjaxRequest(theLink.replace('../','/'));
		}
		
		return false;
	});
}


// Sends Ajax request and puts returned content into $('body')
function setupAndSendAjaxRequest (requestedPage) {
	sendAjaxRequest(requestedPage, function(data){
		replaceHTMLOfPage(data);
	});
}

// Prepare to show loading screen
function showLoadingAjax () {
	$('body').prepend('<div id="progressDiv"><span id="outerProgress"><span id="innerProgress"></span></span></div>');
	showProgressBar();
}

// Unhide progress bar
function showProgressBar () {
	$("#progressDiv").css('display', 'block');
	$("#progressDiv #innerProgress").addClass('animateProgress');
}

// Hide progress bar
function hideProgressBar () {
	$("#progressDiv").css('display', 'none');
	$("#progressDiv #innerProgress").removeClass('animateProgress');
}

// Parses hash and redirects if needed
function dealWithHash () {
	if (!_ignoreHashChangeOnce) {
		var hash = window.location.hash.substr(1);
		console.log('Hash changed to: '+hash);
		if (hash != '') {
			setupAndSendAjaxRequest(hash);
		}else{
			setupAndSendAjaxRequest('/home/');
		}
	}
	_ignoreHashChangeOnce = false;
}

function updateHashWithoutTriggeringChange(hash) {
	_ignoreHashChangeOnce = true;
	window.location.hash = hash
}

function resetPage () {
	setupAndSendAjaxRequest('/home/');
}

String.prototype.toTitleCase = function () {
    return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
};

// Called when page has loaded
function documentReady () {

	// When first loaded (after function definitions), check to see if it needs to redirect you because of a hash
	dealWithHash();
}