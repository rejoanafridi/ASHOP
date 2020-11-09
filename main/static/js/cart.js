var updateBtns = document.getElementsByClassName("update-cart");

for (var i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener("click", function () {
		var productId = this.dataset.product;
		var action = this.dataset.action;
		console.log("productId:", productId, "Action:", action);

		console.log("user:", user);
		if (user === "AnonymousUser") {
			console.log("Not Logged In");
		} else {
			console.log("User is logged in, sending data");
		}
	});
}
