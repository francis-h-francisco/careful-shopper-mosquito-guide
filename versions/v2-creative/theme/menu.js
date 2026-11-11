/* Version 2: phone menu, the "On this page" box, and the current-section highlight. */
(function () {
	var button = document.querySelector('.fg-menu-button');
	var menu = document.getElementById(button ? button.getAttribute('aria-controls') : '');
	if (button && menu) {
		var setOpen = function (open) {
			button.setAttribute('aria-expanded', open ? 'true' : 'false');
			menu.classList.toggle('is-open', open);
		};
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
	}

	/* The contents box stays open beside the guide on wide screens and folds away on phones. */
	var box = document.querySelector('.fg-toc__box');
	if (!box) return;
	var wide = window.matchMedia('(min-width: 64rem)');
	var sync = function () { if (wide.matches) box.open = true; };
	sync();
	if (wide.addEventListener) wide.addEventListener('change', sync);
	box.addEventListener('click', function (event) {
		if (event.target.closest('a') && !wide.matches) box.open = false;
	});

	if (!('IntersectionObserver' in window)) return;
	var links = Array.prototype.slice.call(box.querySelectorAll('a[href^="#"]'));
	var byId = {};
	links.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
	var observer = new IntersectionObserver(function (entries) {
		entries.forEach(function (entry) {
			if (!entry.isIntersecting) return;
			links.forEach(function (a) { a.classList.remove('is-active'); a.removeAttribute('aria-current'); });
			var link = byId[entry.target.id];
			if (link) { link.classList.add('is-active'); link.setAttribute('aria-current', 'location'); }
		});
	}, { rootMargin: '-30% 0px -60% 0px' });
	Object.keys(byId).forEach(function (id) {
		var section = document.getElementById(id);
		if (section) observer.observe(section);
	});
})();
