# Governance

How changes reach this repository, who decides, and what happens to the design if someone leaves.

## Maintainers

- **Carlos E. Tejada** ([@ctejada10](https://github.com/ctejada10)) maintains the repository, the docs and the releases.
- **Felix Hähnlein** ([@Obikate](https://github.com/Obikate)) designed the cubes and has the final say on the printed parts.

Access to this repository matches [cad-a11y](https://github.com/cad-accessibility/cad-a11y): the same people have the same roles in both.

## How changes reach master

- Nobody pushes to `master` directly. Every change, from anyone, arrives as a pull request.
- A pull request needs one approval from someone with write access other than its author. Its checks must pass: `reuse-lint`, `check-exports` and `pr-title`. Its branch must be up to date with `master`.
- Pull requests are squash-merged, so `master` gets one commit per pull request, titled with the pull request's title.
- `master` cannot be deleted or force-pushed.
- Organization owners can merge a pull request without the approval. GitHub records when they do, and they still have to go through a pull request.

## The hardware design

- The Onshape document named in each `hardware/<device>/onshape.toml` is the source of the design. Only maintainers edit it. Anyone with the link can view it.
- Files in `hardware/` are only ever exported from a named Onshape version of that document. The `check-exports` check enforces this.
- **Felix approves every change to a printed part before it is released.** GitHub accepts any maintainer's approval, so this rule is kept by people, not by the settings.
- If you don't maintain the design, you can't edit the Onshape document, so a design change starts as an issue. Say what should change and why, with measurements or the results of a test print. If you made the change in your own copy of the document, link that copy's version. A maintainer then makes the change in the source document.
- Each printed part should carry the version it was released in, raised or embossed, so a part in hand can be matched to its files.

## Releases

- Versions follow Semantic Versioning, with the hardware meaning described in [CHANGELOG.md](CHANGELOG.md).
- Release tags start with `v`. Only repository admins and maintainers can create, move or delete them. Sign them with `git tag -s`.
- Releases are immutable. Once published, a release's files and tag cannot change. So create the release as a draft, attach the exports and `SHA256SUMS`, check them, and only then publish.

## If a maintainer leaves

- Before the owner of an Onshape document leaves, they transfer its ownership to a remaining maintainer or to a University of Washington account. Without that, the source of the design can be lost.
- Organization owners can give another person the maintainer role.
