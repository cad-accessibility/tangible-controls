## Closes

Closes #<!-- issue number -->

## Summary

What changed and why. The PR title becomes the commit message when squash-merged, so use a Conventional Commits prefix: `feat:`, `fix:`, `docs:`, `a11y:`, `chore:` and so on.

## Accessibility impact

How this affects people building or using the devices without sight, or "No accessibility impact."

Images need alt text that says what they show: `![The slider board with its knob halfway along the track](url)`, not "photo".

## Hardware changes

Delete this section if no printed part changed.

- Onshape version: <!-- the /v/ link -->
- What changed, in words: <!-- which part, which dimensions, and why -->

- [ ] Exported from that version, and listed in `onshape.toml`
- [ ] `SHA256SUMS` rewritten with `python3 scripts/check_exports.py --write-sums hardware/<device>`
- [ ] Printed and fitted
- [ ] Parts list and build guide updated

## Testing

- [ ] `python3 scripts/check_exports.py` passes
- [ ] `reuse lint` passes
- [ ] Tried on a real device (say which)
