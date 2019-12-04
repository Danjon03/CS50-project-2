document.addEventListener('DOMContentLoaded', () => 
{
		
	
	
	namespace = '/test2';
	var socket = io(namespace);
	
		
	
	socket.on('connect', function() {
		//for testing if connection exists only
		//alert("connected")
	
		document.querySelector('#btn2').onclick = () => 
		{
			localStorage.clear();
		};
	});
});