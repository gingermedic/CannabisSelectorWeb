const strains = {
    "Super Soldier Serum": {
        "description": "A potent hybrid with a cerebral buzz and relaxing body high.",
        "uses": ["creativity", "euphoria", "stress relief"],
        "type": "Hybrid",
        "terpenes": ["Myrcene", "Limonene", "Caryophyllene"],
        "image": "images/supersolderserum.PNG"
    },
    "Wedding Cake": {
        "description": "A rich indica-dominant hybrid with sweet, tangy flavors.",
        "uses": ["relaxation", "euphoria", "sleep"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Limonene", "Caryophyllene", "Humulene"],
        "image": "images/wedding_cake.png"
    },
    "Ice Cream Cake": {
        "description": "An indica-heavy hybrid with creamy flavors.",
        "uses": ["relaxation", "sleep", "pain relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene", "Limonene", "Caryophyllene"],
        "image": "images/ice_cream_cake.png"
    },
    "Red Runtz": {
        "description": "A candy-flavored hybrid with a balanced mix of relaxation.",
        "uses": ["euphoria", "appetite", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Caryophyllene", "Limonene"],
        "image": "images/red_runtz.png"
    }
    // Add your remaining 62 strains here
};

let answers = [];

function startQuestions() {
    document.getElementById('welcome').style.display = 'none';
    document.getElementById('question').style.display = 'block';
    showQuestion("What’s your primary goal?", ["Relax and Sleep", "Boost Appetite", "Feel Energized", "Have Fun or Socialize"], nextStep);
}

function showQuestion(text, options, callback) {
    document.getElementById('question-text').textContent = text;
    const optionsDiv = document.getElementById('options');
    optionsDiv.innerHTML = '';
    options.forEach(option => {
        const btn = document.createElement('button');
        btn.textContent = option;
        btn.onclick = () => callback(option);
        optionsDiv.appendChild(btn);
    });
}

function nextStep(choice) {
    answers.push(choice);
    if (answers.length === 1) {
        if (choice === "Relax and Sleep") {
            showQuestion("How intense do you want the relaxation?", ["Mild", "Deep"], showResult);
        } else if (choice === "Boost Appetite") {
            showQuestion("What vibe do you want with your appetite boost?", ["Chill", "Upbeat"], showResult);
        } else if (choice === "Feel Energized") {
            showQuestion("Do you need to focus or just feel active?", ["Focus (Study/Work)", "Active (Action)"], showResult);
        } else if (choice === "Have Fun or Socialize") {
            showQuestion("What kind of social vibe are you feeling?", ["Chill Gathering", "Lively Evening"], showResult);
        }
    }
}

function showResult(choice) {
    answers.push(choice);
    const [goal, detail] = answers;
    const strainName = getResult(goal, detail);
    const strain = strains[strainName];
    document.getElementById('question').style.display = 'none';
    const resultDiv = document.getElementById('result');
    resultDiv.style.display = 'block';
    document.getElementById('result-title').textContent = `Recommended Strain: ${strainName}`;
    document.getElementById('result-image').src = strain.image;
    document.getElementById('result-description').textContent = strain.description;
    document.getElementById('result-type').textContent = `Type: ${strain.type}`;
    document.getElementById('result-uses').textContent = `Best for: ${strain.uses.join(', ')}`;
    document.getElementById('result-terpenes').textContent = `Terpenes: ${strain.terpenes.join(', ')}`;
}

function getResult(goal, detail) {
    if (goal === "Relax and Sleep") return detail === "Mild" ? "Wedding Cake" : "Ice Cream Cake";
    if (goal === "Boost Appetite") return detail === "Chill" ? "Ice Cream Cake" : "Red Runtz";
    if (goal === "Feel Energized") return detail === "Focus (Study/Work)" ? "Super Soldier Serum" : "Super Soldier Serum"; // Adjust as needed
    if (goal === "Have Fun or Socialize") return detail === "Chill Gathering" ? "Wedding Cake" : "Super Soldier Serum";
    return "Super Soldier Serum"; // Default
}

function reset() {
    answers = [];
    document.getElementById('result').style.display = 'none';
    document.getElementById('welcome').style.display = 'block';
}