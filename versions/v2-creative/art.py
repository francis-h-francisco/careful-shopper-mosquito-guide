"""Version 2 line illustrations, drawn for this guide (no stock downloads, no brands).

Each drawing is a 64 x 64 line icon in currentColor, so CSS sets its color. They are
decorative: every <svg> is aria-hidden and the text beside it carries the meaning.
"""

_OPEN = ('<svg class="{cls}" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2.25" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">')
_MESH = 'stroke-width="1.25" opacity=".45"'

DRAWINGS = {
    # Barriers
    "door": f'<rect x="16" y="7" width="32" height="51" rx="2"/><path d="M32 7v51"/>'
            f'<path {_MESH} d="M16 15h32M16 23h32M16 31h32M16 39h32M16 47h32M24 7v51M40 7v51"/>'
            '<circle cx="29.5" cy="33" r="1.8" fill="currentColor"/><circle cx="34.5" cy="33" r="1.8" fill="currentColor"/>'
            '<path d="M10 58h44"/>',
    "pyramid": '<circle cx="32" cy="6" r="2"/><path d="M32 8 11 46h42Z"/>'
               f'<path {_MESH} d="M32 8 25 46M32 8l7 38M18 34h28M22 26h20"/>'
               '<rect x="9" y="46" width="46" height="8" rx="2"/><path d="M12 54v4M52 54v4"/>',
    "canopy": '<path d="M32 6v6"/><path d="M12 48c0-17 8-30 20-36 12 6 20 19 20 36"/>'
              f'<path {_MESH} d="M22 48c0-14 4-26 10-36M42 48c0-14-4-26-10-36"/>'
              '<path d="M23 28l1.2 2.4 2.4 1.2-2.4 1.2L23 35l-1.2-2.4-2.4-1.2 2.4-1.2z" fill="currentColor" stroke-width="1"/>'
              '<path d="M41 22l1 2 2 1-2 1-1 2-1-2-2-1 2-1z" fill="currentColor" stroke-width="1"/>'
              '<path d="M38 36l.8 1.6 1.6.8-1.6.8-.8 1.6-.8-1.6-1.6-.8 1.6-.8z" fill="currentColor" stroke-width="1"/>'
              '<rect x="9" y="48" width="46" height="7" rx="2"/>',
    "cube": '<path d="M12 18 32 10l20 8v28l-20 8-20-8z"/><path d="M12 18l20 8 20-8M32 26v28"/>'
            f'<path {_MESH} d="M12 27l20 8 20-8M12 36l20 8 20-8M22 14v36M42 14v36"/>',
    "stroller": '<path d="M16 30a16 16 0 0 1 28-10L30 30z"/>'
                f'<path {_MESH} d="M20 24l10 6M25 18l5 12M32 15l-2 15"/>'
                '<path d="M12 30h36l-5 12H19z"/><path d="M48 30l5-10h5"/>'
                '<circle cx="21" cy="50" r="5"/><circle cx="41" cy="50" r="5"/>',
    "umbrella": '<path d="M8 22c5-9 13-13 24-13s19 4 24 13z"/><path d="M32 9v47"/>'
                f'<path {_MESH} d="M8 22l-1 34M56 22l1 34M18 22l-1 34M46 22l1 34M7 34h50M7 45h50"/>'
                '<path d="M4 57h56"/>',
    # Other layers
    "pump": '<rect x="21" y="26" width="22" height="31" rx="4"/><path d="M26 26v-6h12v6M31 20v-7h11l3 3"/>'
            '<path d="M49 13l6-3M49 17h7M49 21l6 3"/><path {m} d="M21 38h22"/>'.format(m=_MESH),
    "mist": '<rect x="22" y="24" width="20" height="33" rx="3"/><path d="M27 24v-8h10v8"/><path d="M32 16v-5h-9"/>'
            '<circle cx="16" cy="9" r="1.3" fill="currentColor"/><circle cx="11" cy="13" r="1.3" fill="currentColor"/>'
            '<circle cx="16" cy="15" r="1.3" fill="currentColor"/><circle cx="11" cy="7" r="1.3" fill="currentColor"/>'
            '<path {m} d="M22 40h20"/>'.format(m=_MESH),
    "shirt": '<path d="M22 12 10 18l4 10 7-3v29h22V25l7 3 4-10-12-6c-2 4-5 6-10 6s-8-2-10-6z"/>'
             '<circle cx="50" cy="40" r="1.3" fill="currentColor"/><circle cx="55" cy="45" r="1.3" fill="currentColor"/>'
             '<circle cx="50" cy="49" r="1.3" fill="currentColor"/><circle cx="56" cy="36" r="1.3" fill="currentColor"/>',
    "tube": '<path d="M19 10h26l-4 36H23z"/><path {m} d="M19 15h26"/>'
            '<rect x="27" y="46" width="10" height="9" rx="1.5"/><path d="M27 34h10"/>'.format(m=_MESH),
    "lotion": '<path d="M23 23h18v31a3 3 0 0 1-3 3H26a3 3 0 0 1-3-3z"/><path d="M27 23v-6h10v6M30 17v-5h4v5"/>'
              '<path d="M32 33c-3 4-4 6-4 8a4 4 0 0 0 8 0c0-2-1-4-4-8z"/>',
    # Layers and the risk card
    "shield": '<path d="M32 6 52 13v14c0 13-8 22-20 27C20 49 12 40 12 27V13z"/>'
              '<path d="m23 30 6 6 12-12"/>',
    "drop": '<path d="M32 8C24 20 18 28 18 37a14 14 0 0 0 28 0c0-9-6-17-14-29z"/>'
            '<path d="M26 39a6 6 0 0 0 6 6"/>',
    "mosquito": '<ellipse cx="27" cy="36" rx="13" ry="4.2" transform="rotate(-18 27 36)"/>'
                '<circle cx="43" cy="29" r="3.6"/><path d="M46 27.5l12-5"/>'
                '<path d="M30 31c-3-12 3-21 10-24-1 9-4 17-10 24z"/>'
                '<path d="M25 33c-10-6-13-15-11-22 7 4 11 12 11 22z"/>'
                '<path d="M30 39l-5 14M35 37l1 15M39 34l7 13M24 40l-11 9"/>',
}

PRODUCT_ART = {
    "Doorway Screen With Magnetic Closure": "door",
    "Pyramid Bed and Camping Net": "pyramid",
    "Glow-in-the-Dark Bed Canopy": "canopy",
    "Roomy Bed Netting Cube": "cube",
    "Baby and Stroller Netting": "stroller",
    "Outdoor Umbrella Enclosure": "umbrella",
    "20% Picaridin Repellent": "pump",
    "IR3535 Repellent Spray": "mist",
    "Permethrin Clothing Spray": "shirt",
    "1% Hydrocortisone Cream": "tube",
    "Calamine Lotion": "lotion",
}
LAYER_ART = ["shield", "pump", "drop"]


def svg(name, cls="fg-art"):
    return _OPEN.format(cls=cls) + DRAWINGS[name] + "</svg>"
