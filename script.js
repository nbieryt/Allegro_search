function validate(){
    var product1 = document.getElementById('product1');
    var min_price1 = document.getElementById('min_price1');
    var max_price1 = document.getElementById('max_price1');
    var reputation1 = document.getElementById('reputation1');

	var product2 = document.getElementById('product2');
    var min_price2 = document.getElementById('min_price2');
    var max_price2 = document.getElementById('max_price2');
    var reputation2 = document.getElementById('reputation2');
	
	var product3 = document.getElementById('product3');
    var min_price3 = document.getElementById('min_price3');
    var max_price3 = document.getElementById('max_price3');
    var reputation3 = document.getElementById('reputation3');
	
	var product4 = document.getElementById('product4');
    var min_price4 = document.getElementById('min_price4');
    var max_price4 = document.getElementById('max_price4');
    var reputation4 = document.getElementById('reputation4');
	
	var product5 = document.getElementById('product5');
    var min_price5 = document.getElementById('min_price5');
    var max_price5 = document.getElementById('max_price5');
    var reputation5 = document.getElementById('reputation5');
	
	
    if(product1.value == ""){
        alert('please enter the product name');
        return false;
    }
    if(min_price1.value == ""){
        alert('please choose the minimum price');
        return false;
    }
    if(max_price1.value == ""){
        alert('please choose the maximum price');
        return false;
    }
	if(reputation1.value == ""){
        alert('please choose the reputation');
        return false;
    }
    
	
	
	if(product2.value != ""){
		if(min_price2.value == ""){
			alert('please choose the minimum price');
			return false;
		}
		if(max_price2.value == ""){
			alert('please choose the maximum price');
			return false;
		}
		if(reputation2.value == ""){
			alert('please choose the reputation');
			return false;
		}	
	}
	
	
	
	if(product3.value != ""){
		if(min_price3.value == ""){
			alert('please choose the minimum price');
			return false;
		}
		if(max_price3.value == ""){
			alert('please choose the maximum price');
			return false;
		}
		if(reputation3.value == ""){
			alert('please choose the reputation');
			return false;
		}	
	}
	
	
	if(product4.value != ""){
		if(min_price4.value == ""){
			alert('please choose the minimum price');
			return false;
		}
		if(max_price4.value == ""){
			alert('please choose the maximum price');
			return false;
		}
		if(reputation4.value == ""){
			alert('please choose the reputation');
			return false;
		}	
	}
	
	
	if(product5.value != ""){
		if(min_price5.value == ""){
			alert('please choose the minimum price');
			return false;
		}
		if(max_price5.value == ""){
			alert('please choose the maximum price');
			return false;
		}
		if(reputation5.value == ""){
			alert('please choose the reputation');
			return false;
		}	
	}

}