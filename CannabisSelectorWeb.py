import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import sys

# Get the base directory (handles PyInstaller bundling)
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STRAIN_PHOTO_DIR = os.path.join(BASE_DIR, "Strain_Photos")

strains = {
    "Super Soldier Serum": {
        "description": "A potent hybrid with a cerebral buzz and relaxing body high, ideal for creativity and stress relief.",
        "uses": ["creativity", "euphoria", "stress relief"],
        "type": "Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Limonene (citrus, uplifting)", "Caryophyllene (spicy, stress relief)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "supersolderserum.PNG")
    },
    "Wedding Cake": {
        "description": "A rich indica-dominant hybrid with sweet, tangy flavors, offering deep relaxation and euphoria.",
        "uses": ["relaxation", "euphoria", "sleep"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Caryophyllene (spicy, calming)", "Humulene (woody, anti-inflammatory)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "wedding_cake.png")
    },
    "Dog CBD": {
        "description": "A CBD-rich hybrid designed for calming effects with minimal psychoactivity, often used for anxiety relief.",
        "uses": ["calm", "anxiety relief", "sleep"],
        "type": "Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Pinene (pine, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "dog_cbd.png")
    },
    "Lunar Diesel": {
        "description": "A sativa-leaning hybrid with a diesel-like aroma and uplifting, energetic effects.",
        "uses": ["energy", "focus", "mood boost"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Pinene (pine, focus)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "lunar_diesel.png")
    },
    "Ice Cream Cake": {
        "description": "An indica-heavy hybrid with creamy flavors, promoting deep relaxation and sedation.",
        "uses": ["relaxation", "sleep", "pain relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Limonene (citrus, mood boost)", "Caryophyllene (spicy, stress relief)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "ice_cream_cake.png")
    },
    "Gary Payton": {
        "description": "A balanced hybrid with a peppery, sweet profile, delivering euphoria and physical relaxation.",
        "uses": ["euphoria", "relaxation", "social"],
        "type": "Hybrid",
        "terpenes": ["Caryophyllene (spicy, calming)", "Limonene (citrus, uplifting)", "Pinene (pine, focus)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "gary_payton.png")
    },
    "Rootbeer Rockz x Minties": {
        "description": "A unique hybrid with sweet, minty notes, offering a balanced high for relaxation and creativity.",
        "uses": ["creativity", "relaxation", "mood boost"],
        "type": "Hybrid",
        "terpenes": ["Linalool (floral, calming)", "Myrcene (earthy, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "rootbeer_rockz_x_minties.png")
    },
    "Tropical Banana": {
        "description": "A sativa-dominant strain with fruity, banana-like flavors, boosting energy and mood.",
        "uses": ["energy", "focus", "mood boost"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Terpinolene (fruity, energizing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "tropical_banana.png")
    },
    "GG4": {
        "description": "A powerful indica-dominant hybrid known for its sticky resin and heavy relaxation effects.",
        "uses": ["relaxation", "sleep", "pain relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Caryophyllene (spicy, anti-inflammatory)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "gg4.png")
    },
    "Mendo Breath": {
        "description": "A sweet indica strain with strong sedative effects, ideal for relaxation and stress relief.",
        "uses": ["relaxation", "sleep", "stress relief"],
        "type": "Indica",
        "terpenes": ["Myrcene (earthy, sedative)", "Caryophyllene (spicy, calming)", "Linalool (floral, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "mendo_breath.png")
    },
    "Kept Secret": {
        "description": "A mysterious hybrid with earthy flavors, blending euphoria and calm.",
        "uses": ["euphoria", "relaxation", "social"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Linalool (floral, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "kept_secret.png")
    },
    "Pink Zkittles": {
        "description": "A fruity indica-dominant hybrid with uplifting yet calming effects, known for its candy-like taste.",
        "uses": ["euphoria", "relaxation", "appetite"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Limonene (citrus, mood boost)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "pink_zkittles.png")
    },
    "Red Runtz": {
        "description": "A candy-flavored hybrid with a balanced mix of relaxation and euphoria.",
        "uses": ["euphoria", "appetite", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Caryophyllene (spicy, stress relief)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "red_runtz.png")
    },
    "Cherry AK47": {
        "description": "A sativa-dominant strain with cherry notes, delivering energy and focus with a mild body high.",
        "uses": ["energy", "focus", "mood boost"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Pinene (pine, focus)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "cherry_ak47.png")
    },
    "Original Jack": {
        "description": "A classic sativa strain offering clear-headed, creative effects, inspired by Jack Herer.",
        "uses": ["creativity", "focus", "energy"],
        "type": "Sativa",
        "terpenes": ["Pinene (pine, alertness)", "Terpinolene (floral, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "original_jack.png")
    },
    "Sweet & Sour Jack": {
        "description": "A sativa-leaning hybrid with tangy, sweet flavors, boosting energy and mood.",
        "uses": ["energy", "mood boost", "focus"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Myrcene (earthy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "sweet_sour_jack.png")
    },
    "Tally Man": {
        "description": "A balanced hybrid with fruity flavors, offering relaxation and mild euphoria.",
        "uses": ["euphoria", "relaxation", "social"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Caryophyllene (spicy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "tally_man.png")
    },
    "Easy Bake": {
        "description": "An indica-dominant strain with a sweet profile, ideal for unwinding and sedation.",
        "uses": ["relaxation", "sleep", "stress relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Linalool (floral, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "easy_bake.png")
    },
    "Garlic Gaillionair": {
        "description": "A pungent indica strain with savory garlic notes, delivering deep relaxation.",
        "uses": ["relaxation", "sleep", "pain relief"],
        "type": "Indica",
        "terpenes": ["Myrcene (earthy, sedative)", "Caryophyllene (spicy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "garlic_gaillionair.png")
    },
    "Mandarin Cookies": {
        "description": "A hybrid with citrusy, cookie-like flavors, blending euphoria and relaxation.",
        "uses": ["euphoria", "relaxation", "social"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Myrcene (earthy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "mandarin_cookies.png")
    },
    "Glueball": {
        "description": "A sticky indica-dominant hybrid with intense relaxation and euphoria.",
        "uses": ["relaxation", "sleep", "pain relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Caryophyllene (spicy, stress relief)", "Myrcene (earthy, sedative)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "glueball.png")
    },
    "Pink Z": {
        "description": "A fruity hybrid with uplifting and calming effects, derived from Zkittlez lineage.",
        "uses": ["euphoria", "appetite", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Myrcene (earthy, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "pink_z.png")
    },
    "Strawberry Guava": {
        "description": "A sativa-leaning hybrid with sweet, tropical flavors and energizing effects.",
        "uses": ["energy", "mood boost", "focus"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Terpinolene (fruity, energizing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "strawberry_guava.png")
    },
    "Tahitian Pearl": {
        "description": "A balanced hybrid with exotic, fruity flavors, offering relaxation and mild euphoria.",
        "uses": ["euphoria", "relaxation", "social"],
        "type": "Hybrid",
        "terpenes": ["Linalool (floral, calming)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "tahitian_pearl.png")
    },
    "White Cindy": {
        "description": "A sativa-dominant hybrid with uplifting, creative effects, from Cinderella 99 lineage.",
        "uses": ["creativity", "energy", "focus"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Pinene (pine, focus)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "white_cindy.png")
    },
    "AJ's Bud": {
        "description": "A hybrid with balanced effects, ideal for relaxation and social enjoyment.",
        "uses": ["relaxation", "social", "euphoria"],
        "type": "Hybrid",
        "terpenes": ["Myrcene (earthy, calming)", "Caryophyllene (spicy, stress relief)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "ajs_bud.png")
    },
    "Read Headed Stranger": {
        "description": "A sativa strain with energizing and euphoric effects, often linked to Red Headed Stranger.",
        "uses": ["energy", "mood boost", "focus"],
        "type": "Sativa",
        "terpenes": ["Limonene (citrus, uplifting)", "Pinene (pine, focus)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "read_headed_stranger.png")
    },
    "Red Froot": {
        "description": "A hybrid with fruity flavors, offering relaxation and mild euphoria.",
        "uses": ["euphoria", "appetite", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Myrcene (earthy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "red_froot.png")
    },
    "Fucshia": {
        "description": "An indica-dominant strain with floral notes, ideal for deep relaxation.",
        "uses": ["relaxation", "sleep", "stress relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Linalool (floral, sedative)", "Myrcene (earthy, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "fucshia.png")
    },
    "Final Boss #4": {
        "description": "A potent hybrid with strong effects, blending relaxation and euphoria.",
        "uses": ["euphoria", "relaxation", "pain relief"],
        "type": "Hybrid",
        "terpenes": ["Caryophyllene (spicy, stress relief)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "final_boss_4.png")
    },
    "I-95": {
        "description": "A hybrid with diesel-like potency, offering a balanced high with relaxation and energy.",
        "uses": ["energy", "relaxation", "focus"],
        "type": "Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "i95.png")
    },
    "Lemon Grinder": {
        "description": "A sativa-dominant strain with zesty lemon flavors, boosting energy and focus.",
        "uses": ["energy", "focus", "mood boost"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Pinene (pine, alertness)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "lemon_grinder.png")
    },
    "Screaming OG": {
        "description": "An indica-dominant hybrid with loud, potent effects, great for relaxation and pain relief.",
        "uses": ["relaxation", "sleep", "pain relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Caryophyllene (spicy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "screaming_og.png")
    },
    "Apple Jack": {
        "description": "A sativa-leaning hybrid with apple flavors, offering energy and euphoria.",
        "uses": ["energy", "mood boost", "creativity"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Pinene (pine, focus)", "Terpinolene (fruity, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "apple_jack.png")
    },
    "Royal Skunk": {
        "description": "A hybrid with skunky notes, providing relaxation and mild euphoria.",
        "uses": ["relaxation", "euphoria", "social"],
        "type": "Hybrid",
        "terpenes": ["Myrcene (earthy, calming)", "Caryophyllene (spicy, stress relief)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "royal_skunk.png")
    },
    "Black Velvet": {
        "description": "A smooth indica with deep relaxation and velvety effects, perfect for unwinding.",
        "uses": ["relaxation", "sleep", "stress relief"],
        "type": "Indica",
        "terpenes": ["Myrcene (earthy, sedative)", "Linalool (floral, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "black_velvet.png")
    },
    "Octane": {
        "description": "A high-energy sativa with fuel-like potency, ideal for daytime activity.",
        "uses": ["energy", "focus", "mood boost"],
        "type": "Sativa",
        "terpenes": ["Limonene (citrus, uplifting)", "Pinene (pine, focus)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "octane.png")
    },
    "Truck Stop": {
        "description": "A hybrid with earthy tones, offering a balanced high for relaxation and mild euphoria.",
        "uses": ["relaxation", "euphoria", "social"],
        "type": "Hybrid",
        "terpenes": ["Myrcene (earthy, calming)", "Caryophyllene (spicy, stress relief)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "truck_stop.png")
    },
    "Violet Fog": {
        "description": "An indica-dominant strain with hazy, calming effects and a floral undertone.",
        "uses": ["relaxation", "sleep", "stress relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Linalool (floral, sedative)", "Myrcene (earthy, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "violet_fog.png")
    },
    "Biscotti 2.0": {
        "description": "A refined indica-hybrid with sweet, nutty flavors, promoting relaxation and calm.",
        "uses": ["relaxation", "sleep", "pain relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Caryophyllene (spicy, calming)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "biscotti_2_0.png")
    },
    "Randy Marsh": {
        "description": "A quirky hybrid with balanced effects, great for social fun and relaxation.",
        "uses": ["euphoria", "social", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Myrcene (earthy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "randy_marsh.png")
    },
    "Swampwater Fumez": {
        "description": "An indica strain with earthy, dank effects, ideal for deep relaxation.",
        "uses": ["relaxation", "sleep", "stress relief"],
        "type": "Indica",
        "terpenes": ["Myrcene (earthy, sedative)", "Caryophyllene (spicy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "swampwater_fumez.png")
    },
    "Cheeseburger Haze": {
        "description": "A sativa-dominant hybrid with savory notes and uplifting, energetic effects.",
        "uses": ["energy", "mood boost", "focus"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Pinene (pine, focus)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "cheeseburger_haze.png")
    },
    "Chem Puff": {
        "description": "A hybrid with chemical potency, offering euphoria and relaxation.",
        "uses": ["euphoria", "relaxation", "appetite"],
        "type": "Hybrid",
        "terpenes": ["Myrcene (earthy, calming)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "chem_puff.png")
    },
    "Future Diesel": {
        "description": "A sativa-leaning hybrid with diesel flavors and energizing effects.",
        "uses": ["energy", "focus", "mood boost"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Pinene (pine, focus)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "future_diesel.png")
    },
    "Kush Mints": {
        "description": "An indica-dominant hybrid with minty freshness and strong relaxation effects.",
        "uses": ["relaxation", "sleep", "stress relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "kush_mints.png")
    },
    "Whipped Grapes": {
        "description": "A hybrid with grape flavors, blending relaxation and euphoria.",
        "uses": ["euphoria", "appetite", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Myrcene (earthy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "whipped_grapes.png")
    },
    "GMO": {
        "description": "A funky indica-dominant hybrid with intense relaxation and a pungent garlic aroma.",
        "uses": ["relaxation", "sleep", "pain relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Caryophyllene (spicy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "gmo.png")
    },
    "Roasted Garlic Margy": {
        "description": "An indica strain with savory garlic notes and deep sedative effects.",
        "uses": ["relaxation", "sleep", "stress relief"],
        "type": "Indica",
        "terpenes": ["Myrcene (earthy, sedative)", "Linalool (floral, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "roasted_garlic_margy.png")
    },
    "NYC Chem 110": {
        "description": "A hybrid with chemical potency, offering a balanced high of energy and relaxation.",
        "uses": ["energy", "relaxation", "focus"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Myrcene (earthy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "nyc_chem_110.png")
    },
    "NYC Chem 74": {
        "description": "A hybrid with diesel-like effects, blending energy and relaxation.",
        "uses": ["energy", "focus", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Pinene (pine, focus)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "nyc_chem_74.png")
    },
    "Blue Nerds": {
        "description": "A hybrid with sweet, candy-like flavors and balanced effects of euphoria and calm.",
        "uses": ["euphoria", "appetite", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Myrcene (earthy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "blue_nerds.png")
    },
    "Grape Honey": {
        "description": "An indica-dominant strain with sweet grape notes and soothing relaxation.",
        "uses": ["relaxation", "sleep", "appetite"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Linalool (floral, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "grape_honey.png")
    },
    "Jelly Haze": {
        "description": "A sativa-dominant hybrid with fruity haze effects, boosting energy and creativity.",
        "uses": ["energy", "creativity", "mood boost"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Pinene (pine, focus)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "jelly_haze.png")
    },
    "Moon Palace": {
        "description": "An indica strain with dreamy, sedative effects and a smooth flavor profile.",
        "uses": ["relaxation", "sleep", "stress relief"],
        "type": "Indica",
        "terpenes": ["Myrcene (earthy, sedative)", "Linalool (floral, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "moon_palace.png")
    },
    "Pink Lucy": {
        "description": "A hybrid with floral, uplifting effects and a calming finish.",
        "uses": ["euphoria", "social", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Linalool (floral, relaxing)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "pink_lucy.png")
    },
    "Scroopy Noopers": {
        "description": "A playful hybrid with balanced euphoria and relaxation, offering a fun experience.",
        "uses": ["euphoria", "appetite", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Myrcene (earthy, calming)", "Caryophyllene (spicy, stress relief)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "scroopy_noopers.png")
    },
    "Coal Creek Kush": {
        "description": "An indica-dominant strain with earthy potency and deep relaxation effects.",
        "uses": ["relaxation", "sleep", "pain relief"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Caryophyllene (spicy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "coal_creek_kush.png")
    },
    "Prince": {
        "description": "A regal hybrid with balanced effects, great for social settings and mild relaxation.",
        "uses": ["euphoria", "social", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Myrcene (earthy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "prince.png")
    },
    "Strawnana": {
        "description": "A hybrid with strawberry-banana flavors, offering relaxation and euphoria.",
        "uses": ["euphoria", "appetite", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Myrcene (earthy, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "strawnana.png")
    },
    "Chem Pie": {
        "description": "A hybrid with chemical potency, blending energy and relaxation with a unique flavor.",
        "uses": ["energy", "euphoria", "relaxation"],
        "type": "Hybrid",
        "terpenes": ["Pinene (pine, focus)", "Limonene (citrus, uplifting)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "chem_pie.png")
    },
    "Hazelnut Cream": {
        "description": "An indica-dominant strain with nutty flavors and sedative effects.",
        "uses": ["relaxation", "sleep", "appetite"],
        "type": "Indica-Dominant Hybrid",
        "terpenes": ["Myrcene (earthy, sedative)", "Linalool (floral, relaxing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "hazelnut_cream.png")
    },
    "Kiwi Comet": {
        "description": "A sativa-leaning hybrid with fruity kiwi flavors and energizing effects.",
        "uses": ["energy", "focus", "mood boost"],
        "type": "Sativa-Dominant Hybrid",
        "terpenes": ["Limonene (citrus, uplifting)", "Terpinolene (fruity, energizing)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "kiwi_comet.png")
    },
    "Ruby Grapes": {
        "description": "An indica strain with sweet grape notes and deep relaxation effects.",
        "uses": ["relaxation", "sleep", "appetite"],
        "type": "Indica",
        "terpenes": ["Myrcene (earthy, sedative)", "Linalool (floral, calming)"],
        "image": os.path.join(STRAIN_PHOTO_DIR, "ruby_grapes.png")
    }
}

class CannabisSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wildflowers Dispensary - Strain Selector")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f4f8")
        self.answers = []

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font=("Helvetica", 12), padding=10, background="#4CAF50", foreground="white")
        style.configure("TLabel", font=("Helvetica", 14), background="#f0f4f8", foreground="#2E7D32")
        style.map("TButton", background=[("active", "#45a049")])

        self.header_frame = ttk.Frame(root, padding="10")
        self.header_frame.pack(fill="x")

        try:
            logo_path = os.path.join(BASE_DIR, "logo.png")
            self.logo_image = Image.open(logo_path).resize((150, 150), Image.LANCZOS)
            self.logo = ImageTk.PhotoImage(self.logo_image)
            self.logo_label = ttk.Label(self.header_frame, image=self.logo)
            self.logo_label.pack(pady=10)
        except Exception as e:
            self.logo_label = ttk.Label(self.header_frame, text=f"Logo Error: {e}", foreground="red")
            self.logo_label.pack(pady=10)

        self.content_frame = ttk.Frame(root, padding="20")
        self.content_frame.pack(expand=True, fill="both")

        welcome_text = (
            "Welcome to Wildflowers Dispensary!\n\n"
            "Find your perfect strain—whether for relaxation, energy, or fun.\n"
            "Click 'Start' to begin, and feel free to ask your budtender any questions!"
        )
        self.question_label = ttk.Label(self.content_frame, text=welcome_text, wraplength=500, justify="center")
        self.question_label.pack(pady=20)

        self.button_frame = ttk.Frame(self.content_frame)
        self.button_frame.pack(pady=20)
        self.start_button = ttk.Button(self.button_frame, text="Start", command=self.start_questions)
        self.start_button.pack()
        self.option_buttons = []

    def start_questions(self):
        self.start_button.pack_forget()
        self.logo_label.pack_forget()
        self.question_label.config(text="What’s your primary goal?")
        self.show_options(["Relax and Sleep", "Boost Appetite", "Feel Energized", "Have Fun or Socialize"])

    def show_options(self, options):
        print(f"Showing options: {options}")  # Debug
        for button in self.option_buttons:
            button.pack_forget()
        self.option_buttons = []
        for option in options:
            btn = ttk.Button(self.button_frame, text=option, command=lambda o=option: self.next_step(o), width=25)
            btn.pack(pady=5)
            self.option_buttons.append(btn)
        self.button_frame.update()

    def next_step(self, choice):
        print(f"Choice selected: {choice}")  # Debug
        self.answers.append(choice)
        print(f"Answers: {self.answers}")  # Debug
        if len(self.answers) == 1:
            if choice == "Relax and Sleep":
                self.question_label.config(text="How intense do you want the relaxation?")
                self.show_options(["Mild", "Deep"])
            elif choice == "Boost Appetite":
                print("Boost Appetite selected")  # Debug
                self.question_label.config(text="What vibe do you want with your appetite boost?")
                self.show_options(["Chill", "Upbeat"])
            elif choice == "Feel Energized":
                self.question_label.config(text="Do you need to focus or just feel active?")
                self.show_options(["Focus (Study/Work)", "Active (Action)"])
            elif choice == "Have Fun or Socialize":
                self.question_label.config(text="What kind of social vibe are you feeling?")
                self.show_options(["Chill Gathering", "Lively Evening"])
        elif len(self.answers) == 2:
            strain = self.get_result()
            print(f"Result strain: {strain}")  # Debug
            self.show_result(strain)

    def get_result(self):
        goal, detail = self.answers
        if goal == "Relax and Sleep":
            return "Wedding Cake" if detail == "Mild" else "Mendo Breath"
        elif goal == "Boost Appetite":
            return "Ice Cream Cake" if detail == "Chill" else "Red Runtz"
        elif goal == "Feel Energized":
            return "Original Jack" if detail == "Focus (Study/Work)" else "Tropical Banana"
        elif goal == "Have Fun or Socialize":
            return "Gary Payton" if detail == "Chill Gathering" else "Super Soldier Serum"

    def show_result(self, strain_name):
        strain_info = strains.get(strain_name)
        result_text = (
            f"Recommended Strain: {strain_name}\n\n"
            f"Type: {strain_info['type']}\n"
            f"Description: {strain_info['description']}\n"
            f"Best for: {', '.join(strain_info['uses'])}\n"
            f"Key Terpenes: {', '.join(strain_info['terpenes'])}"
        )

        result_window = tk.Toplevel(self.root)
        result_window.title("Your Strain Recommendation")
        result_window.geometry("450x500")
        result_window.configure(bg="#f0f4f8")

        try:
            strain_image = Image.open(strain_info['image']).resize((200, 200), Image.LANCZOS)
            strain_photo = ImageTk.PhotoImage(strain_image)
            image_label = ttk.Label(result_window, image=strain_photo)
            image_label.image = strain_photo
            image_label.pack(pady=10)
        except Exception as e:
            image_label = ttk.Label(result_window, text=f"Image Error: {e}", foreground="red")
            image_label.pack(pady=10)

        info_label = ttk.Label(result_window, text=result_text, wraplength=400, justify="center")
        info_label.pack(pady=10)
        close_button = ttk.Button(result_window, text="Close", command=result_window.destroy)
        close_button.pack(pady=10)

        self.restart()

    def restart(self):
        self.answers = []
        self.question_label.config(text=(
            "Welcome to Wildflowers Dispensary!\n\n"
            "Find your perfect strain—whether for relaxation, energy, or fun.\n"
            "Click 'Start' to begin, and feel free to ask your budtender any questions!"
        ))
        for button in self.option_buttons:
            button.pack_forget()
        self.option_buttons = []
        self.logo_label.pack(in_=self.header_frame, pady=10)
        self.start_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CannabisSelectorApp(root)
    root.mainloop()
