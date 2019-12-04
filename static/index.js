
					localStorage.clear();
	
	
	
	document.addEventListener('DOMContentLoaded', () => {
		document.getElementById("invisibleButton").style.display="none";
	document.getElementById("userName").style.display="none";
	document.getElementById("chat").style.display="none";
		
		
		namespace = '/test2';
		var socket = io(namespace);
	
		
	
		socket.on('connect', function() {
			//for testing if connection exists only
			//alert("connected")
			
			if(localStorage.getItem('usersName') === null && localStorage.getItem('lastChat') === null)
			{
				//alert("local Storage is empty");
			
			}
			
			else if (localStorage.getItem('lastChat') === null)
			{
				document.querySelector("#form").value = localStorage.getItem('usersName');
				
				document.querySelector("#btn").click();
				
			}
			else
			{
				//alert("made it to the else " + localStorage.getItem('lastChat') + " " + localStorage.getItem('usersName'));
				
				document.querySelector("#userName").value = localStorage.getItem('usersName');
				
				document.querySelector("#chat").value = localStorage.getItem('lastChat');
				
				
				
				document.querySelector("#invisibleButton").click();
					
					
					
					
					
					
					
				
				
				
			}
			
			document.querySelector('#btn').onclick = () => {
				//alert("in here current ");
				if(!localStorage.getItem('usersName'))
					localStorage.setItem('usersName', document.querySelector("#form").value);
				
				
				// when you get back this needs to set the local storage to the name
			
			
			
			};
			
		});
	
	
	});
