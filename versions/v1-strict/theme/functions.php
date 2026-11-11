<?php
/**
 * Careful Shopper Strict: load the child stylesheet and the phone menu script.
 */
add_action('wp_enqueue_scripts', function () {
    $version = wp_get_theme()->get('Version');
    wp_enqueue_style('careful-shopper', get_stylesheet_uri(), array(), $version);
    wp_enqueue_script('careful-shopper-menu', get_stylesheet_directory_uri() . '/menu.js', array(), $version, array('strategy' => 'defer', 'in_footer' => true));
});
