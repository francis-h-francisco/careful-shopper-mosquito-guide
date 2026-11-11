"""The guide copy, shared by both versions.

Source: 20261005-MosquitoBlog (what goes in each zone) and the Careful Shopper Style Sheet.
Both versions render this same data, so the words never drift apart. Do not add products,
prices, ratings, dates, brand names or bracketed notes here.
"""

SITE_NAME = "Careful Shopper"
TAGLINE = "Products that work better together"

NAV = [
    ("Home", "/"),
    ("Shopping Index", "/shopping-index/"),
    ("Mosquito Protection", "/#top"),
    ("About Mrs. Shopper", "/about-mrs-shopper/"),
    ("Contact", "/contact/"),
]
CURRENT_NAV = "Mosquito Protection"

BREADCRUMB = ["Bug and pest protection", "Mosquito barriers"]
TITLE = "Keep Mosquitoes From Biting: Barrier Nets and Screens for Every Space"
BYLINE = "By Mrs. Shopper."
SHORT_ANSWER = ("<strong>Short answer:</strong> Stop mosquitoes with physical barriers, reduce them around "
                "your home, and keep bite relief on hand. This page covers the first layer: nets and screens "
                "that keep mosquitoes out.")

DISCLOSURE = ("Mrs. Shopper explains: I put affiliate sales links on this website. If you buy any products "
              "using these links, I may earn a small commission at no extra cost to you. As an Amazon "
              "Associate, I earn from qualifying purchases.")

PHOTO_ALT = "Close-up of skin with a raised, pale mosquito bite bump surrounded by redness"
PHOTO_CREDIT = "Dreamstime_216036901"

WHY_TITLE = "Why do mosquitoes bite in the first place?"
WHY = [
    "Not all mosquito species target humans, and among the ones that do, only the females bite. A female "
    "mosquito needs the protein and iron found in blood to develop her eggs. The hunt begins when she tracks "
    "your exhaled carbon dioxide (CO2), body heat, and unique skin scent. Once she lands, she searches for "
    "exposed skin and uses specialized mouthparts to pierce it. As she feeds, she injects saliva containing "
    "anticoagulants and mild anesthetics so you don’t feel the initial bite.",
    "Later, your immune system reacts to the proteins in that saliva, triggering the inflammation, redness, "
    "and itch you know all too well.",
]
RISK_TITLE = "One bite can carry more than an itch"
RISK = [
    "When a mosquito bites, her sharp needle-like mouthpart (called a proboscis) goes straight into your skin. "
    "Germs and tiny parasites can live inside this tube and slip right into your blood before you even notice. "
    "You may already know about West Nile Virus or Malaria, but mosquitoes also carry lesser-known threats like "
    "Dengue, Chikungunya, and Eastern Equine Encephalitis. These illnesses can cause high fevers, painful joint "
    "aches, and even dangerous brain swelling. Just one bite can put a healthy person in the hospital, but you "
    "can block these pests before they reach you. Essential protection includes bed nets for night, stroller "
    "netting for baby strollers, strong insect repellents, outdoor bug zappers, smoke coils, and clothing sprays "
    "containing Permethrin, which kills mosquitoes on contact when they land.",
]

LAYERS_TITLE = "Three layers, because one layer fails alone"
LAYERS = [
    ("Layer 1: Block", "Nets and screens keep mosquitoes away from skin.", True),
    ("Layer 2: Reduce", "Repellents, traps, and standing-water control cut how many are around.", False),
    ("Layer 3: Relieve", "Creams and balms calm the bites that still get through.", False),
]
YOU_ARE_HERE = "You are here."
LAYERS_CLOSE = ("A net can’t follow you outdoors, and repellent wears off overnight. "
                "Each layer covers the other’s gap.")

TABLE_TITLE = "Compare the barriers at a glance"
TABLE_HEAD = ("Barrier", "Best for", "Covers", "Setup")
TABLE = [
    ("Magnetic doorway screen", "Busy doors, pets", "One doorway", "Minutes, snaps shut on its own"),
    ("Pyramid bed and camping net", "Beds and camping cots", "Single to king bed", "Hangs from one point"),
    ("Glow-in-the-dark bed canopy", "Kids’ rooms", "Single, twin, or full bed", "Hangs from one ceiling point"),
    ("Bed netting cube", "Sleepers who want more room", "One bed", "Six hanging loops"),
    ("Baby and stroller netting", "Strollers, car seats, bassinets", "One seat", "Elastic drawstring"),
    ("Outdoor umbrella enclosure", "Patios, group campsites", "Umbrella up to 11 feet", "Tent pins or weight bags"),
]

BARRIERS_TITLE = "Barriers that keep every flying insect out"
BARRIERS_INTRO = ("If mosquitoes mostly come in through one door, start with the doorway screen. If you sleep "
                  "somewhere you can’t seal, choose a bed net. If you spend evenings outside, the umbrella "
                  "enclosure covers a group. You can view current specifications and availability for each one "
                  "on Amazon.")
_S = "https://www.amazon.com/s?k="
BARRIERS = [
    ("Doorway Screen With Magnetic Closure", _S + "magnetic+doorway+mosquito+screen", None,
     [("Best for:", "Doors that open all day"),
      ("Works with:", "A bed net, for mosquitoes that slip in overnight."),
      ("Trade-off:", "Doorways only, so measure the frame first.")]),
    ("Pyramid Bed and Camping Net", _S + "pyramid+mosquito+net+bed+camping", None,
     [("Best for:", "Nights at home or camping"),
      ("Works with:", "A doorway screen, so fewer mosquitoes get in."),
      ("Trade-off:", "Needs an overhead hook. Tuck in the edges.")]),
    ("Glow-in-the-Dark Bed Canopy", _S + "glow+in+the+dark+mosquito+net+bed+canopy", None,
     [("Best for:", "Kids’ bedrooms"),
      ("Works with:", "Bite relief, for bites picked up outdoors."),
      ("Trade-off:", "The stars need daylight to glow.")]),
    ("Roomy Bed Netting Cube", _S + "rectangular+bed+mosquito+net+cube", None,
     [("Best for:", "Sleepers who want room to sit up"),
      ("Works with:", "A doorway screen, to keep the room clearer."),
      ("Trade-off:", "More hanging points to set up.")]),
    ("Baby and Stroller Netting", _S + "baby+stroller+mosquito+net", None,
     [("Best for:", "Babies, who cannot swat mosquitoes"),
      ("Works with:", "A bed net, for naps and nights at home."),
      ("Trade-off:", "Check the stroller fit and the heat.")]),
    ("Outdoor Umbrella Enclosure", _S + "patio+umbrella+mosquito+net+enclosure", None,
     [("Best for:", "Backyard gatherings and group campsites"),
      ("Works with:", "Personal repellent, for guests walking to and from it."),
      ("Trade-off:", "Needs ground space for pins or weights.")]),
]

PAIRS_TITLE = "Add the other two layers"
PAIRS_INTRO = "Nets and screens block mosquitoes, but they cannot follow you outdoors. These products cover the gaps."
PAIRS = [
    ("20% Picaridin Repellent", "https://www.amazon.com/Ranger-Ready-Repellents-Picaridin-Repellent/dp/B07P4XC5VD",
     "Layer 2: Reduce",
     [("Best for:", "Skin protection outdoors"),
      ("Works with:", "The umbrella enclosure, for guests walking to and from it.")]),
    ("IR3535 Repellent Spray", "https://www.amazon.com/Warrior-DEET-Free-Shield-Spray/dp/B0DC7H1G46",
     "Layer 2: Reduce",
     [("Best for:", "Sensitive skin and evenings before bed"),
      ("Works with:", "A bed net, for the time before bed.")]),
    ("Permethrin Clothing Spray", "https://www.amazon.com/Sawyer-Products-Permethrin-Repellent-Clothing/dp/B0F29L8XXJ",
     "Layer 2: Reduce",
     [("Best for:", "Clothing and gear"),
      ("Works with:", "Nets and screens, for time spent outside a barrier."),
      ("Trade-off:", "Clothing only, never skin.")]),
    ("1% Hydrocortisone Cream", "https://www.amazon.com/Basic-Care-Hydrocortisone-Cream-Anti-Itch/dp/B0779CBH6S",
     "Layer 3: Relieve",
     [("Best for:", "Bites that still get through"),
      ("Works with:", "The bed canopy and bed nets, for bites picked up during the day."),
      ("Trade-off:", "Use sparingly in skin folds.")]),
    ("Calamine Lotion", "https://www.amazon.com/Calamine-Drying-Topical-Suspension-Protectant/dp/B00ILKHOBO",
     "Layer 3: Relieve",
     [("Best for:", "Gentle itch relief"),
      ("Works with:", "Hydrocortisone cream, between applications.")]),
]

CURATED_TITLE = "Curated by Mrs. Shopper"
BIO = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus "
       "ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent "
       "mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Nulla "
       "facilisi. Curabitur sodales.")
BIO_LINK = ("Read Mrs. Shopper’s full background", "/about-mrs-shopper/")
NO_SPONSORS = "Careful Shopper accepts no sponsorships from manufacturers or brands."
FOOTER_LINKS = [
    ("About Mrs. Shopper", "/about-mrs-shopper/"),
    ("How we choose products", "/how-we-choose-products/"),
    ("Affiliate disclosure", "/#affiliate-disclosure"),
    ("Contact", "/contact/"),
    ("Privacy policy", "/privacy-policy/"),
]
COPYRIGHT = "© 2026 Careful Shopper"

# Shown on links in the menu and footer whose pages are outside this one-page test.
NOT_BUILT_TITLE = "This page is not part of the test"
NOT_BUILT_TEXT = "The test builds one blog page only. This link is kept so the header and footer look complete."
NOT_BUILT_LINK = ("Read the mosquito protection guide", "/")

BUTTON_LABEL = "See Example"


def caption_words(lines):
    return sum(len((lead + " " + text).split()) for lead, text in lines)


for _name, _url, _layer, _lines in BARRIERS + [(n, u, l, c) for n, u, l, c in PAIRS]:
    assert caption_words(_lines) <= 30, (_name, caption_words(_lines))
