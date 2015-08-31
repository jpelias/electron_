#!/usr/bin/env python
# list of words from http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Contemporary_poetry

#sudo apt-get install libwww-perl
#sudo apt-get install  libgmp3-dev
#sudo pip install gmpy


import os
from time import sleep
import sys, ecdsa, hashlib, binascii
from addrgen import addr_from_mpk
import random
import requests
import json


import urllib
import urllib2

TOKEN = '110309400:AAExG6jwuCUjJzeLzWqi4jmDhrEriDGT5fY'
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def reply(msg):
    
    resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
    'chat_id': '6660201' ,
    'text': msg.encode('utf-8'),
    'disable_web_page_preview': 'true',
    'reply_to_message_id': "" ,
    })).read()

    return



# secp256k1, http://www.oid-info.com/get/1.3.132.0.10
_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2FL
_r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141L
_b = 0x0000000000000000000000000000000000000000000000000000000000000007L
_a = 0x0000000000000000000000000000000000000000000000000000000000000000L
_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798L
_Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8L
curve_secp256k1 = ecdsa.ellipticcurve.CurveFp( _p, _a, _b )
generator_secp256k1 = ecdsa.ellipticcurve.Point( curve_secp256k1, _Gx, _Gy, _r )
oid_secp256k1 = (1,3,132,0,10)
SECP256k1 = ecdsa.curves.Curve("SECP256k1", curve_secp256k1, generator_secp256k1, oid_secp256k1 )

words = [
"like",
"just",
"love",
"know",
"never",
"want",
"time",
"out",
"there",
"make",
"look",
"eye",
"down",
"only",
"think",
"heart",
"back",
"then",
"into",
"about",
"more",
"away",
"still",
"them",
"take",
"thing",
"even",
"through",
"long",
"always",
"world",
"too",
"friend",
"tell",
"try",
"hand",
"thought",
"over",
"here",
"other",
"need",
"smile",
"again",
"much",
"cry",
"been",
"night",
"ever",
"little",
"said",
"end",
"some",
"those",
"around",
"mind",
"people",
"girl",
"leave",
"dream",
"left",
"turn",
"myself",
"give",
"nothing",
"really",
"off",
"before",
"something",
"find",
"walk",
"wish",
"good",
"once",
"place",
"ask",
"stop",
"keep",
"watch",
"seem",
"everything",
"wait",
"got",
"yet",
"made",
"remember",
"start",
"alone",
"run",
"hope",
"maybe",
"believe",
"body",
"hate",
"after",
"close",
"talk",
"stand",
"own",
"each",
"hurt",
"help",
"home",
"god",
"soul",
"new",
"many",
"two",
"inside",
"should",
"true",
"first",
"fear",
"mean",
"better",
"play",
"another",
"gone",
"change",
"use",
"wonder",
"someone",
"hair",
"cold",
"open",
"best",
"any",
"behind",
"happen",
"water",
"dark",
"laugh",
"stay",
"forever",
"name",
"work",
"show",
"sky",
"break",
"came",
"deep",
"door",
"put",
"black",
"together",
"upon",
"happy",
"such",
"great",
"white",
"matter",
"fill",
"past",
"please",
"burn",
"cause",
"enough",
"touch",
"moment",
"soon",
"voice",
"scream",
"anything",
"stare",
"sound",
"red",
"everyone",
"hide",
"kiss",
"truth",
"death",
"beautiful",
"mine",
"blood",
"broken",
"very",
"pass",
"next",
"forget",
"tree",
"wrong",
"air",
"mother",
"understand",
"lip",
"hit",
"wall",
"memory",
"sleep",
"free",
"high",
"realize",
"school",
"might",
"skin",
"sweet",
"perfect",
"blue",
"kill",
"breath",
"dance",
"against",
"fly",
"between",
"grow",
"strong",
"under",
"listen",
"bring",
"sometimes",
"speak",
"pull",
"person",
"become",
"family",
"begin",
"ground",
"real",
"small",
"father",
"sure",
"feet",
"rest",
"young",
"finally",
"land",
"across",
"today",
"different",
"guy",
"line",
"fire",
"reason",
"reach",
"second",
"slowly",
"write",
"eat",
"smell",
"mouth",
"step",
"learn",
"three",
"floor",
"promise",
"breathe",
"darkness",
"push",
"earth",
"guess",
"save",
"song",
"above",
"along",
"both",
"color",
"house",
"almost",
"sorry",
"anymore",
"brother",
"okay",
"dear",
"game",
"fade",
"already",
"apart",
"warm",
"beauty",
"heard",
"notice",
"question",
"shine",
"began",
"piece",
"whole",
"shadow",
"secret",
"street",
"within",
"finger",
"point",
"morning",
"whisper",
"child",
"moon",
"green",
"story",
"glass",
"kid",
"silence",
"since",
"soft",
"yourself",
"empty",
"shall",
"angel",
"answer",
"baby",
"bright",
"dad",
"path",
"worry",
"hour",
"drop",
"follow",
"power",
"war",
"half",
"flow",
"heaven",
"act",
"chance",
"fact",
"least",
"tired",
"children",
"near",
"quite",
"afraid",
"rise",
"sea",
"taste",
"window",
"cover",
"nice",
"trust",
"lot",
"sad",
"cool",
"force",
"peace",
"return",
"blind",
"easy",
"ready",
"roll",
"rose",
"drive",
"held",
"music",
"beneath",
"hang",
"mom",
"paint",
"emotion",
"quiet",
"clear",
"cloud",
"few",
"pretty",
"bird",
"outside",
"paper",
"picture",
"front",
"rock",
"simple",
"anyone",
"meant",
"reality",
"road",
"sense",
"waste",
"bit",
"leaf",
"thank",
"happiness",
"meet",
"men",
"smoke",
"truly",
"decide",
"self",
"age",
"book",
"form",
"alive",
"carry",
"escape",
"damn",
"instead",
"able",
"ice",
"minute",
"throw",
"catch",
"leg",
"ring",
"course",
"goodbye",
"lead",
"poem",
"sick",
"corner",
"desire",
"known",
"problem",
"remind",
"shoulder",
"suppose",
"toward",
"wave",
"drink",
"jump",
"woman",
"pretend",
"sister",
"week",
"human",
"joy",
"crack",
"grey",
"pray",
"surprise",
"dry",
"knee",
"less",
"search",
"bleed",
"caught",
"clean",
"embrace",
"future",
"king",
"son",
"sorrow",
"chest",
"hug",
"remain",
"sat",
"worth",
"blow",
"daddy",
"final",
"parent",
"tight",
"also",
"create",
"lonely",
"safe",
"cross",
"dress",
"evil",
"silent",
"bone",
"fate",
"perhaps",
"anger",
"class",
"scar",
"snow",
"tiny",
"tonight",
"continue",
"control",
"dog",
"edge",
"mirror",
"month",
"suddenly",
"comfort",
"given",
"loud",
"quickly",
"gaze",
"plan",
"rush",
"stone",
"town",
"battle",
"ignore",
"spirit",
"stood",
"stupid",
"yours",
"brown",
"build",
"dust",
"hey",
"kept",
"pay",
"phone",
"twist",
"although",
"ball",
"beyond",
"hidden",
"nose",
"taken",
"fail",
"float",
"pure",
"somehow",
"wash",
"wrap",
"angry",
"cheek",
"creature",
"forgotten",
"heat",
"rip",
"single",
"space",
"special",
"weak",
"whatever",
"yell",
"anyway",
"blame",
"job",
"choose",
"country",
"curse",
"drift",
"echo",
"figure",
"grew",
"laughter",
"neck",
"suffer",
"worse",
"yeah",
"disappear",
"foot",
"forward",
"knife",
"mess",
"somewhere",
"stomach",
"storm",
"beg",
"idea",
"lift",
"offer",
"breeze",
"field",
"five",
"often",
"simply",
"stuck",
"win",
"allow",
"confuse",
"enjoy",
"except",
"flower",
"seek",
"strength",
"calm",
"grin",
"gun",
"heavy",
"hill",
"large",
"ocean",
"shoe",
"sigh",
"straight",
"summer",
"tongue",
"accept",
"crazy",
"everyday",
"exist",
"grass",
"mistake",
"sent",
"shut",
"surround",
"table",
"ache",
"brain",
"destroy",
"heal",
"nature",
"shout",
"sign",
"stain",
"choice",
"doubt",
"glance",
"glow",
"mountain",
"queen",
"stranger",
"throat",
"tomorrow",
"city",
"either",
"fish",
"flame",
"rather",
"shape",
"spin",
"spread",
"ash",
"distance",
"finish",
"image",
"imagine",
"important",
"nobody",
"shatter",
"warmth",
"became",
"feed",
"flesh",
"funny",
"lust",
"shirt",
"trouble",
"yellow",
"attention",
"bare",
"bite",
"money",
"protect",
"amaze",
"appear",
"born",
"choke",
"completely",
"daughter",
"fresh",
"friendship",
"gentle",
"probably",
"six",
"deserve",
"expect",
"grab",
"middle",
"nightmare",
"river",
"thousand",
"weight",
"worst",
"wound",
"barely",
"bottle",
"cream",
"regret",
"relationship",
"stick",
"test",
"crush",
"endless",
"fault",
"itself",
"rule",
"spill",
"art",
"circle",
"join",
"kick",
"mask",
"master",
"passion",
"quick",
"raise",
"smooth",
"unless",
"wander",
"actually",
"broke",
"chair",
"deal",
"favorite",
"gift",
"note",
"number",
"sweat",
"box",
"chill",
"clothes",
"lady",
"mark",
"park",
"poor",
"sadness",
"tie",
"animal",
"belong",
"brush",
"consume",
"dawn",
"forest",
"innocent",
"pen",
"pride",
"stream",
"thick",
"clay",
"complete",
"count",
"draw",
"faith",
"press",
"silver",
"struggle",
"surface",
"taught",
"teach",
"wet",
"bless",
"chase",
"climb",
"enter",
"letter",
"melt",
"metal",
"movie",
"stretch",
"swing",
"vision",
"wife",
"beside",
"crash",
"forgot",
"guide",
"haunt",
"joke",
"knock",
"plant",
"pour",
"prove",
"reveal",
"steal",
"stuff",
"trip",
"wood",
"wrist",
"bother",
"bottom",
"crawl",
"crowd",
"fix",
"forgive",
"frown",
"grace",
"loose",
"lucky",
"party",
"release",
"surely",
"survive",
"teacher",
"gently",
"grip",
"speed",
"suicide",
"travel",
"treat",
"vein",
"written",
"cage",
"chain",
"conversation",
"date",
"enemy",
"however",
"interest",
"million",
"page",
"pink",
"proud",
"sway",
"themselves",
"winter",
"church",
"cruel",
"cup",
"demon",
"experience",
"freedom",
"pair",
"pop",
"purpose",
"respect",
"shoot",
"softly",
"state",
"strange",
"bar",
"birth",
"curl",
"dirt",
"excuse",
"lord",
"lovely",
"monster",
"order",
"pack",
"pants",
"pool",
"scene",
"seven",
"shame",
"slide",
"ugly",
"among",
"blade",
"blonde",
"closet",
"creek",
"deny",
"drug",
"eternity",
"gain",
"grade",
"handle",
"key",
"linger",
"pale",
"prepare",
"swallow",
"swim",
"tremble",
"wheel",
"won",
"cast",
"cigarette",
"claim",
"college",
"direction",
"dirty",
"gather",
"ghost",
"hundred",
"loss",
"lung",
"orange",
"present",
"swear",
"swirl",
"twice",
"wild",
"bitter",
"blanket",
"doctor",
"everywhere",
"flash",
"grown",
"knowledge",
"numb",
"pressure",
"radio",
"repeat",
"ruin",
"spend",
"unknown",
"buy",
"clock",
"devil",
"early",
"false",
"fantasy",
"pound",
"precious",
"refuse",
"sheet",
"teeth",
"welcome",
"add",
"ahead",
"block",
"bury",
"caress",
"content",
"depth",
"despite",
"distant",
"marry",
"purple",
"threw",
"whenever",
"bomb",
"dull",
"easily",
"grasp",
"hospital",
"innocence",
"normal",
"receive",
"reply",
"rhyme",
"shade",
"someday",
"sword",
"toe",
"visit",
"asleep",
"bought",
"center",
"consider",
"flat",
"hero",
"history",
"ink",
"insane",
"muscle",
"mystery",
"pocket",
"reflection",
"shove",
"silently",
"smart",
"soldier",
"spot",
"stress",
"train",
"type",
"view",
"whether",
"bus",
"energy",
"explain",
"holy",
"hunger",
"inch",
"magic",
"mix",
"noise",
"nowhere",
"prayer",
"presence",
"shock",
"snap",
"spider",
"study",
"thunder",
"trail",
"admit",
"agree",
"bag",
"bang",
"bound",
"butterfly",
"cute",
"exactly",
"explode",
"familiar",
"fold",
"further",
"pierce",
"reflect",
"scent",
"selfish",
"sharp",
"sink",
"spring",
"stumble",
"universe",
"weep",
"women",
"wonderful",
"action",
"ancient",
"attempt",
"avoid",
"birthday",
"branch",
"chocolate",
"core",
"depress",
"drunk",
"especially",
"focus",
"fruit",
"honest",
"match",
"palm",
"perfectly",
"pillow",
"pity",
"poison",
"roar",
"shift",
"slightly",
"thump",
"truck",
"tune",
"twenty",
"unable",
"wipe",
"wrote",
"coat",
"constant",
"dinner",
"drove",
"egg",
"eternal",
"flight",
"flood",
"frame",
"freak",
"gasp",
"glad",
"hollow",
"motion",
"peer",
"plastic",
"root",
"screen",
"season",
"sting",
"strike",
"team",
"unlike",
"victim",
"volume",
"warn",
"weird",
"attack",
"await",
"awake",
"built",
"charm",
"crave",
"despair",
"fought",
"grant",
"grief",
"horse",
"limit",
"message",
"ripple",
"sanity",
"scatter",
"serve",
"split",
"string",
"trick",
"annoy",
"blur",
"boat",
"brave",
"clearly",
"cling",
"connect",
"fist",
"forth",
"imagination",
"iron",
"jock",
"judge",
"lesson",
"milk",
"misery",
"nail",
"naked",
"ourselves",
"poet",
"possible",
"princess",
"sail",
"size",
"snake",
"society",
"stroke",
"torture",
"toss",
"trace",
"wise",
"bloom",
"bullet",
"cell",
"check",
"cost",
"darling",
"during",
"footstep",
"fragile",
"hallway",
"hardly",
"horizon",
"invisible",
"journey",
"midnight",
"mud",
"nod",
"pause",
"relax",
"shiver",
"sudden",
"value",
"youth",
"abuse",
"admire",
"blink",
"breast",
"bruise",
"constantly",
"couple",
"creep",
"curve",
"difference",
"dumb",
"emptiness",
"gotta",
"honor",
"plain",
"planet",
"recall",
"rub",
"ship",
"slam",
"soar",
"somebody",
"tightly",
"weather",
"adore",
"approach",
"bond",
"bread",
"burst",
"candle",
"coffee",
"cousin",
"crime",
"desert",
"flutter",
"frozen",
"grand",
"heel",
"hello",
"language",
"level",
"movement",
"pleasure",
"powerful",
"random",
"rhythm",
"settle",
"silly",
"slap",
"sort",
"spoken",
"steel",
"threaten",
"tumble",
"upset",
"aside",
"awkward",
"bee",
"blank",
"board",
"button",
"card",
"carefully",
"complain",
"crap",
"deeply",
"discover",
"drag",
"dread",
"effort",
"entire",
"fairy",
"giant",
"gotten",
"greet",
"illusion",
"jeans",
"leap",
"liquid",
"march",
"mend",
"nervous",
"nine",
"replace",
"rope",
"spine",
"stole",
"terror",
"accident",
"apple",
"balance",
"boom",
"childhood",
"collect",
"demand",
"depression",
"eventually",
"faint",
"glare",
"goal",
"group",
"honey",
"kitchen",
"laid",
"limb",
"machine",
"mere",
"mold",
"murder",
"nerve",
"painful",
"poetry",
"prince",
"rabbit",
"shelter",
"shore",
"shower",
"soothe",
"stair",
"steady",
"sunlight",
"tangle",
"tease",
"treasure",
"uncle",
"begun",
"bliss",
"canvas",
"cheer",
"claw",
"clutch",
"commit",
"crimson",
"crystal",
"delight",
"doll",
"existence",
"express",
"fog",
"football",
"gay",
"goose",
"guard",
"hatred",
"illuminate",
"mass",
"math",
"mourn",
"rich",
"rough",
"skip",
"stir",
"student",
"style",
"support",
"thorn",
"tough",
"yard",
"yearn",
"yesterday",
"advice",
"appreciate",
"autumn",
"bank",
"beam",
"bowl",
"capture",
"carve",
"collapse",
"confusion",
"creation",
"dove",
"feather",
"girlfriend",
"glory",
"government",
"harsh",
"hop",
"inner",
"loser",
"moonlight",
"neighbor",
"neither",
"peach",
"pig",
"praise",
"screw",
"shield",
"shimmer",
"sneak",
"stab",
"subject",
"throughout",
"thrown",
"tower",
"twirl",
"wow",
"army",
"arrive",
"bathroom",
"bump",
"cease",
"cookie",
"couch",
"courage",
"dim",
"guilt",
"howl",
"hum",
"husband",
"insult",
"led",
"lunch",
"mock",
"mostly",
"natural",
"nearly",
"needle",
"nerd",
"peaceful",
"perfection",
"pile",
"price",
"remove",
"roam",
"sanctuary",
"serious",
"shiny",
"shook",
"sob",
"stolen",
"tap",
"vain",
"void",
"warrior",
"wrinkle",
"affection",
"apologize",
"blossom",
"bounce",
"bridge",
"cheap",
"crumble",
"decision",
"descend",
"desperately",
"dig",
"dot",
"flip",
"frighten",
"heartbeat",
"huge",
"lazy",
"lick",
"odd",
"opinion",
"process",
"puzzle",
"quietly",
"retreat",
"score",
"sentence",
"separate",
"situation",
"skill",
"soak",
"square",
"stray",
"taint",
"task",
"tide",
"underneath",
"veil",
"whistle",
"anywhere",
"bedroom",
"bid",
"bloody",
"burden",
"careful",
"compare",
"concern",
"curtain",
"decay",
"defeat",
"describe",
"double",
"dreamer",
"driver",
"dwell",
"evening",
"flare",
"flicker",
"grandma",
"guitar",
"harm",
"horrible",
"hungry",
"indeed",
"lace",
"melody",
"monkey",
"nation",
"object",
"obviously",
"rainbow",
"salt",
"scratch",
"shown",
"shy",
"stage",
"stun",
"third",
"tickle",
"useless",
"weakness",
"worship",
"worthless",
"afternoon",
"beard",
"boyfriend",
"bubble",
"busy",
"certain",
"chin",
"concrete",
"desk",
"diamond",
"doom",
"drawn",
"due",
"felicity",
"freeze",
"frost",
"garden",
"glide",
"harmony",
"hopefully",
"hunt",
"jealous",
"lightning",
"mama",
"mercy",
"peel",
"physical",
"position",
"pulse",
"punch",
"quit",
"rant",
"respond",
"salty",
"sane",
"satisfy",
"savior",
"sheep",
"slept",
"social",
"sport",
"tuck",
"utter",
"valley",
"wolf",
"aim",
"alas",
"alter",
"arrow",
"awaken",
"beaten",
"belief",
"brand",
"ceiling",
"cheese",
"clue",
"confidence",
"connection",
"daily",
"disguise",
"eager",
"erase",
"essence",
"everytime",
"expression",
"fan",
"flag",
"flirt",
"foul",
"fur",
"giggle",
"glorious",
"ignorance",
"law",
"lifeless",
"measure",
"mighty",
"muse",
"north",
"opposite",
"paradise",
"patience",
"patient",
"pencil",
"petal",
"plate",
"ponder",
"possibly",
"practice",
"slice",
"spell",
"stock",
"strife",
"strip",
"suffocate",
"suit",
"tender",
"tool",
"trade",
"velvet",
"verse",
"waist",
"witch",
"aunt",
"bench",
"bold",
"cap",
"certainly",
"click",
"companion",
"creator",
"dart",
"delicate",
"determine",
"dish",
"dragon",
"drama",
"drum",
"dude",
"everybody",
"feast",
"forehead",
"former",
"fright",
"fully",
"gas",
"hook",
"hurl",
"invite",
"juice",
"manage",
"moral",
"possess",
"raw",
"rebel",
"royal",
"scale",
"scary",
"several",
"slight",
"stubborn",
"swell",
"talent",
"tea",
"terrible",
"thread",
"torment",
"trickle",
"usually",
"vast",
"violence",
"weave",
"acid",
"agony",
"ashamed",
"awe",
"belly",
"blend",
"blush",
"character",
"cheat",
"common",
"company",
"coward",
"creak",
"danger",
"deadly",
"defense",
"define",
"depend",
"desperate",
"destination",
"dew",
"duck",
"dusty",
"embarrass",
"engine",
"example",
"explore",
"foe",
"freely",
"frustrate",
"generation",
"glove",
"guilty",
"health",
"hurry",
"idiot",
"impossible",
"inhale",
"jaw",
"kingdom",
"mention",
"mist",
"moan",
"mumble",
"mutter",
"observe",
"ode",
"pathetic",
"pattern",
"pie",
"prefer",
"puff",
"rape",
"rare",
"revenge",
"rude",
"scrape",
"spiral",
"squeeze",
"strain",
"sunset",
"suspend",
"sympathy",
"thigh",
"throne",
"total",
"unseen",
"weapon",
"weary"
]



n = 1626

# Note about US patent no 5892470: Here each word does not represent a given digit.
# Instead, the digit represented by a word is variable, it depends on the previous word.

def mn_encode( message ):
    out = []
    for i in range(len(message)/8):
        word = message[8*i:8*i+8]
        x = int(word, 16)
        w1 = (x%n)
        w2 = ((x/n) + w1)%n
        w3 = ((x/n/n) + w2)%n
        out += [ words[w1], words[w2], words[w3] ]
    return out

def mn_decode( wlist ):
    out = ''
    for i in range(len(wlist)/3):
        word1, word2, word3 = wlist[3*i:3*i+3]
        w1 =  words.index(word1)
        w2 = (words.index(word2))%n
        w3 = (words.index(word3))%n
        x = w1 +n*((w2-w1)%n) +n*n*((w3-w2)%n)
        out += '%08x'%x
    return out

def public_key_to_address(public_key):
    md = hashlib.new('ripemd160')
    md.update(hashlib.sha256( public_key ).digest())
    vh160 = chr(0) + md.digest()
    h = hashlib.sha256(hashlib.sha256( vh160 ).digest()).digest()
    addr = vh160 + h[0:4]

    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    long_value = 0L
    for (i, c) in enumerate(addr[::-1]):
        long_value += (256**i) * ord(c)

    result = ''
    while long_value >= 58:
        div, mod = divmod(long_value, 58)
        result = alphabet[mod] + result
        long_value = div
    result = alphabet[long_value] + result

    nPad = 0
    for c in addr:
        if c == '\0': nPad += 1
        else: break

    return (alphabet[0]*nPad) + result




for joder in range(10000):

    acumulado = 0
    palabras = ""
    frase = ['','','','','','','','','','','','']

    for i in range(12):

        palabras = random.sample(words,1)
        frase[i] = ''.join(palabras)


    #print ' '.join(frase)
    #print frase
    semilla = mn_decode(frase)

#print mn_encode('f90e7d9fb490955f2d9483fd44d8b9f7')

    #print semilla

    for seed in range(1):
        oldseed = seed = semilla
        for i in range(100000):
            seed = hashlib.sha256(seed + oldseed).digest()
        master_private_key = ecdsa.SigningKey.from_secret_exponent( ecdsa.util.string_to_number( seed ), curve = SECP256k1 )
        mpk = master_private_key.get_verifying_key().to_string().encode('hex')


    seq = 0
    for_change = 0
    mpk = mpk.decode('hex')

    for seq in range(10):

        z = ecdsa.util.string_to_number( hashlib.sha256(hashlib.sha256( "%d:%d:" % (seq,for_change) + mpk ).digest()).digest() )
        master_public_key = ecdsa.VerifyingKey.from_string( mpk, curve = SECP256k1 )
        public_key = ecdsa.VerifyingKey.from_public_point( master_public_key.pubkey.point + z*SECP256k1.generator, curve = SECP256k1 )

        direccion = public_key_to_address( '04'.decode('hex') + public_key.to_string() )


        #direccion = "12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"

        # cantidad = os.popen("GET https://blockchain.info/es/q/addressbalance/" + direccion).read()

        url = "https://block.io/api/v2/get_address_balance/?api_key=0908-42b6-3792-14b9&addresses=" + direccion

        #url = "https://bitcoin.toshi.io/api/v0/addresses/" + direccion

        headers = {'Content-Type': 'application/json',
           'Accept-Encoding': 'gzip, deflate' ,
           'User-Agent': 'Ninguno' ,
           'Connection': 'keep-alive'}

        cantidad = 0

        r = requests.get(url,headers=headers)

        if r.status_code == 200:

            data=r.json()

            #print data

            cantidad = (float (data['data']['available_balance']))

            #print cantidad available_balance

        #print direccion,cantidad

        #amount = float (cantidad)

        #print direccion, amount
        acumulado = acumulado + cantidad


    #print semilla  , acumulado
    
    
    print '.'
    
    if acumulado >0:
        reply (semilla +"   " +str(acumulado))
        
        
        
    
    
    #sleep (4)

