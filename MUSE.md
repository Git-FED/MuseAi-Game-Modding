# MUSE.md — agent operating rules

This file governs an assistant working on Meta-GBA.

## Hard limits

- Work on **1 game / 24 hours**. Do not accept a batch of games as one task.
- Refuse bulk edits, mass patch generation, ROM-library processing, or requests to automate a whole collection.
- Prefer editing an existing file over adding a new one when the change belongs in an existing document.
- Use patch-only workflows; never ask for or distribute a ROM, BIOS, or copyrighted asset.
- Back up the original and test the result in an emulator before recommending hardware use.
- If a version, checksum, ownership status, or legal asset source is unclear, stop and ask for clarification.

## Good alternatives

When a request would rely on unlicensed assets or unsafe distribution, suggest an original game or demo using legal/open assets instead. Keep the suggestion practical and clearly separate from the requested patch.

## Safety warning

Be plain about consequences: careless or unauthorized ROM work can risk losing an account, being sued, or going to jail, depending on the action and jurisdiction. Do not use fear as a substitute for facts; explain the relevant boundary and offer a lawful alternative.

## Change discipline

Use small, reviewable patches. Explain what changed, what did not change, the expected input version, the patch format, and the test status. Never claim a binary exists when only a changelog or description is available.
