//Collection of verbs, nouns, and adverbs to feed to the game prompt.
var verbs = ["improve", "warn", "remove", "suspect,", "comb", "grab", "applaud", "wave,", "meddle", "whirl", "harass",
    "employ,", "connect", "tie", "wipe", "float,", "drop", "handle", "clip", "itch,", "spill", "allow", "scrub", "record", "taste", "wash", "excuse", "judge,", "ruin", "explode", "jog", "flash,", "press", "boast", "apologise", "discover", "terrify", "rock", "stroke", "observe,", "deceive", "suppose", "lighten", "advise,", "back", "wander", "weigh",
    "invite,", "shop", "grate", "permit", "signal,", "tug", "laugh", "brush", "bury,", "guard", "strengthen", "license", "slow,", "peel", "bless", "doubt", "bubble,", "trap", "fire", "trot", "paste,", "agree", "pour", "memorise",
    "happen,", "manage", "arrange", "bolt", "poke,", "object", "talk", "reflect", "inject,", "reach", "guide", "admit",
    "lick,", "long", "strip", "soothe", "repair,", "clean", "shelter", "settle", "knot,", "command", "sigh",
    "concentrate", "damage,", "pretend", "list", "fail", "depend"];
var nouns = ["woods", "moment", "marriage", "item", "golf", "malice", "prison", "outcome", "butter", "dust", "chin",
    "chair", "maiden", "demon", "corner", "sultan", "series", "opinion", "domicile", "salad", "banner", "avenue",
    "labyrinth", "village", "timepiece", "assault", "bagpipe", "reflex", "rating", "arbiter", "cobblestone",
    "kindness", "crime", "opportunity", "thicket", "alcohol", "democracy", "disease", "square", "guardhouse",
    "person", "attendant", "dirt", "sulphur", "meeting", "speakeasy", "sugar", "ocean", "bronze", "freedom",
    "physician", "cuisine", "nephew", "habitation", "whale", "kerchief", "hoof", "abyss", "wench", "exertion",
    "effort", "jealousy", "fire", "contribution", "python", "life", "material", "circle", "skillet", "board",
    "prairie", "salary", "shadow", "ensemble", "essence", "hindrance", "flower", "cat", "dawn", "northwest", "gift",
    "tomahawk", "gem", "window", "festivity", "concept", "discipline", "rock", "hint", "flood", "brain", "revolver", "bottle", "fact", "shotgun", "cradle", "impropriety", "admiral", "emporium", "speaker"];
var adverbs = ["tediously", "immediately", "hopefully", "essentially", "tremendously", "frankly", "kookily",
    "frequently", "always", "violently", "likely", "upside-down", "neatly", "freely", "lightly", "lazily",
    "triumphantly", "easily", "roughly", "openly", "silently", "also", "scarily", "nervously", "never",
    "speedily", "mainly", "technically", "worriedly", "clearly", "loosely", "courageously", "quietly", "limply",
    "quarrelsomely", "knowledgeably", "strictly", "awkwardly", "unaccountably", "valiantly", "generally",
    "yearningly", "nicely", "sleepily", "normally", "thus", "carefully", "kiddingly", "carelessly", "instantly",
    "helpfully", "famously", "actually", "devotedly", "dramatically", "recklessly", "madly", "stealthily",
    "sheepishly", "coyly", "constantly", "joyously", "eagerly", "sadly", "successfully", "foolishly", "noisily",
    "unabashedly", "yearly", "defiantly", "regularly", "ultimately", "simply", "daily", "promptly", "beautifully", "lovingly", "vainly", "keenly", "woefully", "faithfully", "probably", "", "adventurously", "strongly",
    "already", "tightly", "", "unnaturally", "knavishly", "deceivingly", "seriously", "", "specifically",
    "upbeat", "powerfully", "softly", "", "effectively", "smoothly", "yawningly", "far", "", "heavily", "solemnly"];

//Coding for home screen.
var homeScreen = function () {
    background(115, 113, 113);
    textSize(80);
    textLeading(68);
    fill(0, 0, 0);
    textAlign(RIGHT, BASELINE);
    text("THINGS\nDRAWN\nTERRIBLY", 12, 4, 388, 400);

    //Makes the two buttons at the bottom. 
    textSize(20);
    stroke(0, 0, 0);
    strokeWeight(3);
    noFill();
    rect(212, 340, 150, 50);
    noStroke();
    text("Draw", 308, 373);

    stroke(0, 0, 0);
    strokeWeight(3);
    rect(33, 340, 150, 50);
    noStroke();
    fill(0, 0, 0);

    text("Instructions", 155, 373);
    noFill();
};
//Coding for rules screen. 
var rulesScreen = function () {
    fill(0, 0, 0);
    background(115, 113, 113);
    textSize(60);
    textLeading(48);
    textAlign(RIGHT, BASELINE);
    text("RULES\nTYPED\nROUGHLY", 12, 4, 388, 400);

    textSize(20);
    stroke(0, 0, 0);
    strokeWeight(3);
    noFill();
    rect(212, 340, 150, 50);
    noStroke();
    text("Draw", 308, 373);

    stroke(0, 0, 0);
    strokeWeight(3);
    rect(33, 340, 150, 50);
    noStroke();
    fill(0, 0, 0);

    text("Home", 137, 373);
    textAlign(CENTER);
    text("The goal of the game is to draw the given prompt using only the randomly 4 colors generated in the bottom left corner. To change colors, just click on the color. The prompt changes each time the game is restarted.", 0, 200, 400, 142);
    noFill();

};

var paintColors = [];
var paintSpace = [];

var gameScreen = function () {
    background(255, 255, 255);

    noStroke();
    fill(92, 92, 92);
    rect(0, 341, 404, 65);
    fill(255, 0, 0);

    //Generates the 4 colored squares. 
    for (var i = 5; i < 50; i += 25) { //Sets the x position of the 2 squares. Could be expanded for more colors.
        for (var j = 345; j < 390; j += 25) { //Sets the y position. 
            var r = round(random(0, 255)); //Generates random r, g, b, values for the colors. 
            var g = round(random(0, 255));
            var b = round(random(0, 255));
            paintColors.push([r, g, b]); //Creates an array with the 4 colors.
            paintSpace.push([i, j]); //Creates an array with the location of each color. 
        }
    }
    for (var i = 0; i < paintColors.length; i++) { // Uses the 
        fill(paintColors[i][0], paintColors[i][1], paintColors[i][2]);
        rect(paintSpace[i][0], paintSpace[i][1], 25, 25);
    }

    //Code to generate the prompt using the random nouns, verbs, and adverbs lists. 
    fill(0, 0, 0);
    textAlign(LEFT);
    var a = round(random(0, 99));
    var b = round(random(0, 99));
    var c = round(random(0, 99));
    textSize(28);
    textLeading(26);
    textAlign(CENTER);
    text("Draw a " + nouns[a] + " " + verbs[b] + "(ing) " + adverbs[c], 58, 345, 326, 329);
};
var home = true; var rules = false; var game = false;
var mouseClicked = function () {
    //0 is home, 1 is instructions, 2 is draw
    // Code looks at where the button is when it is clicked and on what screen. Allowing screen changes. 
    if (home === true) {
        if (mouseX > 33 && mouseX < 183 && mouseY > 340 && mouseY < 390) {
            home = false;
            rules = true;
            game = false;
            rulesScreen();
        }
        else if (mouseX > 212 && mouseX < 362 && mouseY > 340 && mouseY < 390) {
            home = false;
            rules = false;
            game = true;
            gameScreen();
        }
    }
    else if (rules === true) {
        if (mouseX > 33 && mouseX < 183 && mouseY > 340 && mouseY < 390) {
            home = true;
            rules = false;
            game = false;
            homeScreen();
        }
        else if (mouseX > 212 && mouseX < 362 && mouseY > 340 && mouseY < 390) {
            home = false;
            rules = false;
            game = true;
            gameScreen();
        }
    }
    else {
        return;
    }
};

var rCurrent; var gCurrent; var bCurrent;


var currentColor = function () {
    var changeColor = function (quad) {//Function that takes the paintColors array for the color clicked and assigns those values to the paintbrush. 
        rCurrent = paintColors[quad][0];
        gCurrent = paintColors[quad][1];
        bCurrent = paintColors[quad][2];
    };
    if (mouseIsPressed && mouseX >= 5 && mouseX <= 55 && mouseY >= 345 && mouseY <= 395) {
        if (mouseX < 30 && mouseY < 370) { changeColor(0); }
        else if (mouseX < 30 && mouseY > 370) { changeColor(1); }
        else if (mouseX > 30 && mouseY < 370) { changeColor(2); }
        else if (mouseX > 30 && mouseY > 370) { changeColor(3); }
    }
};
homeScreen(); //Starts the game with the home screen.
var draw = function () {
    currentColor(); //Checks to see if the color is changed. 
    if (game === true && mouseIsPressed && mouseY < 340) { // Paints the current color when mouse is pressed.
        fill(rCurrent, gCurrent, bCurrent);
        noStroke();
        ellipse(mouseX, mouseY, 10, 10);
    }
};



