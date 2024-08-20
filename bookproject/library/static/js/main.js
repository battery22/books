console.log('hello');
function isWebp() {
	//is it webp
	function testWebP(callback) {

		var webP = new Image();
		webP.onload = webP.onerror = function () {
			callback(webP.height == 2);
		};
		webP.src = "data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA";
	}
	//add class _web or _no-web for tag HTML
	testWebP(function (support) {
			var className = support === true ? 'webp' : 'no-webp';
			document.documentElement.classList.add(className);
	});
}
 
isWebp();

