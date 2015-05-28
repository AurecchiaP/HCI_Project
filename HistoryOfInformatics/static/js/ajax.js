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
	window.title = json['title']

	// Take the title from the webpage
	// var newTitle = $('div.title.hidden').html();
	// if (newTitle != undefined) {
	// 	document.title = newTitle
	// 	$('div.title.hidden').remove();
	// };

	// Intercept clicks on links - new watcher has to be made to apply to the new links
	$('a').click(function(event){
		event.preventDefault();
		setupAndSendAjaxRequest($(this).attr('href'));
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

// Called when page has loaded
function documentReady () {

	// var jsonDict = {"body": "<div id=\"wrapper\">\n        <div id=\"navbar\">\n            <div id=\"nav_search_mobile\">\n                <form action=\"get\">\n                    <input id=\"search_field\" autocomplete=\"off\" name=\"search\" type=\"text\" placeholder=\"TO BE CHANGED\">\n                    <input id=\"search_submit\" value=\"\" type=\"image\" src=\"images/search.png\">\n                </form>\n            </div>\n            <!--            <a href=\"#\" id=\"menu-icon\">&#9776;</a>-->\n            <ul>\n                <li class=\"nav_home selected\"><a href=\"../index.html\">HOME</a>\n                </li>\n                <li class=\"nav_software\"><a href=\"#\">SOFTWARE</a>\n                </li>\n                <li class=\"nav_hardware\"><a href=\"#\">HARDWARE</a>\n                </li>\n                <li class=\"nav_internet\"><a href=\"#\">INTERNET</a>\n                </li>\n                <li class=\"nav_games\"><a href=\"#\">GAMES</a>\n                </li>\n                <li class=\"nav_hci\"><a href=\"#\">HCI</a>\n                </li>\n                <div id=\"nav_search\">\n                    <form action=\"get\">\n                        <input id=\"search_field\" autocomplete=\"off\" name=\"search\" type=\"text\" placeholder=\"Search...\">\n                        <input id=\"search_submit\" value=\"\" type=\"image\" src=\"images/search.png\">\n                    </form>\n                </div>\n            </ul>\n        </div>\n        <div id=\"externalContainer\">\n            <div id=\"contentContainer\">\n                <h1>History of Informatics</h1>\n                <div id=\"sectionSelector\">\n                    <div class=\"row\">\n                        <div id=\"softwareIcon\" class=\"di_o\"><img src=\"images/icons/software_w.png\" alt=\"softwareIcon\">\n                        </div>\n                        <span id=\"softwareName\">Software</span>\n                    </div>\n                    <div class=\"row\">\n                        <div id=\"hardwareIcon\" class=\"di_o\"><img src=\"images/icons/hardware_w.png\" alt=\"hardwareIcon\">\n                        </div>\n                        <span id=\"hardwareName\">Hardware</span>\n                    </div>\n                    <div class=\"row\">\n                        <div id=\"internetIcon\" class=\"di_o\"><img src=\"images/icons/internet_w.png\" alt=\"internetIcon\">\n                        </div>\n                        <span id=\"internetName\">Internet</span>\n                    </div>\n                    <div class=\"row\">\n                        <div id=\"gamesIcon\" class=\"di_o\"><img src=\"images/icons/games_w.png\" alt=\"gamesIcon\">\n                        </div>\n                        <span id=\"gamesName\">Games</span>\n                    </div>\n                    <div class=\"row\">\n                        <div id=\"hciIcon\" class=\"di_o\"><img src=\"images/icons/hci_w.png\" alt=\"hciIcon\">\n                        </div>\n                        <span id=\"hciName\">HCI</span>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>", "title":"History Of Informatics"}
	// console.log(JSON.stringify(jsonDict));

	// When first loaded (after function definitions), check to see if it needs to redirect you because of a hash
	dealWithHash();
}