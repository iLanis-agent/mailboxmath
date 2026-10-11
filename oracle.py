import json, math

def r1(x): return math.floor(x * 10 + 0.5) / 10
def r2(x): return math.floor(x * 100 + 0.5) / 100
def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word): return str(n) + " " + word + ("" if n == 1 else "s")
def fmt(x): return str(jsnum(x))

def slot_plan(slotW, slotH, pL, pW, pH):
    if not (slotW > 0) or not (slotH > 0) or not (pL > 0) or not (pW > 0) or not (pH > 0):
        return {"error": "slot and parcel must be positive"}
    s = sorted([slotW, slotH])
    p = sorted([pL, pW, pH])
    fits = p[0] <= s[0] and p[1] <= s[1]
    return {"fits": fits, "faceA": jsnum(p[1]), "faceB": jsnum(p[0])}

def stamp_plan(weightG, perStampG, priceEach):
    if not (weightG > 0) or not (perStampG > 0) or not (priceEach > 0):
        return {"error": "weight, stamp limit and price must be positive"}
    stamps = max(1, math.ceil(weightG / perStampG))
    cost = r2(stamps * priceEach)
    return {"stamps": stamps, "cost": jsnum(cost)}

def fill_plan(boxL, perDayL):
    if not (boxL > 0) or not (perDayL > 0):
        return {"error": "box and daily mail must be positive"}
    return {"days": jsnum(r1(boxL / perDayL))}

def render_slot(r, slotW, slotH, pL, pW, pH):
    dims = fmt(pL) + " x " + fmt(pW) + " x " + fmt(pH)
    slot = fmt(slotW) + " x " + fmt(slotH)
    if not r["fits"]:
        return ("No face of a " + dims + " cm parcel fits the " + slot
                + " cm slot - it stays with the courier.")
    return ("A " + dims + " cm parcel fits the " + slot + " cm slot on its "
            + fmt(r["faceA"]) + " x " + fmt(r["faceB"]) + " cm face.")

def render_stamp(r, weightG, perStampG, priceEach):
    return ("At " + fmt(weightG) + " g and a labeled " + fmt(perStampG) + " g per stamp, a letter needs "
            + plural(r["stamps"], "stamp") + " - " + fmt(r["cost"]) + " at " + fmt(priceEach) + " each.")

def render_fill(r, boxL, perDayL):
    return ("A " + fmt(boxL) + " L box getting a labeled " + fmt(perDayL) + " L of mail a day fills up in about "
            + fmt(r["days"]) + " days.")

cases = []
for slotW, slotH, pL, pW, pH in [(25, 4, 30, 25, 3.5), (25, 4, 30, 25, 10), (30, 5, 12, 10, 4),
                                  (20, 3, 25, 15, 2.5), (25, 4, 28, 26, 8), (0, 4, 30, 25, 3.5)]:
    r = slot_plan(slotW, slotH, pL, pW, pH)
    cases.append({"fn": "slotPlan", "args": [slotW, slotH, pL, pW, pH], "result": r,
                  "render": None if "error" in r else render_slot(r, slotW, slotH, pL, pW, pH)})
for weightG, perStampG, priceEach in [(85, 20, 0.85), (18, 20, 0.85), (200, 20, 1.1), (41, 20, 0.85), (0, 20, 0.85)]:
    r = stamp_plan(weightG, perStampG, priceEach)
    cases.append({"fn": "stampPlan", "args": [weightG, perStampG, priceEach], "result": r,
                  "render": None if "error" in r else render_stamp(r, weightG, perStampG, priceEach)})
for boxL, perDayL in [(40, 3), (25, 4), (60, 2.5), (0, 3)]:
    r = fill_plan(boxL, perDayL)
    cases.append({"fn": "fillPlan", "args": [boxL, perDayL], "result": r,
                  "render": None if "error" in r else render_fill(r, boxL, perDayL)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
