<?php
/**
 * Plugin Name: Careful Shopper Guide Import
 * Description: Creates the source-provided nine-zone guide as the Playground homepage once.
 */
add_action('init', function () {
    if (get_option('careful_shopper_guide_imported')) return;
    $content = <<<'GUIDE_HTML'
<header class="site-header">
 <div class="header-inner">
  <a class="brand" href="#top" aria-label="Careful Shopper home">
   <span class="brand-mark" aria-hidden="true">C</span>
   <span class="brand-copy"><span class="brand-name">Careful Shopper</span><span class="tagline">Products that work better together.</span></span>
  </a>
  <nav class="desktop-nav" aria-label="Main navigation">
   <a href="#top">Home</a><span class="nav-unavailable" aria-label="Shopping Index destination not supplied">Shopping Index</span>
   <a href="#hero">Mosquito Protection</a><a href="#curated">About Mrs. Shopper</a>
   <span class="nav-unavailable" aria-label="Contact destination not supplied">Contact</span>
  </nav>
  <button class="menu-button" id="menuButton" type="button" aria-expanded="false" aria-controls="mobileNav">Menu</button>
 </div>
 <nav class="mobile-nav" id="mobileNav" aria-label="Mobile navigation">
  <a href="#top">Home</a><span class="nav-unavailable" aria-label="Shopping Index destination not supplied">Shopping Index</span>
  <a href="#hero">Mosquito Protection</a><a href="#curated">About Mrs. Shopper</a>
  <span class="nav-unavailable" aria-label="Contact destination not supplied">Contact</span>
 </nav>
</header>
<main>
 <section class="zone hero" id="hero">
  <p class="breadcrumb">Home › Bug and pest protection › Mosquito barriers</p>
  <h1>Keep Mosquitoes From Biting: Barrier Nets and Screens for Every Space</h1>
  <p class="byline">By Mrs. Shopper.</p>
  <p class="short-answer"><strong>Short answer:</strong> Stop mosquitoes with physical barriers, reduce them around your home, and keep bite relief on hand. This page covers the first layer: nets and screens that keep mosquitoes out.</p>
 </section>
 <section class="zone disclosure" aria-label="Affiliate disclosure">
  Mrs. Shopper explains: I put affiliate sales links on this website. If you buy any products using these links, I may earn a small commission at no extra cost to you. As an Amazon Associate, I earn from qualifying purchases.
 </section>
 <section class="zone education" aria-labelledby="why-bite">
  <figure class="bite-photo-wrap" style="float:left;width:40%;max-width:26ch;margin:0 1.25rem .75rem 0">
   <img class="bite-photo" src="data:image/webp;base64,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" alt="Close-up of a mosquito bite showing swelling and a small blister" width="640" height="360">
   <figcaption class="photo-credit">Dreamstime_216036901</figcaption>
  </figure>
  <h2 id="why-bite">Why do mosquitoes bite in the first place?</h2>
  <p>Not all mosquito species target humans, and among the ones that do, only the females bite. A female mosquito needs the protein and iron found in blood to develop her eggs. The hunt begins when she tracks your exhaled carbon dioxide (CO2), body heat, and unique skin scent. Once she lands, she searches for exposed skin and uses specialized mouthparts to pierce it. As she feeds, she injects saliva containing anticoagulants and mild anesthetics so you don’t feel the initial bite.</p>
  <p>Later, your immune system reacts to the proteins in that saliva, triggering the inflammation, redness, and itch you know all too well.</p>
  <div class="education-second">
   <h2>One bite can carry more than an itch</h2>
   <p>When a mosquito bites, her sharp needle-like mouthpart (called a proboscis) goes straight into your skin. Germs and tiny parasites can live inside this tube and slip right into your blood before you even notice. You may already know about West Nile Virus or Malaria, but mosquitoes also carry lesser-known threats like Dengue, Chikungunya, and Eastern Equine Encephalitis. These illnesses can cause high fevers, painful joint aches, and even dangerous brain swelling. Just one bite can put a healthy person in the hospital, but you can block these pests before they reach you. Essential protection includes bed nets for night, stroller netting for baby strollers, strong insect repellents, outdoor bug zappers, smoke coils, and clothing sprays containing Permethrin, which kills mosquitoes on contact when they land.</p>
  </div>
 </section>
 <section class="zone layer-zone" aria-labelledby="layers-title">
  <h2 id="layers-title">Three layers, because one layer fails alone</h2>
  <div class="layer-grid">
   <article class="layer-card"><h3>Block</h3><p>Nets and screens keep mosquitoes away from skin. You are here.</p></article>
   <article class="layer-card"><h3>Reduce</h3><p>Repellents, traps, and standing-water control cut how many are around.</p></article>
   <article class="layer-card"><h3>Relieve</h3><p>Creams and balms calm the bites that still get through.</p></article>
  </div>
  <p class="layer-close">A net can’t follow you outdoors, and repellent wears off overnight. Each layer covers the other’s gap.</p>
 </section>
 <section class="zone comparison" aria-labelledby="compare-title">
  <h2 id="compare-title">Compare the barriers at a glance</h2>
  <div class="table-wrap" role="region" aria-label="Barrier comparison table" tabindex="0">
   <table>
    <thead><tr><th>Barrier</th><th>Best for</th><th>Covers</th><th>Setup</th></tr></thead>
    <tbody>
     <tr><td>Magnetic doorway screen</td><td>Busy doors, pets</td><td>One doorway</td><td>Minutes, snaps shut on its own</td></tr>
     <tr><td>Pyramid bed and camping net</td><td>Beds and camping cots</td><td>Single to king bed</td><td>Hangs from one point</td></tr>
     <tr><td>Glow-in-the-dark bed canopy</td><td>Kids’ rooms</td><td>Single, twin, or full bed</td><td>Hangs from one ceiling point</td></tr>
     <tr><td>Bed netting cube</td><td>Sleepers who want more room</td><td>One bed</td><td>Six hanging loops</td></tr>
     <tr><td>Baby and stroller netting</td><td>Strollers, car seats, bassinets</td><td>One seat</td><td>Elastic drawstring</td></tr>
     <tr><td>Outdoor umbrella enclosure</td><td>Patios, group campsites</td><td>Umbrella up to 11 feet</td><td>Tent pins or weight bags</td></tr>
    </tbody>
   </table>
  </div>
 </section>
 <section class="zone barrier-zone" aria-labelledby="barriers-title">
  <section class="disclosure" aria-label="Affiliate disclosure">
   Mrs. Shopper explains: I put affiliate sales links on this website. If you buy any products using these links, I may earn a small commission at no extra cost to you. As an Amazon Associate, I earn from qualifying purchases.
  </section>
  <h2 id="barriers-title" style="margin-top:1rem">Barriers that keep every flying insect out</h2>
  <p class="card-zone-intro">If mosquitoes mostly come in through one door, start with the doorway screen. If you sleep somewhere you can’t seal, choose a bed net. If you spend evenings outside, the umbrella enclosure covers a group. You can view current specifications and availability for each one on Amazon.</p>
  <div class="product-grid">
   <article class="product-card">
    <a class="product-window" href="https://www.amazon.com/s?k=magnetic+doorway+mosquito+screen" target="_blank" rel="noopener noreferrer" aria-label="See example results for Doorway Screen With Magnetic Closure">Product window</a>
    <h3>Doorway Screen With Magnetic Closure</h3>
    <p class="caption-line"><strong>Best for:</strong> Doors that open all day</p>
    <p class="caption-line"><strong>Works with:</strong> A bed net, for mosquitoes that slip in overnight.</p>
    <p class="caption-line"><strong>Trade-off:</strong> Doorways only, so measure the frame first.</p>
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/s?k=magnetic+doorway+mosquito+screen" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article><article class="product-card">
    <a class="product-window" href="https://www.amazon.com/s?k=pyramid+bed+camping+mosquito+net" target="_blank" rel="noopener noreferrer" aria-label="See example results for Pyramid Bed and Camping Net">Product window</a>
    <h3>Pyramid Bed and Camping Net</h3>
    <p class="caption-line"><strong>Best for:</strong> Nights at home or camping</p>
    <p class="caption-line"><strong>Works with:</strong> A doorway screen, so fewer mosquitoes get in.</p>
    <p class="caption-line"><strong>Trade-off:</strong> Needs an overhead hook. Tuck in the edges.</p>
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/s?k=pyramid+bed+camping+mosquito+net" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article><article class="product-card">
    <a class="product-window" href="https://www.amazon.com/s?k=glow+in+the+dark+mosquito+bed+canopy" target="_blank" rel="noopener noreferrer" aria-label="See example results for Glow-in-the-Dark Bed Canopy">Product window</a>
    <h3>Glow-in-the-Dark Bed Canopy</h3>
    <p class="caption-line"><strong>Best for:</strong> Kids’ bedrooms</p>
    <p class="caption-line"><strong>Works with:</strong> Bite relief, for bites picked up outdoors.</p>
    <p class="caption-line"><strong>Trade-off:</strong> The stars need daylight to glow.</p>
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/s?k=glow+in+the+dark+mosquito+bed+canopy" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article><article class="product-card">
    <a class="product-window" href="https://www.amazon.com/s?k=rectangular+mosquito+bed+net+cube" target="_blank" rel="noopener noreferrer" aria-label="See example results for Roomy Bed Netting Cube">Product window</a>
    <h3>Roomy Bed Netting Cube</h3>
    <p class="caption-line"><strong>Best for:</strong> Sleepers who want room to sit up</p>
    <p class="caption-line"><strong>Works with:</strong> A doorway screen, to keep the room clearer.</p>
    <p class="caption-line"><strong>Trade-off:</strong> More hanging points to set up.</p>
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/s?k=rectangular+mosquito+bed+net+cube" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article><article class="product-card">
    <a class="product-window" href="https://www.amazon.com/s?k=baby+stroller+mosquito+net" target="_blank" rel="noopener noreferrer" aria-label="See example results for Baby and Stroller Netting">Product window</a>
    <h3>Baby and Stroller Netting</h3>
    <p class="caption-line"><strong>Best for:</strong> Babies, who cannot swat mosquitoes</p>
    <p class="caption-line"><strong>Works with:</strong> A bed net, for naps and nights at home.</p>
    <p class="caption-line"><strong>Trade-off:</strong> Check the stroller fit and the heat.</p>
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/s?k=baby+stroller+mosquito+net" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article><article class="product-card">
    <a class="product-window" href="https://www.amazon.com/s?k=outdoor+patio+umbrella+mosquito+net+enclosure" target="_blank" rel="noopener noreferrer" aria-label="See example results for Outdoor Umbrella Enclosure">Product window</a>
    <h3>Outdoor Umbrella Enclosure</h3>
    <p class="caption-line"><strong>Best for:</strong> Backyard gatherings and group campsites</p>
    <p class="caption-line"><strong>Works with:</strong> Personal repellent, for guests walking to and from it.</p>
    <p class="caption-line"><strong>Trade-off:</strong> Needs ground space for pins or weights.</p>
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/s?k=outdoor+patio+umbrella+mosquito+net+enclosure" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article>
  </div>
 </section>
 <section class="zone pairing-zone" aria-labelledby="pairing-title">
  <section class="disclosure" aria-label="Affiliate disclosure">
   Mrs. Shopper explains: I put affiliate sales links on this website. If you buy any products using these links, I may earn a small commission at no extra cost to you. As an Amazon Associate, I earn from qualifying purchases.
  </section>
  <h2 id="pairing-title" style="margin-top:1rem">Add the other two layers</h2>
  <p class="card-zone-intro">Nets and screens block mosquitoes, but they cannot follow you outdoors. These products cover the gaps.</p>
  <div class="product-grid">
   <article class="product-card">
    <a class="product-window" href="https://www.amazon.com/Ranger-Ready-Repellents-Picaridin-Repellent/dp/B07P4XC5VD" target="_blank" rel="noopener noreferrer" aria-label="See example for 20% Picaridin Repellent">Product window</a>
    <h3>20% Picaridin Repellent</h3>
    <p class="caption-line"><strong>Best for:</strong> Skin protection outdoors</p>
    <p class="caption-line"><strong>Works with:</strong> The umbrella enclosure, for guests walking to and from it.</p>
    
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/Ranger-Ready-Repellents-Picaridin-Repellent/dp/B07P4XC5VD" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article><article class="product-card">
    <a class="product-window" href="https://www.amazon.com/Warrior-DEET-Free-Shield-Spray/dp/B0DC7H1G46" target="_blank" rel="noopener noreferrer" aria-label="See example for IR3535 Repellent Spray">Product window</a>
    <h3>IR3535 Repellent Spray</h3>
    <p class="caption-line"><strong>Best for:</strong> Sensitive skin and evenings before bed</p>
    <p class="caption-line"><strong>Works with:</strong> A bed net, for the time before bed.</p>
    
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/Warrior-DEET-Free-Shield-Spray/dp/B0DC7H1G46" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article><article class="product-card">
    <a class="product-window" href="https://www.amazon.com/Sawyer-Products-Permethrin-Repellent-Clothing/dp/B0F29L8XXJ" target="_blank" rel="noopener noreferrer" aria-label="See example for Permethrin Clothing Spray">Product window</a>
    <h3>Permethrin Clothing Spray</h3>
    <p class="caption-line"><strong>Best for:</strong> Clothing and gear</p>
    <p class="caption-line"><strong>Works with:</strong> Nets and screens, for time spent outside a barrier.</p>
    <p class="caption-line"><strong>Trade-off:</strong> Clothing only, never skin.</p>
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/Sawyer-Products-Permethrin-Repellent-Clothing/dp/B0F29L8XXJ" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article><article class="product-card">
    <a class="product-window" href="https://www.amazon.com/Basic-Care-Hydrocortisone-Cream-Anti-Itch/dp/B0779CBH6S" target="_blank" rel="noopener noreferrer" aria-label="See example for 1% Hydrocortisone Cream">Product window</a>
    <h3>1% Hydrocortisone Cream</h3>
    <p class="caption-line"><strong>Best for:</strong> Bites that still get through</p>
    <p class="caption-line"><strong>Works with:</strong> The bed canopy and bed nets, for bites picked up during the day.</p>
    <p class="caption-line"><strong>Trade-off:</strong> Use sparingly in skin folds.</p>
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/Basic-Care-Hydrocortisone-Cream-Anti-Itch/dp/B0779CBH6S" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article><article class="product-card">
    <a class="product-window" href="https://www.amazon.com/Calamine-Drying-Topical-Suspension-Protectant/dp/B00ILKHOBO" target="_blank" rel="noopener noreferrer" aria-label="See example for Calamine Lotion">Product window</a>
    <h3>Calamine Lotion</h3>
    <p class="caption-line"><strong>Best for:</strong> Gentle itch relief</p>
    <p class="caption-line"><strong>Works with:</strong> Hydrocortisone cream, between applications.</p>
    
    <div class="card-spacer"></div>
    <a class="product-cta" href="https://www.amazon.com/Calamine-Drying-Topical-Suspension-Protectant/dp/B00ILKHOBO" target="_blank" rel="noopener noreferrer">SEE EXAMPLE</a>
   </article>
  </div>
 </section>
 <section class="zone footer-zone" id="curated" aria-labelledby="curated-title">
  <h2 id="curated-title">Curated by Mrs. Shopper</h2>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vitae justo sed urna commodo aliquet. Donec at sapien non neque posuere tincidunt. Vivamus consequat, erat sed facilisis luctus, magna sem interdum arcu, sed suscipit nibh sapien vitae lorem. Praesent elementum, nibh sed tempor varius, risus nulla blandit sapien, sed luctus magna neque id augue.</p>
  <p>Careful Shopper accepts no sponsorships from manufacturers or brands.</p>
  <nav class="footer-nav" aria-label="Footer navigation">
   <a href="#curated">About Mrs. Shopper</a>
   <span class="nav-unavailable" aria-label="How we choose products destination not supplied">How we choose products</span>
   <span class="nav-unavailable" aria-label="Affiliate disclosure destination not supplied">Affiliate disclosure</span>
   <span class="nav-unavailable" aria-label="Contact destination not supplied">Contact</span>
   <span class="nav-unavailable" aria-label="Privacy policy destination not supplied">Privacy policy</span>
  </nav>
  <p class="footer-note">Some navigation destinations were not included in the supplied test materials. Zone 7 links are Amazon category searches for this test, not verified individual listings or confirmed affiliate-tracked links.</p>
  <p class="copyright">© 2026 Careful Shopper</p>
 </section>
</main>
GUIDE_HTML;
    $page_id = wp_insert_post(array(
        'post_title' => 'Keep Mosquitoes From Biting: Barrier Nets and Screens for Every Space',
        'post_name' => 'mosquito-protection-guide',
        'post_status' => 'publish',
        'post_type' => 'page',
        'post_content' => $content
    ));
    if (!is_wp_error($page_id) && $page_id) {
        update_option('show_on_front', 'page');
        update_option('page_on_front', $page_id);
        update_option('careful_shopper_guide_imported', 1);
    }
});
