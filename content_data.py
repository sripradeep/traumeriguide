# -*- coding: utf-8 -*-
"""Structured content for the Traumeri Sedona guest guides."""

ICONS = {
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s-7-7.2-7-12a7 7 0 1 1 14 0c0 4.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.9 6.6 7.1.6-5.4 4.7 1.7 7-6.3-3.8L5.7 21l1.7-7-5.4-4.7 7.1-.6z"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "camera": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7l1.5-3h5L16 7"/><circle cx="12" cy="13.5" r="3.5"/></svg>',
}

# ---------------------------------------------------------------- DINING ----
DINING_INTRO = ("Sedona's dining scene punches well above its size — red-rock-view "
    "patios, chef-driven Latin and regional Mexican kitchens, and easy walkable cafes "
    "around West Sedona. Almost everything below is a 10-minute drive or less from the casitas.")
DINING_TIP = ("<b>Elote Cafe and Canyon Echo don't take phone reservations" 
    " far in advance</b> — Elote opens at 5pm and doesn't seat large parties without a wait, "
    "so arrive right at open or be ready to wait at the bar. For West Sedona walkable options, "
    "ChocolaTree and Vespa Cafe (both near Whole Foods) are a 5–10 minute walk from the casitas — "
    "no car needed.")
DINING = [
    {"name":"Mariposa Latin Inspired Grill","img":"https://upload.wikimedia.org/wikipedia/commons/f/fc/Ceviche_del_Per%C3%BA.jpg","tag":"Fine Dining · Latin American","time":"~5 min drive",
     "desc":"Chef Lisa Dahl's flagship room perched above the red rocks — Latin-inspired steaks, ceviche, and a sunset view that rivals the food. Reservations strongly recommended.",
     "tags":["Red Rock Views","Latin Cuisine","Reservations Recommended"]},
    {"name":"Elote Cafe","img":"https://upload.wikimedia.org/wikipedia/commons/c/cb/Elote_as%C3%A1ndose.jpg","tag":"Regional Mexican","time":"~5 min drive",
     "desc":"A Sedona institution serving inventive, deeply flavorful regional Mexican dishes (the smoked-pork elote is the namesake order). No reservations — arrive at 5pm open or expect a wait.",
     "tags":["Local Favorite","No Reservations","Bold Flavors"]},
    {"name":"Cress on Oak Creek","img":"https://upload.wikimedia.org/wikipedia/commons/f/fb/DZ6_2628_Cozy_candlelit_dinner_for_two_elegant_Thai_restaurant_setting_with_twinkling_lights_and_a_delicate_orchid_centerpiece.jpg","tag":"Fine Dining · Creekside","time":"~10 min drive",
     "desc":"L'Auberge de Sedona's creekside restaurant — candlelit tables right on Oak Creek, refined seasonal New American cooking, and one of the most romantic settings in town.","tags":["Creekside","Romantic","Upscale"]},
    {"name":"Canyon Echo","img":"https://upload.wikimedia.org/wikipedia/commons/6/6a/Fall_colors_in_Boynton_Canyon.jpg","tag":"New Southwest · Indigenous Ingredients","time":"~12 min drive",
     "desc":"At the base of Boynton Canyon, this is currently the hardest reservation in the Verde Valley — a menu built on tepary beans, prickly pear, and mesquite flour, with standouts like blue-corn-crusted trout and slow-roasted bison rib.","tags":["Book Ahead","Indigenous Ingredients","Boynton Canyon"]},
    {"name":"The Golden Goose","img":"https://upload.wikimedia.org/wikipedia/commons/0/04/Steak_at_restaurant_Vltava.jpg","tag":"Steak & Seafood","time":"~8 min drive",
     "desc":"A longtime local awards favorite — Best Steak, Best Seafood, Best Prime Rib, and Best Dessert in Sedona reader polls, in a cozy dining-room setting.","tags":["Local Awards","Steakhouse","Date Night"]},
    {"name":"Hideaway House","img":"https://upload.wikimedia.org/wikipedia/commons/6/65/Pork_tagliatelle_pasta_dish_at_restaurant_in_Rome%2C_Italy.jpg","tag":"Italian · Patio Views","time":"~9 min drive",
     "desc":"Italian comfort food on a patio overlooking Oak Creek — one of the best sunset-dinner views in Sedona, and a longtime favorite with locals.","tags":["Italian","Patio","Oak Creek Views"]},
    {"name":"Coffee Pot Restaurant","img":"https://upload.wikimedia.org/wikipedia/commons/b/be/Liat_Portal_for_Foodie_Disorder_-_Israeli_Breakfast_Plate_with_Herb_Omelet_Sandwich.jpg","tag":"Breakfast · Diner","time":"~6 min drive",
     "desc":"A Sedona breakfast legend sitting in the shadow of Coffee Pot Rock — the menu famously offers 101 different omelet combinations.","tags":["Breakfast","101 Omelets","Local Classic"]},
    {"name":"ChocolaTree Organic Eatery","img":"https://upload.wikimedia.org/wikipedia/commons/6/62/Tasty_Buddha_Bowl_with_Falafel_-_Dyke_Road_Park_Cafe_2025-05-09.jpg","tag":"Vegan & Vegetarian","time":"Walkable","desc":"A community-run vegan/vegetarian cafe with a big boho patio, counter service, and house-made chocolate. One of the few true walk-to spots from the casitas.","tags":["Walkable","Vegan","Outdoor Patio"]},
    {"name":"Vino di Sedona","img":"https://upload.wikimedia.org/wikipedia/commons/8/8d/Yerevan_Wine_Days_Tasting_Package.jpg","tag":"Wine Bar · Tapas","time":"~7 min drive",
     "desc":"Family-owned tasting room pouring from a list of nearly 1,000 bottles, with tapas-style small plates and live music on weekends.","tags":["Wine Bar","Live Music","Tapas"]},
    {"name":"Mesa Grill Sedona","img":"https://upload.wikimedia.org/wikipedia/commons/0/04/Burger_%2B_French_Fries%2C_Tamrah_Restaurant_%28Voi%29%2C_2025_%2801%29.jpg","tag":"American · Sunday Brunch","time":"~5 min drive",
     "desc":"A diverse, good-value menu — steak, burgers, seafood, salads — with great views and a popular Sunday brunch. Book a day ahead in season or be ready to wait for a walk-in table.","tags":["Sunday Brunch","Good Value","Family Friendly"]},
]

# ----------------------------------------------------------------- HIKES ----
HIKES_INTRO = ("From a flat half-mile stroll to a strenuous summit push, Sedona's trail "
    "system has something for every energy level — and several of the best trailheads are "
    "a 10–15 minute drive from the casitas. A $5 Red Rock Pass (or America the Beautiful pass) "
    "is required to park at most Forest Service trailheads.")
HIKES_TIP = ("<b>Start early.</b> Devil's Bridge, Cathedral Rock, and Soldier Pass fill their "
    "trailhead lots by 8–9am most of the year. Download the <b>AllTrails</b> app before you go for "
    "live difficulty ratings, water-crossing conditions, and closure alerts — and carry more water "
    "than you think you'll need; the high desert air is deceptively dry.")
HIKES = [
    {"name":"Devil's Bridge","img":"https://upload.wikimedia.org/wikipedia/commons/c/c3/Devil%27s_Bridge_Trail%2C_Sedona%2C_Arizona_-_panoramio_%2838%29.jpg","tag":"Easy–Moderate · 4.2 mi RT","time":"~12 min drive",
     "desc":"Sedona's most photographed trail — a natural sandstone arch you can walk out onto. Extremely popular; the rough access road needs high clearance or add 1.6 mi by parking at Dry Creek Vista.","tags":["Iconic","Crowded","High-Clearance Road"]},
    {"name":"Cathedral Rock Trail","img":"https://upload.wikimedia.org/wikipedia/commons/b/b0/Cathedral_Rock_-_Sedona_AZ-1.jpg","tag":"Moderate–Strenuous · 1.2 mi RT","time":"~10 min drive",
     "desc":"Short but steep, with hand-over-foot slickrock scrambling near the top — and one of the most rewarding 360° views in Sedona. Vortex site. Red Rock Pass required at Back O'Beyond trailhead.","tags":["Vortex Site","Scrambling","Big Views"]},
    {"name":"Bell Rock & Courthouse Butte Loop","img":"https://upload.wikimedia.org/wikipedia/commons/e/e6/Sedona_Arizona-27527-6.jpg","tag":"Easy–Moderate · 3.9 mi loop","time":"~15 min drive",
     "desc":"A mostly flat loop around two of Sedona's signature formations, with the option to scramble partway up Bell Rock itself. Family-friendly and a vortex site.","tags":["Vortex Site","Family Friendly","Flat Loop Option"]},
    {"name":"Boynton Canyon Trail","img":"https://upload.wikimedia.org/wikipedia/commons/6/6a/Fall_colors_in_Boynton_Canyon.jpg","tag":"Moderate · 6.1 mi RT","time":"~15 min drive",
     "desc":"A red-rock box canyon hike past the Kachina Woman formation, sacred to the Yavapai and Hopi. One of Sedona's four major vortex sites, with a peaceful, shaded second half.","tags":["Vortex Site","Sacred Site","Shaded"]},
    {"name":"West Fork Oak Creek Trail","img":"https://upload.wikimedia.org/wikipedia/commons/d/de/Man_Hiking_Along_The_West_Fork_Trail_In_Sedona_AZ.jpg","tag":"Easy · 6 mi RT","time":"~25 min drive",
     "desc":"Sedona's most beloved canyon walk — multiple creek crossings beneath towering cliff walls. Cool and shaded even in summer; a $12 day-use fee applies at the trailhead.","tags":["Shaded","Creek Crossings","Day-Use Fee"]},
    {"name":"Bear Mountain Trail","img":"https://upload.wikimedia.org/wikipedia/commons/9/96/Bear_Mountain%2C_Sedona%2C_Arizona_-_panoramio_%2845%29.jpg","tag":"Strenuous · 5 mi RT, 1,800 ft gain","time":"~18 min drive",
     "desc":"Steep switchbacks lead to sweeping summit views toward the San Francisco Peaks. One of the toughest — and most rewarding — day hikes in the area.","tags":["Strenuous","Summit Views","Switchbacks"]},
    {"name":"Soldier Pass Trail","img":"https://upload.wikimedia.org/wikipedia/commons/0/07/Devil%27s_Kitchen_Sedona.jpg","tag":"Moderate · 4.5 mi RT","time":"~10 min drive",
     "desc":"Passes the Seven Sacred Pools and the Devil's Kitchen sinkhole. Trailhead parking is extremely limited — the Soldier Pass trolley/shuttle is the easiest way in during busy season.","tags":["Sinkhole","Limited Parking","Shuttle Recommended"]},
    {"name":"Doe Mountain Trail","img":"https://upload.wikimedia.org/wikipedia/commons/1/10/Aerie_Trail%2C_Sedona%2C_Arizona_-_panoramio_%285%29.jpg","tag":"Moderate · ~1 mi to rim + mesa loop","time":"~14 min drive",
     "desc":"A short, lung-busting set of switchbacks opens onto a flat mesa-top loop with wide-open views — a quieter sunset alternative to the bigger-name trails.","tags":["Sunset Spot","Less Crowded","Mesa-Top Loop"]},
    {"name":"Airport Mesa Loop","img":"https://upload.wikimedia.org/wikipedia/commons/c/c5/Sedona_Arizona_1.jpg","tag":"Easy · 3.2 mi loop","time":"~8 min drive",
     "desc":"An easy loop trail right next to the Airport Mesa vortex and overlook — sweeping views with comparatively little elevation gain.","tags":["Vortex Site","Easy","Sunset Views"]},
    {"name":"Vultee Arch Trail","img":"https://upload.wikimedia.org/wikipedia/commons/e/ec/Sterling_Pass_Trail_To_Vultee_Arch_Trail%2C_Sedona%2C_Arizona%2C_Coconino_County_-_panoramio.jpg","tag":"Moderate · 3.6 mi RT","time":"~20 min drive (4WD road)",
     "desc":"A quieter alternative to Devil's Bridge — a natural sandstone arch reached via a shaded canyon trail off Sterling Pass Road. The access road requires a high-clearance vehicle.","tags":["Quiet Alternative","Natural Arch","4WD Access"]},
]

# ------------------------------------------------------------ SPIRITUAL ----
SPIRITUAL_INTRO = ("Long before Sedona became a New Age destination, the Yavapai and Hopi "
    "considered this red-rock landscape sacred, using it for healing, ceremony, and vision quests. "
    "Today the area is best known for its four vortex sites — places where many visitors report a "
    "noticeable shift in energy, mood, or clarity — along with a few quieter spots built for reflection.")
SPIRITUAL_TIP = ("<b>Vortex etiquette:</b> stay on marked trails, never remove rocks or build cairns, "
    "and skip the urge to light candles, burn sage, or leave offerings — these sites are sacred to "
    "Indigenous communities and the National Forest prohibits open flame and disturbing natural features. "
    "Sunrise and sunset are the quietest, most powerful times to visit any of the four vortexes.")
SPIRITUAL = [
    {"name":"Airport Mesa Vortex","img":"https://upload.wikimedia.org/wikipedia/commons/c/c5/Sedona_Arizona_1.jpg","tag":"Masculine Energy","time":"~8 min drive",
     "desc":"The most accessible of the four vortexes — a short walk from the parking area to an overlook said to carry strong, motivating, 'masculine' energy. Also Sedona's best sunset and stargazing spot.","tags":["Easy Access","Sunset","Stargazing"]},
    {"name":"Cathedral Rock Vortex","img":"https://upload.wikimedia.org/wikipedia/commons/a/af/Cathedral_Rock%2C_Sedona_%2846131198634%29.jpg","tag":"Feminine Energy","time":"~10 min drive",
     "desc":"Reached via a steep scramble partway up Cathedral Rock, this vortex is associated with nurturing, emotional-healing 'feminine' energy and some of the most photographed views in Arizona.","tags":["Emotional Healing","Scramble Required","Iconic Views"]},
    {"name":"Bell Rock Vortex","img":"https://upload.wikimedia.org/wikipedia/commons/e/e6/Sedona_Arizona-27527-6.jpg","tag":"Balanced Energy","time":"~15 min drive",
     "desc":"Considered both masculine and feminine in nature — a balanced site that's also the easiest vortex to reach, with a flat approach and the option to climb partway up the formation.","tags":["Balanced","Easiest Access","Family Friendly"]},
    {"name":"Boynton Canyon Vortex","img":"https://upload.wikimedia.org/wikipedia/commons/6/6a/Fall_colors_in_Boynton_Canyon.jpg","tag":"Harmonizing Energy","time":"~15 min drive",
     "desc":"A peaceful, balanced energy site inside a red-rock box canyon near the Kachina Woman formation — sacred to the Yavapai and Hopi, who used the canyon for ceremony.","tags":["Sacred Site","Peaceful","Shaded Canyon"]},
    {"name":"Chapel of the Holy Cross","img":"https://upload.wikimedia.org/wikipedia/commons/a/af/2021_Chapel_of_the_Holy_Cross_from_right_below.jpg","tag":"Interfaith Chapel","time":"~10 min drive",
     "desc":"A striking 1956 chapel built directly into a red-rock butte, open to all faiths. Free admission, open daily — many visitors describe a noticeable calm inside, vortex or not.","tags":["Free Entry","Architecture","Open Daily"]},
    {"name":"Amitabha Stupa & Peace Park","img":"https://upload.wikimedia.org/wikipedia/commons/0/0c/Amitabha_Chorten_in_Sedona_-_538813921.jpg","tag":"Buddhist Meditation Site","time":"~12 min drive",
     "desc":"A hillside Buddhist stupa and walking meditation trail tucked into a quiet residential canyon — prayer wheels, a labyrinth, and benches for sitting. Free, donation-based, open dawn to dusk.","tags":["Meditation","Free / Donation","Quiet"]},
]

# ----------------------------------------------------------------- POI -----
POI_INTRO = ("Beyond the trailheads, Sedona's red-rock setting holds state parks, ancient "
    "cliff dwellings, classic photo stops, and a couple of only-in-Sedona experiences worth "
    "building a day around.")
POI_TIP = ("<b>Slide Rock State Park</b> fills its parking lot by mid-morning in summer — go right "
    "at opening (8am) or after 4pm. <b>Palatki and Honanki Heritage Sites</b> require a free advance "
    "reservation through the Forest Service — book a few days ahead. If you're visiting Tuzigoot or "
    "Montezuma Castle too, an <b>America the Beautiful annual pass</b> ($80) pays for itself fast.")
POI = [
    {"name":"Red Rock State Park","img":"https://upload.wikimedia.org/wikipedia/commons/a/a3/Red_Rock_State_Park%2C_AZ.jpg","tag":"286-Acre Nature Preserve","time":"~15 min drive",
     "desc":"A quieter, less crowded park than the famous trailheads — five miles of interconnecting trails along Oak Creek, ranger-led programs, and excellent birding.","tags":["Nature Preserve","Ranger Programs","Oak Creek"]},
    {"name":"Slide Rock State Park","img":"https://upload.wikimedia.org/wikipedia/commons/b/bc/Slide_Rock%2C_Oak_Creek_Canyon%2C_AZ_9-15_%2821721214731%29.jpg","tag":"Natural Waterslide","time":"~25 min drive",
     "desc":"A natural rock waterslide in Oak Creek Canyon set in a historic apple orchard — Sedona's classic summer swimming hole. Arrives at capacity early on hot days.","tags":["Swimming","Historic Orchard","Summer Favorite"]},
    {"name":"Crescent Moon Picnic Site (Red Rock Crossing)","img":"https://upload.wikimedia.org/wikipedia/commons/b/b8/Crescent_Moon_Ranch_%28October_24%2C_2017%29_%2837926047431%29.jpg","tag":"Classic Photo Spot","time":"~12 min drive",
     "desc":"The postcard view of Cathedral Rock reflected in Oak Creek — shallow wading, shaded picnic areas, and arguably the most photographed angle in Sedona.","tags":["Photo Spot","Picnic Area","Wading"]},
    {"name":"Tlaquepaque Arts & Shopping Village","img":"https://upload.wikimedia.org/wikipedia/commons/5/55/Sedona_Tlaquepaque_%2836369258821%29.jpg","tag":"Arts Village","time":"~8 min drive",
     "desc":"A meticulously recreated Spanish-colonial village of courtyards and fountains, packed with 40+ galleries, boutiques, and restaurants. As much a sight to see as a place to shop.","tags":["Arts Village","Architecture","Dining"]},
    {"name":"Palatki & Honanki Heritage Sites","img":"https://upload.wikimedia.org/wikipedia/commons/5/5f/Palatki_doorway_Sedona_Arizona.jpg","tag":"Ancient Cliff Dwellings","time":"~25 min drive",
     "desc":"Sinagua cliff dwellings and some of the best-preserved rock art in the Southwest, tucked into red-rock alcoves. Free, advance reservation required through the Coconino National Forest.","tags":["Reservation Required","Rock Art","History"]},
    {"name":"Pink Jeep & Off-Road Tours","img":"https://upload.wikimedia.org/wikipedia/commons/3/36/Pink_Jeep_Sedona_4863.jpg","tag":"Signature Sedona Experience","time":"Depart Uptown",
     "desc":"The classic Sedona thrill ride — guided open-air Jeep tours bouncing over slickrock backroads to viewpoints most rental cars can't reach.","tags":["Guided Tour","Off-Road","Family Friendly"]},
    {"name":"Sunrise Hot Air Balloon Ride","img":"https://upload.wikimedia.org/wikipedia/commons/5/5e/Hot-air_balloon%2C_Wanderlust_Balloons%2C_Lake_Havasu_City%2C_Arizona%2C_USA.jpg","tag":"Sunrise Flight","time":"Pickup from Sedona",
     "desc":"Drift silently over the red rocks at sunrise — several local operators run dawn launches with champagne toasts on landing. Book a few days ahead, especially in spring and fall.","tags":["Sunrise","Bucket List","Book Ahead"]},
    {"name":"Tuzigoot National Monument","img":"https://upload.wikimedia.org/wikipedia/commons/e/e5/Tuzigoot_December_2013_1.JPG","tag":"Sinagua Pueblo Ruins","time":"~30 min drive",
     "desc":"A 1,000-year-old hilltop pueblo of 110 rooms overlooking the Verde River floodplain — one of the best-preserved prehistoric sites in the Southwest, easily paired with Jerome.","tags":["History","Easy Walk","Pairs with Jerome"]},
]

# --------------------------------------------------------- SCENIC DRIVES ---
DRIVES_INTRO = ("Some of Sedona's best scenery doesn't require leaving the car. These routes "
    "range from a quick 20-minute loop to a full half-day out-and-back, and several of the "
    "biggest views in Arizona are visible right from the pull-offs.")
DRIVES_TIP = ("<b>Schnebly Hill Road</b> requires a high-clearance (ideally 4WD) vehicle past the "
    "first mile or so — a standard sedan should turn around at the first overlook. For the easiest "
    "big payoff with zero off-roading, drive the <b>Red Rock Scenic Byway (SR-179)</b> at golden hour, "
    "when the rock formations turn deep red-orange.")
DRIVES = [
    {"name":"Red Rock Scenic Byway (SR-179)","img":"https://upload.wikimedia.org/wikipedia/commons/b/b2/Sedona_AZ_%288405081725%29.jpg","tag":"All-American Road · 7.5 mi","time":"South of town",
     "desc":"Arizona's only 'All-American Road' — a designation given to just a few dozen routes nationwide. Passes Bell Rock, Courthouse Butte, Cathedral Rock turnoffs, and the Chapel of the Holy Cross.","tags":["All-American Road","Easy Drive","Multiple Viewpoints"]},
    {"name":"Oak Creek Canyon (SR-89A North)","img":"https://upload.wikimedia.org/wikipedia/commons/a/ac/Oak_Creek_Canyon_02.jpg","tag":"Switchback Canyon Drive · 14 mi","time":"North of town",
     "desc":"A dramatic climb beneath towering canyon walls toward Flagstaff, with hairpin turns, creekside pull-offs, and the famous Oak Creek Vista overlook. Stunning in fall foliage season.","tags":["Fall Foliage","Switchbacks","Creekside Pull-offs"]},
    {"name":"Schnebly Hill Road","img":"https://upload.wikimedia.org/wikipedia/commons/6/64/Sedona_Arizona.jpg","tag":"High-Clearance 4WD Road","time":"Departs Uptown",
     "desc":"A rugged unpaved climb from Uptown Sedona up to Schnebly Hill Vista and Munds Mountain — one of the most sweeping panoramic overlooks in the region. High-clearance vehicle required.","tags":["4WD Required","Panoramic Overlook","Adventurous"]},
    {"name":"Dry Creek Road & Boynton Pass Loop","img":"https://upload.wikimedia.org/wikipedia/commons/b/ba/Dry_Creek_Road%2C_Sedona%2C_United_States_%28Unsplash%29.jpg","tag":"Backroad Loop","time":"West Sedona","desc":"A quieter back way to the Devil's Bridge and Boynton Canyon trailheads, winding past red-rock formations with a fraction of the SR-179 traffic.","tags":["Less Traffic","Trailhead Access","Red Rock Views"]},
    {"name":"Red Rock Loop Road","img":"https://upload.wikimedia.org/wikipedia/commons/1/1d/View_from_Red_Rock_Loop_road_%283879564434%29.jpg","tag":"8-Mile Loop","time":"West of Uptown",
     "desc":"A relaxed loop through high-desert neighborhoods and open red-rock country, passing the entrance to Red Rock State Park along the way.","tags":["Relaxed Pace","8 Miles","Passes State Park"]},
    {"name":"Jerome & Mingus Mountain Drive (SR-89A South)","img":"https://upload.wikimedia.org/wikipedia/commons/7/74/Jerome_Ghost_Town%2C_Arizona%2C_USA_-_2024_30.jpg","tag":"Mountain Switchbacks","time":"~40 min drive",
     "desc":"A climbing mountain road to the historic ghost-town-turned-arts-colony of Jerome at 5,000 ft, with wide Verde Valley overlooks on the way up.","tags":["Ghost Town","Mountain Overlooks","Day Trip"]},
]

# ------------------------------------------------------------- SHOPPING ----
SHOPPING_INTRO = ("From a Spanish-colonial arts village to crystal shops and Native American "
    "trading posts, Sedona's shopping leans art and craft over big-box — most of it concentrated "
    "in two walkable pockets, Uptown and Tlaquepaque.")
SHOPPING_TIP = ("<b>Parking in Uptown</b> fills up fast midday — the free lots at the south end near "
    "the Sedona Visitor Center are usually the easiest bet, and it's a short, scenic walk from there. "
    "Tlaquepaque has its own free parking lot just off SR-179.")
SHOPPING = [
    {"name":"Tlaquepaque Arts & Shopping Village","img":"https://upload.wikimedia.org/wikipedia/commons/9/9f/Sedona_Tlaquepaque_%2836369262001%29.jpg","tag":"40+ Galleries & Boutiques","time":"~8 min drive",
     "desc":"Sedona's signature shopping destination — a recreated Spanish-colonial village of cobbled courtyards and fountains, home to high-end art galleries, jewelry, and a working pottery studio.","tags":["Art Galleries","Architecture","Restaurants Onsite"]},
    {"name":"Uptown Sedona","img":"https://upload.wikimedia.org/wikipedia/commons/8/86/Deer_Gathering_in_Uptown%2C_Sedona%2C_Arizona.jpg","tag":"Historic Walkable District","time":"~10 min drive",
     "desc":"The original heart of town — Southwestern boutiques, jewelry, t-shirt shops, and several crystal stores lining a walkable strip with red-rock views at every turn.","tags":["Walkable","Souvenirs","Crystal Shops"]},
    {"name":"Sedona Crystal Vortex","img":"https://upload.wikimedia.org/wikipedia/commons/1/14/Quartz%2C_Tibet.jpg","tag":"Healing Crystals & Readings","time":"Uptown (3 locations)",
     "desc":"Sedona's best-known crystal shop, with three Uptown locations offering crystal jewelry, aura photography, and psychic readings alongside a huge raw-crystal selection.","tags":["Crystals","Aura Photos","Readings"]},
    {"name":"Hillside Sedona","img":"https://upload.wikimedia.org/wikipedia/commons/8/8f/Uptown%2C_Sedona%2C_AZ_7-30-13a_%289546440907%29.jpg","tag":"Open-Air Gallery Complex","time":"~9 min drive",
     "desc":"A multi-level open-air complex of galleries and boutiques just south of Tlaquepaque, with patio dining and some of the best red-rock views from any shopping center in town.","tags":["Galleries","Patio Dining","Red Rock Views"]},
    {"name":"Garland's Navajo Rugs","img":"https://upload.wikimedia.org/wikipedia/commons/2/24/RUG-WEAVING_AT_HUBBARD_TRADING_POST._THIS_WAS_THE_FIRST_SUCH_POST_ON_THE_NAVAJO_RESERVATION_-_NARA_-_544360.jpg","tag":"Native American Art","time":"~25 min drive (Oak Creek Canyon)",
     "desc":"One of the Southwest's most respected dealers of antique and contemporary Navajo rugs, set in a historic Oak Creek Canyon trading post — worth the drive even just to browse.","tags":["Navajo Rugs","Native American Art","Oak Creek Canyon"]},
    {"name":"Sedona Farmers Market","img":"https://upload.wikimedia.org/wikipedia/commons/f/f0/Farmer%27s_Market_Produce_%28Unsplash%29.jpg","tag":"Seasonal · Fridays","time":"Posse Grounds Park",
     "desc":"A seasonal Friday-morning market with local produce, baked goods, and handmade crafts — a relaxed way to spend an hour before a hike.","tags":["Seasonal","Local Produce","Friday Mornings"]},
]

# --------------------------------------------------------- GUEST TIPS ------
GUEST_TIPS = [
    {"h":"Getting Around","p":"A car is recommended for trailheads and day trips, though West Sedona (ChocolaTree, Vespa Cafe, Whole Foods) is genuinely walkable from the casitas. Download the AllTrails app before hiking for real-time conditions and closures."},
    {"h":"Red Rock Pass","p":"Most Forest Service trailheads (Devil's Bridge, Cathedral Rock, Bell Rock, Boynton Canyon, and more) require a $5 day pass or $15 weekly pass, sold at trailhead kiosks and local visitor centers. An America the Beautiful annual pass also works."},
    {"h":"Best Time to Visit","p":"March–May and September–November bring the most comfortable hiking temperatures. Summer days run hot (90s°F) but evenings cool off pleasantly at Sedona's ~4,500 ft elevation — start hikes by 7am in summer."},
    {"h":"Quiet Hours","p":"In line with City of Sedona ordinances, please keep noise to a minimum between 9:00 PM and 8:00 AM — both casitas sit in a residential compound shared with neighbors."},
    {"h":"Wildlife Note","p":"Javelina, coyotes, and the occasional rattlesnake are present in the area, especially around dusk — keep a respectful distance and keep pets leashed outdoors."},
    {"h":"Emergency Contacts","p":"Sedona Fire & Police (non-emergency): 928-282-3100 · Verde Valley Medical Center: 928-639-6000 · For anything property-related, email veedu.stays@gmail.com anytime."},
]

PROPERTY_RULES = [
    {"h":"Quiet Hours","p":"This is a friendly residential compound — please keep noise to a minimum between 9 PM and 8 AM out of respect for neighbors and the other Traumeri home onsite."},
    {"h":"Smoke-Free Home","p":"Both casitas are entirely smoke-free, indoors and out, including vaping. A cleaning fee applies for any violation."},
    {"h":"Pets","p":"Pets are welcome with prior approval and as noted on your booking — please keep pets supervised at all times and clean up after them."},
    {"h":"Breakages","p":"Accidents happen — if something breaks, just let your host know. Minor issues are rarely charged; for anything larger, the cost will always be agreed with you first."},
]

# ----------------------------------------------------------- PROPERTIES ----
ADDRESS = "1580 W State Route 89A, Lot 6 · Sedona, AZ 86336"
WIFI_NETWORK = "TraumeriWiFi"
WIFI_PASSWORD = "5edon@123"

CASITA = {
    "slug": "casita",
    "name": "Traumeri Casita",
    "title_word": "Hideaway",
    "tagline": "A cozy 1-bedroom casita with a private hot tub, steps from West Sedona's restaurants and trails.",
    "overview": ("Traumeri Casita is the smaller of two independent homes on a quiet, gated Sedona "
        "compound — a stylish 1-bedroom retreat built for couples, small families, or solo travelers who want "
        "to be walking distance from West Sedona's restaurants, coffee shops, and trailheads without giving up "
        "privacy. The queen bedroom (with a twin bunk above) and a comfortable sleeper sofa sleep up to 3 guests, "
        "and a private side patio holds a hot tub for five beneath open red-rock-and-mountain views."),
    "stats": [("Bedrooms","1"), ("Bathrooms","1"), ("Max Guests","3"),
              ("To Uptown Sedona","~10 min"), ("To Tlaquepaque","~8 min"), ("To Devil's Bridge","~12 min")],
    "checkin": "4:00 PM", "checkout": "11:00 AM",
    "entry": "Self check-in via smartlock — code sent ~24 hrs before arrival",
    "parking_spot": "3", "parking_note": "1 dedicated spot — Space #3. Please keep the open area between spots clear for the other home's guests.",
    "amenities": ["Private hot tub (seats 5)","Queen bed + twin bunk (upper bunk not for sleeping)",
        "Sleeper sofa & smart TV","Kitchenette with coffee nook","Front patio seating","Side patio dining area",
        "In-unit washer/dryer","High-speed WiFi","Free parking (1 spot)","Pet friendly (with approval)"],
    "rooms_note": "1 queen bed (with a twin bunk above — upper bunk not recommended for sleeping) plus a sleeper sofa in the living room.",
}

CASA = {
    "slug": "casa",
    "name": "Traumeri Casa",
    "title_word": "Retreat",
    "tagline": "A spacious 2-bedroom home with two patios, a hot tub, and a fireplace — sleeps up to 6.",
    "overview": ("Traumeri Casa is the larger of two independent homes on the same quiet Sedona compound — "
        "a fully remodeled 2-bedroom retreat with a king bedroom, a queen bedroom, and a sleeper sofa, "
        "comfortably sleeping up to six. The paved outdoor living area in the middle of the property anchors "
        "the stay: a hot tub, a fireplace, a BBQ grill, and a long dining table set against red rock and "
        "mountain views, with two dedicated parking spots just steps from the door."),
    "stats": [("Bedrooms","2"), ("Bathrooms","2"), ("Max Guests","6"),
              ("To Uptown Sedona","~10 min"), ("To Tlaquepaque","~8 min"), ("To Devil's Bridge","~12 min")],
    "checkin": "4:00 PM", "checkout": "11:00 AM",
    "entry": "Self check-in via smartlock — code sent ~24 hrs before arrival",
    "parking_spot": "1–2", "parking_note": "2 dedicated spots — Spaces #1 and #2. Please keep the open area between spots clear for the other home's guests.",
    "amenities": ["Private hot tub","Fireplace on the paved patio","BBQ grill","King bed + queen bed + sleeper sofa",
        "Fully remodeled kitchen with coffee nook","Dining seats up to 6","Front patio seating","In-unit washer/dryer",
        "High-speed WiFi","Free parking (2 spots)","Pet friendly (with approval)"],
    "rooms_note": "1 king bedroom, 1 queen bedroom, plus a sleeper sofa in the living room — comfortably sleeps up to 6.",
}
