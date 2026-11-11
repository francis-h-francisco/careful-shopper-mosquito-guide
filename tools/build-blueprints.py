#!/usr/bin/env python3
"""Build the WordPress Playground blueprints from the editable sources in versions/.

Each version folder holds:
  theme/      a Twenty Twenty-Five child theme (style.css, functions.php, templates/, parts/, *.js)
  content/    guide.html: the page content, one wp:html block per zone
  version.json  name, slug, folder, title, option key

The build writes the child theme and a must-use plugin into the blueprint. The plugin
uploads the Zone 4 photo, creates the guide page from content/guide.html, and makes it
the static front page. Run:  python3 tools/build-blueprints.py
"""
import base64, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO = os.path.join(ROOT, "assets", "20261111-MosquitoBite.webp")
PHOTO_NAME = "20261111-MosquitoBite.webp"


def read_tree(folder):
    tree = {}
    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)
        if os.path.isdir(path):
            tree[name] = read_tree(path)
        else:
            with open(path, encoding="utf-8") as fh:
                tree[name] = fh.read()
    return tree


PLUGIN = r"""<?php
/**
 * Plugin Name: Careful Shopper Guide Import
 * Description: Creates the nine-zone mosquito guide page and sets it as the front page.
 */
add_action('init', function () {
    if (get_option('__OPTION__')) {
        return;
    }

    // Zone 4 photo: the mosquito-bite photo from the supplied rough draft (the flea photo is not used).
    $image_url = get_option('__OPTION___photo');
    if (!$image_url) {
        $bytes = base64_decode('__PHOTO__', true);
        if ($bytes === false) {
            return;
        }
        $upload = wp_upload_bits('__PHOTO_NAME__', null, $bytes);
        if (!empty($upload['error']) || empty($upload['url'])) {
            return;
        }
        $image_url = $upload['url'];
        update_option('__OPTION___photo', $image_url);
    }

    $content = <<<'GUIDE_HTML'
__CONTENT__
GUIDE_HTML;
    $content = str_replace('__PHOTO_URL__', esc_url($image_url), $content);

    // The page markup is trusted theme content; store it unfiltered so classes and ids survive.
    $kses_was_on = has_filter('content_save_pre', 'wp_filter_post_kses');
    kses_remove_filters();

    $page = array(
        'post_title'     => '__TITLE__',
        'post_name'      => 'mosquito-protection-guide',
        'post_status'    => 'publish',
        'post_type'      => 'page',
        'comment_status' => 'closed',
        'post_content'   => $content,
    );
    $existing = get_page_by_path('mosquito-protection-guide', OBJECT, 'page');
    if ($existing) {
        $page['ID'] = $existing->ID;
        $page_id = wp_update_post(wp_slash($page), true);
    } else {
        $page_id = wp_insert_post(wp_slash($page), true);
    }

    if ($kses_was_on) {
        kses_init_filters();
    }

    if (!is_wp_error($page_id) && $page_id) {
        update_option('show_on_front', 'page');
        update_option('page_on_front', (int) $page_id);
        update_option('__OPTION__', 1);
    }
});
"""


def render(version_dir):
    """Run the version's render.py so content/, parts/ and templates/ match guide_content.py."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("render_" + os.path.basename(version_dir),
                                                  os.path.join(version_dir, "render.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.render()


def build(version_dir):
    render(version_dir)
    meta = json.load(open(os.path.join(version_dir, "version.json"), encoding="utf-8"))
    content = open(os.path.join(version_dir, "content", "guide.html"), encoding="utf-8").read().strip()
    assert "GUIDE_HTML" not in content
    photo = base64.b64encode(open(PHOTO, "rb").read()).decode("ascii")
    plugin = (PLUGIN.replace("__OPTION__", meta["option"])
                    .replace("__PHOTO_NAME__", PHOTO_NAME)
                    .replace("__TITLE__", meta["page_title"].replace("'", "\\'"))
                    .replace("__CONTENT__", content)
                    .replace("__PHOTO__", photo))
    blueprint = {
        "$schema": "https://playground.wordpress.net/blueprint-schema.json",
        "meta": {"title": meta["title"], "description": meta["description"], "author": "Careful Shopper demo"},
        "landingPage": "/",
        "preferredVersions": {"php": "8.3", "wp": "latest"},
        "login": False,
        "steps": [
            {"step": "installTheme", "themeData": {"resource": "wordpress.org/themes", "slug": "twentytwentyfive"},
             "options": {"activate": False}},
            {"step": "setSiteOptions", "options": {
                "blogname": "Careful Shopper",
                "blogdescription": "Products that work better together"}},
            {"step": "writeFiles", "writeToPath": f"/wordpress/wp-content/themes/{meta['theme_folder']}",
             "filesTree": {"name": meta["theme_folder"], "files": read_tree(os.path.join(version_dir, "theme"))}},
            {"step": "writeFiles", "writeToPath": "/wordpress/wp-content/mu-plugins",
             "filesTree": {"name": "mu-plugins", "files": {"careful-shopper-guide-import.php": plugin}}},
            {"step": "activateTheme", "themeFolderName": meta["theme_folder"]},
        ],
    }
    out = os.path.join(ROOT, meta["blueprint"])
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(blueprint, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    # Keep a plain copy of the plugin for linting and review.
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    with open(os.path.join(ROOT, "build", f"{meta['slug']}-plugin.php"), "w", encoding="utf-8") as fh:
        fh.write(plugin)
    print(f"{meta['blueprint']}: {os.path.getsize(out):,} bytes")


if __name__ == "__main__":
    for name in sys.argv[1:] or ["v1-strict", "v2-creative"]:
        build(os.path.join(ROOT, "versions", name))
