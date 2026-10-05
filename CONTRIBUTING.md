# Contributing

Thanks for your interest in the CAD A11y controls. Build reports are as useful as code: if you built a cube or a slider, tell us how it went, even if nothing went wrong.

Who reviews and merges, and how design changes are decided, is in [GOVERNANCE.md](GOVERNANCE.md).

## Before you start

- For anything bigger than a typo, open an issue first, so we can agree on the change before you spend time on it.
- Changes to a printed part start as an issue, because the design lives in Onshape. [GOVERNANCE.md](GOVERNANCE.md#the-hardware-design) explains why.
- Keep pull requests small and focused.

## Branches and pull requests

Create a short-lived branch from `master`, named with a Conventional Commits prefix:

```text
feat/what-you-are-adding
fix/what-you-are-fixing
docs/what-you-are-documenting
a11y/what-you-are-improving
```

The pull request title becomes the commit message when it is squash-merged, so it has to follow [Conventional Commits](https://www.conventionalcommits.org/). The `pr-title` check enforces this. The types are the same as in cad-a11y: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`, `build`, `perf` and `a11y`. A scope is optional:

```text
feat(cube): publish the v0.1.0 print files
fix(slider): print readings as whole numbers
docs(cube): describe the charging port by touch
a11y: split the assembly steps into one action each
```

In the pull request description:

- Link the issue with `Closes #NNN`.
- Describe the accessibility impact, even if it is "No accessibility impact."
- Give every image alt text that says what the image shows.

## Writing the guides

The guides are for blind and low-vision makers first.

- Write one action per step, and say how the reader will know it worked: an announcement, a sound, a click, a drive appearing.
- Never make a step depend on an image. If a photo helps, give it alt text, and put the same information in the text as well.
- Describe parts by shape, size and position, and say how to tell similar parts apart by touch. Don't write "see the figure", "the blue one" or "as shown".
- Use the viewer's exact names for views, such as x+ and z-, and its exact labels for buttons and sections.
- Say what to do when a step fails.
- Keep parts lists as plain CSV with a single header row.

## Changing the hardware

Follow [docs/export-from-onshape.md](docs/export-from-onshape.md). Never edit an export by hand: the `check-exports` check compares every file with its checksum and with the Onshape version it came from. Commit only the STEP and Parasolid files. STL and 3MF print files go on the GitHub release, and the check rejects them in the repository.

## Changing the firmware

Follow [firmware/slider-trinkey/README.md](firmware/slider-trinkey/README.md). Record the CircuitPython and library bundle versions you tested with.

## Checks you can run yourself

```sh
python3 scripts/check_exports.py
reuse lint
```

`check_exports.py` needs Python 3.11 or later and nothing else. To install `reuse`, run `pipx install 'reuse[charset-normalizer]'`.

## Using GitHub with a screen reader

The `gh` command-line tool works well with screen readers. These settings make it quieter and easier to follow:

```sh
gh config set accessible_prompter enabled
gh config set accessible_colors enabled
gh config set spinner disabled
```

Then, for example, `gh issue list`, `gh pr create --fill` and `gh pr checks` cover most of a contribution. The manual is at https://cli.github.com/manual/.
