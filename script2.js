function validate(){

	
	
    if(document.form_1.product1.value != ""){
		if(document.form_1.min_price1.value == ""){
			alert('please choose the minimum price');
			document.form_1.min_price1.focus();
			return false;
		}
		if(document.form_1.max_price1.value == ""){
			alert('please choose the maximum price');
			document.form_1.max_price1.focus();
			return false;
		}
		if(document.form_1.reputation1.value == ""){
			alert('please choose the reputation');
			document.form_1.reputation1.focus();
			return false;
		}
		if(parseFloat(document.form_1.min_price1.value)> parseFloat(document.form_1.max_price1.value)){
			alert('minimum price has to be lower than maximum');
			document.form_1.min_price1.value="";
			document.form_1.max_price1.value="";			
			document.form_1.min_price1.focus();
			document.form_1.max_price1.focus();
			return false;
		}
    }

    
	
    if(document.form_1.product2.value != ""){
		if(document.form_1.min_price2.value == ""){
			alert('please choose the minimum price');
			document.form_1.min_price2.focus();
			return false;
		}
		if(document.form_1.max_price2.value == ""){
			alert('please choose the maximum price');
			document.form_1.max_price2.focus();
			return false;
		}
		if(document.form_1.reputation2.value == ""){
			alert('please choose the reputation');
			document.form_1.reputation2.focus();
			return false;
		}
		if(parseFloat(document.form_1.min_price2.value)> parseFloat(document.form_1.max_price2.value)){
			alert('minimum price has to be lower than maximum');
			document.form_1.min_price2.value="";
			document.form_1.max_price2.value="";			
			document.form_1.min_price2.focus();
			document.form_1.max_price2.focus();
			return false;
		}
    }
	
	
	
    if(document.form_1.product3.value != ""){
		if(document.form_1.min_price3.value == ""){
			alert('please choose the minimum price');
			document.form_1.min_price3.focus();
			return false;
		}
		if(document.form_1.max_price3.value == ""){
			alert('please choose the maximum price');
			document.form_1.max_price3.focus();
			return false;
		}
		if(document.form_1.reputation3.value == ""){
			alert('please choose the reputation');
			document.form_1.reputation3.focus();
			return false;
		}
		if(parseFloat(document.form_1.min_price3.value)>= parseFloat(document.form_1.max_price3.value)){
			alert('minimum price has to be lower than maximum');
			document.form_1.min_price3.value="";
			document.form_1.max_price3.value="";			
			document.form_1.min_price3.focus();
			document.form_1.max_price3.focus();
			return false;
		}
    }
	
    if(document.form_1.product4.value != ""){
		if(document.form_1.min_price4.value == ""){
			alert('please choose the minimum price');
			document.form_1.min_price4.focus();
			return false;
		}
		if(document.form_1.max_price4.value == ""){
			alert('please choose the maximum price');
			document.form_1.max_price4.focus();
			return false;
		}
		if(document.form_1.reputation4.value == ""){
			alert('please choose the reputation');
			document.form_1.reputation4.focus();
			return false;
		}
		if(parseFloat(document.form_1.min_price4.value)>= parseFloat(document.form_1.max_price4.value)){
			alert('minimum price has to be lower than maximum');
			document.form_1.min_price4.value="";
			document.form_1.max_price4.value="";			
			document.form_1.min_price4.focus();
			document.form_1.max_price4.focus();
			return false;
		}
    }
	
	
    if(document.form_1.product5.value != ""){
		if(document.form_1.min_price5.value == ""){
			alert('please choose the minimum price');
			document.form_1.min_price5.focus();
			return false;
		}
		if(document.form_1.max_price5.value == ""){
			alert('please choose the maximum price');
			document.form_1.max_price5.focus();
			return false;
		}
		if(document.form_1.reputation5.value == ""){
			alert('please choose the reputation');
			document.form_1.reputation5.focus();
			return false;
		}
		if(parseFloat(document.form_1.min_price5.value)> parseFloat(document.form_1.max_price5.value)){
			alert('minimum price has to be lower than maximum');
			document.form_1.min_price5.value="";
			document.form_1.max_price5.value="";			
			document.form_1.min_price5.focus();
			document.form_1.max_price5.focus();
			return false;
		}
    }
return true;
}