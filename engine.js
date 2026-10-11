(function (root) {
  "use strict";
  function r0(x) { return Math.round(x); }
  function r1(x) { return Math.round(x * 10) / 10; }
  function r2(x) { return Math.round(x * 100) / 100; }
  function plural(n, word) { return n + " " + word + (n === 1 ? "" : "s"); }

  function slotPlan(slotW, slotH, pL, pW, pH) {
    if (!(slotW > 0) || !(slotH > 0) || !(pL > 0) || !(pW > 0) || !(pH > 0)) return { error: "slot and parcel must be positive" };
    var s = [slotW, slotH].sort(function (a, b) { return a - b; });
    var p = [pL, pW, pH].sort(function (a, b) { return a - b; });
    var fits = p[0] <= s[0] && p[1] <= s[1];
    return { fits: fits, faceA: p[1], faceB: p[0] };
  }

  function stampPlan(weightG, perStampG, priceEach) {
    if (!(weightG > 0) || !(perStampG > 0) || !(priceEach > 0)) return { error: "weight, stamp limit and price must be positive" };
    var stamps = Math.max(1, Math.ceil(weightG / perStampG));
    var cost = r2(stamps * priceEach);
    return { stamps: stamps, cost: cost };
  }

  function fillPlan(boxL, perDayL) {
    if (!(boxL > 0) || !(perDayL > 0)) return { error: "box and daily mail must be positive" };
    var days = r1(boxL / perDayL);
    return { days: days };
  }

  function renderSlot(r, slotW, slotH, pL, pW, pH) {
    var dims = pL + " x " + pW + " x " + pH;
    var slot = slotW + " x " + slotH;
    if (!r.fits) return "No face of a " + dims + " cm parcel fits the " + slot + " cm slot - it stays with the courier.";
    return "A " + dims + " cm parcel fits the " + slot + " cm slot on its " + r.faceA + " x " + r.faceB + " cm face.";
  }

  function renderStamp(r, weightG, perStampG, priceEach) {
    return "At " + weightG + " g and a labeled " + perStampG + " g per stamp, a letter needs " + plural(r.stamps, "stamp") + " - " + r.cost + " at " + priceEach + " each.";
  }

  function renderFill(r, boxL, perDayL) {
    return "A " + boxL + " L box getting a labeled " + perDayL + " L of mail a day fills up in about " + r.days + " days.";
  }

  var api = { slotPlan: slotPlan, stampPlan: stampPlan, fillPlan: fillPlan, renderSlot: renderSlot, renderStamp: renderStamp, renderFill: renderFill };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.MailboxMath = api;
})(this);
