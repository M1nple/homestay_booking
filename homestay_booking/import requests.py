		var name // tạo biến kh có khởi tạo
		var name1 = 'Minh' // biến có khởi tạo
		// 
		name = window.prompt(" nhập tên: ") // nhập từ trình duyệt vào biến name
		hello = 'xin chào ' + name // nối chuỗi 
		// console.log(hello) // in ra console trong f12
		document.write( hello ) // in ra hiển thị trên web
		var yob = window.prompt("nhập năm sinh: ")
		var age = 2025 - yob // toán tử + - * / <>
		var tuoi = " | Năm nay " + name +" "+ age + " tuổi"
		document.write(tuoi)
