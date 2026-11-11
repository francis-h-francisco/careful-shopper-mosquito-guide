/* Phone menu: the Menu button opens the same five links one under another. */
(function () {
	var button = document.querySelector('.cs-menu-button');
	var menu = document.getElementById(button ? button.getAttribute('aria-controls') : '');
	if (!button || !menu) return;

	function setOpen(open) {
		button.setAttribute('aria-expanded', open ? 'true' : 'false');
		menu.classList.toggle('is-open', open);
	}
	button.addEventListener('click', function () {
		setOpen(button.getAttribute('aria-expanded') !== 'true');
	});
	menu.addEventListener('click', function (event) {
		if (event.target.closest('a')) setOpen(false);
	});
	document.addEventListener('keydown', function (event) {
		if (event.key === 'Escape' && menu.classList.contains('is-open')) {
			setOpen(false);
			button.focus();
		}
	});
	document.addEventListener('click', function (event) {
		if (!menu.contains(event.target) && !button.contains(event.target)) setOpen(false);
	});
})();
