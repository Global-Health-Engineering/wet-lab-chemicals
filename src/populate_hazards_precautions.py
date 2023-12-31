import argparse


def print_md_table_hazards(list_of_hazards):
    """
    Hazard statements form part of the Globally Harmonized System
    of Classification and Labelling of Chemicals (GHS).
    """
    d_hazards = {
        "H200":           "unstable explosive",
        "H201":           "explosive: mass explosion hazard",
        "H202":           "explosive: severe projection hazard",
        "H203":           "explosive: fire, blast or projection hazard",
        "H204":           "fire or projection hazard",
        "H205":           "may mass explode in fire",
        "H206":           "fire, blast or projection hazard: increased risk of explosion if desensitizing agent is reduced",
        "H207":           "fire or projection hazard; increased risk of explosion if desensitizing agent is reduced",
        "H208":           "fire hazard; increased risk of explosion if desensitizing agent is reduced",
        "H209":           "explosive",
        "H210":           "very sensitive",
        "H211":           "may be sensitive",
        "H220":           "extremely flammable gas",
        "H221":           "flammable gas",
        "H222":           "extremely flammable material",
        "H223":           "flammable material",
        "H224":           "extremely flammable liquid and vapour",
        "H225":           "highly flammable liquid and vapour",
        "H226":           "flammable liquid and vapour",
        "H227":           "combustible liquid",
        "H228":           "flammable solid",
        "H229":           "pressurized container: may burst if heated",
        "H230":           "may react explosively even in the absence of air",
        "H231":           "may react explosively even in the absence of air at elevated pressure and/or temperature",
        "H240":           "heating may cause an explosion",
        "H241":           "heating may cause a fire or explosion",
        "H242":           "heating may cause a fire",
        "H250":           "catches fire spontaneously if exposed to air",
        "H251":           "self-heating: may catch fire",
        "H252":           "self-heating in large quantities: may catch fire",
        "H260":           "in contact with water releases flammable gases which may ignite spontaneously",
        "H261":           "in contact with water releases flammable gas",
        "H270":           "may cause or intensify fire: oxidizer",
        "H271":           "may cause fire or explosion: strong oxidizer",
        "H272":           "may intensify fire: OXIDISER",
        "H280":           "contains gas under pressure: may explode if heated",
        "H281":           "contains refrigerated gas: may cause cryogenic burns or injury",
        "H282":           "extremely flammable chemical under pressure: May explode if heated",
        "H283":           "flammable chemical under pressure: May explode if heated",
        "H284":           "chemical under pressure: May explode if heated",
        "H290":           "may be corrosive to metals ",
        "H300":           "fatal if swallowed",
        "H300+H310":      "fatal if swallowed or in contact with skin",
        "H300+H310+H330": "fatal if swallowed, in contact with skin or if inhaled",
        "H300+H330":      "fatal if swallowed or if inhaled",
        "H301":           "toxic if swallowed",
        "H301+H311":      "toxic if swallowed or in contact with skin",
        "H301+H311+H331": "toxic if swallowed, in contact with skin or if inhaled",
        "H301+H331":      "toxic if swallowed or if inhaled",
        "H302":           "harmful if swallowed",
        "H302+H312":      "harmful if swallowed or in contact with skin",
        "H302+H312+H332": "harmful if swallowed, in contact with skin or if inhaled",
        "H302+H332":      "harmful if swallowed or inhaled",
        "H303":           "may be harmful if swallowed",
        "H303+H313":      "may be harmful if swallowed or in contact with skin",
        "H303+H313+H333": "may be harmful if swallowed, in contact with skin or if inhaled",
        "H303+H333":      "may be harmful if swallowed or if inhaled",
        "H304":           "may be fatal if swallowed and enters airways",
        "H305":           "may be harmful if swallowed and enters airways",
        "H310":           "fatal in contact with skin",
        "H310+H330":      "fatal in contact with skin or if inhaled",
        "H311":           "toxic in contact with skin",
        "H311+H331":      "toxic in contact with skin or if inhaled",
        "H312":           "harmful in contact with skin",
        "H312+H332":      "harmful in contact with skin or if inhaled",
        "H313":           "May be harmful in contact with skin",
        "H313+H333":      "may be harmful in contact with skin or if inhaled",
        "H314":           "causes severe skin burns and eye damage",
        "H315":           "causes skin irritation",
        "H315+H320":      "causes skin and eye irritation",
        "H316":           "causes mild skin irritation",
        "H317":           "may cause an allergic skin reaction",
        "H318":           "causes serious eye damage",
        "H319":           "causes serious eye irritation",
        "H320":           "causes eye irritation",
        "H330":           "fatal if inhaled",
        "H331":           "toxic if inhaled",
        "H332":           "harmful if inhaled",
        "H333":           "may be harmful if inhaled",
        "H334":           "may cause allergy or asthma symptoms or breathing difficulties if inhaled",
        "H335":           "may cause respiratory irritation",
        "H336":           "may cause drowsiness or dizziness",
        "H340":           "may cause genetic defects",
        "H341":           "suspected of causing genetic defects",
        "H350":           "may cause cancer",
        "H350i":          "may cause cancer by inhalation",
        "H351":           "suspected of causing cancer",
        "H360":           "may damage fertility or the unborn child",
        "H360D":          "may damage the unborn child",
        "H360Df":         "may damage the unborn child. Suspected of damaging fertility",
        "H360F":          "may damage fertility",
        "H360FD":         "may damage fertility, may damage the unborn child",
        "H360Fd":         "may damage fertility, suspected of damaging the unborn child",
        "H361":           "suspected of damaging fertility or the unborn child",
        "H361d":          "suspected of damaging the unborn child",
        "H361f":          "suspected of damaging fertility",
        "H361fd":         "suspected of damaging fertility, suspected of damaging the unborn child",
        "H362":           "may cause harm to breast-fed children",
        "H370":           "causes damage to organs",
        "H371":           "may cause damage to organs",
        "H372":           "causes damage to organs through prolonged or repeated exposure",
        "H373":           "may cause damage to organs through prolonged or repeated exposure",
        "H400":           "very toxic to aquatic life",
        "H401":           "toxic to aquatic life",
        "H402":           "harmful to aquatic life",
        "H410":           "very toxic to aquatic life with long lasting effects",
        "H411":           "toxic to aquatic life with long lasting effects",
        "H412":           "harmful to aquatic life with long lasting effects",
        "H413":           "may cause long lasting harmful effects to aquatic life",
        "H420":           "harms public health and the environment by destroying ozone in the upper atmosphere",
        "H441":           "very toxic to terrestrial invertebrates"
    }

    res = "| Code | Phrase |\n| ---- | ------ |\n"
    for hazard in list_of_hazards:
        res += f"| {hazard} | {d_hazards[hazard]} |\n"
    print(res)
    
    return res


def print_md_table_precautions(list_of_precautions):
    """
    Precautionary statements form part of the Globally Harmonized System
    of Classification and Labelling of Chemicals (GHS). They are intended
    to form a set of standardized phrases giving advice about the correct
    handling of chemical substances and mixtures.
    """
    d_precautions = {
        "P101":           "if medical advice is needed, have product container or label at hand",
        "P102":           "keep out of reach of children",
        "P103":           "read label before use",
        "P201":           "obtain special instructions before use",
        "P202":           "do not handle until all safety precautions have been read and understood",
        "P210":           "keep away from heat, hot surfaces, sparks, open flames and other ignition sources, no smoking",
        "P211":           "do not spray on an open flame or other ignition source",
        "P220":           "keep/store away from clothing/.../combustible materials",
        "P221":           "take any precaution to avoid mixing with combustibles",
        "P222":           "do not allow contact with air",
        "P223":           "do not allow contact with water",
        "P230":           "keep wetted with .",
        "P231":           "handle and store contents under inert gas/...",
        "P231+P232":      "handle and store contents under inert gas, protect from moisture",
        "P232":           "protect from moisture",
        "P233":           "keep container tightly closed",
        "P234":           "keep only in original container/packaging",
        "P235":           "keep cool",
        "P235+P410":      "keep cool, protect from sunlight",
        "P240":           "ground and bond container and receiving equipment",
        "P241":           "use explosion-proof electrical/ventilating/light/.../equipment",
        "P242":           "use only non-sparking tools",
        "P243":           "take precautionary measures to prevent static discharges",
        "P244":           "keep valves and fittings free from grease and oi",
        "P250":           "do not subject to grinding/shock/.../friction",
        "P251":           "pressurized container – do not pierce or burn, even after use",
        "P260":           "do not breathe dust/fume/gas/mist/vapours/spray",
        "P261":           "avoid breathing dust/fume/gas/mist/vapours/spray",
        "P262":           "do not get in eyes, on skin, or on clothing",
        "P263":           "avoid contact during pregnancy and while nursing",
        "P264":           "wash ... thoroughly after handling",
        "P265":           "do not touch eyes",
        "P270":           "do not eat, drink or smoke when using this product",
        "P271":           "use only outdoors or in a well-ventilated area",
        "P272":           "contaminated work clothing should not be allowed out of the workplace",
        "P273":           "avoid release to the environment",
        "P280":           "wear protective gloves/protective clothing/eye protection/face protection",
        "P281":           "use personal protective equipment as required",
        "P282":           "wear cold insulating gloves and either face shield or eye protection",
        "P283":           "wear fire resistant or flame retardant clothing",
        "P284":           "wear respiratory protection",
        "P285":           "in case of inadequate ventilation wear respiratory protection",
        "P301":           "IF SWALLOWED:",
        "P301+P310":      "IF SWALLOWED: immediately call the ETH Emergency Desk: +41 44 342 11 88 (from mobile) or 888 (from landline)",
        "P301+P312":      "IF SWALLOWED: call the ETH Emergency Desk: +41 44 342 11 88 (from mobile) or 888 (from landline)",
        "P301+P330+P331": "IF SWALLOWED: rinse mouth, do NOT induce vomiting",
        "P302":           "IF ON SKIN:",
        "P302+P334":      "IF ON SKIN: immerse in cool water or wrap in wet bandages",
        "P302+P350":      "IF ON SKIN: gently wash with soap and water",
        "P302+P352":      "IF ON SKIN: wash with soap and water",
        "P303":           "IF ON SKIN (or hair):",
        "P303+P361+P353": "IF ON SKIN (or hair): remove/take off immediately all contaminated clothing, rinse skin with water or shower",
        "P304":           "IF INHALED:",
        "P304+P312":      "IF INHALED: call the ETH Emergency Desk: +41 44 342 11 88 (from mobile) or 888 (from landline) if you feel unwell",
        "P304+P340":      "IF INHALED: remove victim to fresh air and keep at rest in a position comfortable for breathing",
        "P304+P341":      "IF INHALED: if breathing is difficult, remove victim to fresh air and keep at rest in a position comfortable for breathing",
        "P305":           "IF IN EYES:",
        "P305+P351+P338": "IF IN EYES: rinse continuously with water for several minutes, remove contact lenses if present and easy to do, continue rinsing",
        "P306":           "IF ON CLOTHING:",
        "P306+P360":      "IF ON CLOTHING: rinse immediately contaminated clothing and skin with plenty of water before removing clothes",
        "P307":           "IF EXPOSED:",
        "P307+P311":      "IF EXPOSED: call the ETH Emergency Desk: +41 44 342 11 88 (from mobile) or 888 (from landline)",
        "P308":           "IF EXPOSED OR CONCERNED:",
        "P308+P311":      "IF EXPOSED OR CONCERNED: call the ETH Emergency Desk: +41 44 342 11 88 (from mobile) or 888 (from landline)",
        "P308+P313":      "IF EXPOSED OR CONCERNED: get medical advice/attention",
        "P309":           "IF EXPOSED OR YOU FEEL UNWELL:",
        "P309+P311":      "IF EXPOSED OR YOU FEEL UNWELL: call the ETH Emergency Desk: +41 44 342 11 88 (from mobile) or 888 (from landline)",
        "P310":           "immediately call the ETH Emergency Desk: +41 44 342 11 88 (from mobile) or 888 (from landline)",
        "P311":           "call the ETH Emergency Desk: +41 44 342 11 88 (from mobile) or 888 (from landline)",
        "P312":           "call the ETH Emergency Desk: +41 44 342 11 88 (from mobile) or 888 (from landline) if you feel unwell",
        "P313":           "get medical advice/attention",
        "P314":           "get medical advice/attention if you feel unwell",
        "P315":           "get immediate medical advice/attention",
        "P317":           "get emergency medical help",
        "P320":           "specific treatment is urgent (see the label)",
        "P321":           "specific treatment (see the label)",
        "P322":           "specific measures (see the label)",
        "P330":           "rinse mouth",
        "P331":           "do NOT induce vomiting",
        "P332":           "IF SKIN IRRITATION OCCURS:",
        "P332+P313":      "IF SKIN IRRITATION OCCURS: get medical advice/attention",
        "P332+P317":      "IF SKIN IRRITATION OCCURS: get emergency medical help",
        "P333":           "IF SKIN IRRITATION OR A RASH OCCURS:",
        "P333+P313":      "IF SKIN IRRITATION OR A RASH OCCURS: get medical advice/attention",
        "P334":           "immerse in cool water/wrap in wet bandages",
        "P335":           "brush off loose particles from skin",
        "P335+P334":      "brush off loose particles from skin, immerse in cool water/wrap in wet bandages",
        "P336":           "thaw frosted parts with lukewarm water ,do not rub affected areas",
        "P337":           "IF EYE IRRITATION PERSISTS:",
        "P337+P313":      "IF EYE IRRITATION PERSISTS: get medical advice/attention",
        "P337+P317":      "IF EYE IRRITATION PERSISTS: get emergency medical help",
        "P338":           "remove contact lenses if present and easy to do, continue rinsing",
        "P340":           "remove victim to fresh air and keep at rest in a position comfortable for breathing",
        "P341":           "if breathing is difficult, remove victim to fresh air and keep at rest in a position comfortable for breathing",
        "P342":           "IF EXPERIENCING RESPIRATORY SYMPTOMS:",
        "P342+P311":      "IF EXPERIENCING RESPIRATORY SYMPTOMS: call the ETH Emergency Desk: +41 44 342 11 88 (from mobile) or 888 (from landline)",
        "P350":           "gently wash with soap and water",
        "P351":           "rinse cautiously with water for several minutes",
        "P352":           "wash with plenty of water",
        "P353":           "rinse skin with water/shower",
        "P360":           "rinse immediately contaminated clothing and skin with plenty of water before removing clothes",
        "P361":           "remove/take off immediately all contaminated clothing",
        "P361+P364":      "take off immediately all contaminated clothing and wash it before reuse",
        "P362":           "take off contaminated clothing",
        "P362+P364":      "take off contaminated clothing and wash it before reuse",
        "P363":           "wash contaminated clothing before reuse",
        "P364":           "and wash it before reuse",
        "P370":           "IN CASE OF FIRE:",
        "P370+P376":      "IN CASE OF FIRE: stop leak if safe to do so",
        "P370+P378":      "IN CASE OF FIRE: use ... to extinguish",
        "P370+P380":      "IN CASE OF FIRE: evacuate area",
        "P370+P380+P375": "IN CASE OF FIRE: evacuate area, fight fire remotely due to the risk of explosion",
        "P371":           "IN CASE OF MAJOR FIRE AND LARGE QUANTITIES:",
        "P371+P380+P375": "IN CASE OF MAJOR FIRE AND LARGE QUANTITIES: evacuate area, fight fire remotely due to the risk of explosion",
        "P372":           "explosion risk",
        "P373":           "do NOT fight fire when fire reaches explosives",
        "P374":           "fight fire with normal precautions from a reasonable distance",
        "P375":           "fight fire remotely due to the risk of explosion",
        "P376":           "stop leak if safe to do so",
        "P377":           "leaking gas fire – do NOT extinguish unless leak can be stopped safely",
        "P378":           "use ... to extinguish",
        "P380":           "evacuate area",
        "P381":           "in case of leakage, eliminate all ignition sources",
        "P390":           "absorb spillage to prevent material damage",
        "P391":           "collect spillage",
        "P401":           "store in accordance with ...",
        "P402":           "store in a dry place.",
        "P402+P404":      "store in a dry place, store in a closed container",
        "P403":           "store in a well ventilated place",
        "P403+P233":      "store in a well ventilated place, keep container tightly closed",
        "P403+P235":      "store in a well ventilated place, keep cool",
        "P404":           "store in a closed container",
        "P405":           "store locked up",
        "P406":           "store in a corrosive resistant/... container with a resistant inner liner",
        "P407":           "maintain air gap between stacks or pallets",
        "P410":           "protect from sunlight",
        "P410+P403":      "protect from sunlight, store in a well ventilated place",
        "P410+P412":      "protect from sunlight, do NOT expose to temperatures exceeding 50 ºC",
        "P411":           "store at temperatures not exceeding ... ºC",
        "P411+P235":      "store at temperatures not exceeding ... ºC, keep cool",
        "P412":           "do not expose to temperatures exceeding 50 ºC",
        "P413":           "store bulk masses greater than ... kg at temperatures not exceeding ... °C",
        "P420":           "store separately/away from other materials",
        "P422":           "store contents under ...",
        "P501":           "dispose of contents/container to [HCI-Shop](https://hci-shop.ethz.ch/en/)",
        "P502":           "refer to manufacturer or supplier for information on recovery or recycling",
    }
    
    res = "| Code | Phrase |\n| ---- | ------ |\n"
    for precaution in list_of_precautions:
        res += f"| {precaution} | {d_precautions[precaution]} |\n"
    print(res)

    for precaution in list_of_precautions:
        if precaution in ["P370+P378", "P411", "P411+P235", "P412", "P413", "P420", "P422"]:
            print(f"WARNING! Fill out {precaution}.")

    return res


def main():
    parser = argparse.ArgumentParser(description="return Markdown table of Hazards or Precautions")
    parser.add_argument("s", type=str, help="string of Hazards or Precautins, never both at the same time")
    args = parser.parse_args()

    lst = [i.translate(str.maketrans('', '', ':,')) for i in args.s.split()]

    if lst[0][0] == "H":
        print_md_table_hazards(lst)
    elif lst[0][0] == "P":
        print_md_table_precautions(lst)


if __name__ == "__main__":
    main()
