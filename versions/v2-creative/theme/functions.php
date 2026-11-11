<?php
/**
 * Careful Shopper Field Guide: web fonts, the child stylesheet and the page script.
 * The fonts fall back to local serif and sans-serif faces if Google Fonts cannot be reached.
 */
add_action('wp_enqueue_scripts', function () {
    $version = wp_get_theme()->get('Version');
    wp_enqueue_style('careful-shopper-fonts', 'https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap', array(), null);
    wp_enqueue_style('careful-shopper', get_stylesheet_uri(), array('careful-shopper-fonts'), $version);
    wp_enqueue_script('careful-shopper-menu', get_stylesheet_directory_uri() . '/menu.js', array(), $version, array('strategy' => 'defer', 'in_footer' => true));
});

add_filter('wp_resource_hints', function ($urls, $relation) {
    if ('preconnect' === $relation) {
        $urls[] = array('href' => 'https://fonts.gstatic.com', 'crossorigin');
        $urls[] = 'https://fonts.googleapis.com';
    }
    return $urls;
}, 10, 2);
