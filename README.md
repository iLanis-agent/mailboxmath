# Mailbox math

Whether a parcel actually fits the letterbox slot, how many stamps a letter really needs, and how many days an unemptied mailbox lasts. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/mailboxmath/

## The three tools

- **Slot plan** - `slotPlan(slotW, slotH, pL, pW, pH)`: checks every face of the parcel against the slot.
- **Stamp plan** - `stampPlan(weightG, perStampG, priceEach)`: stamps needed and cost.
- **Fill plan** - `fillPlan(boxL, perDayL)`: days until the box fills up.

## Labeled norms (illustrative references, not rules)

- Slot: 25 x 4 cm letterbox. Stamp: covers 20 g of letter. Daily mail: 3 L per day. Your slot, stamps and mail decide the real numbers.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (15 cases, 56 checks)

Regenerate the oracle expectations: `python3 oracle.py`
