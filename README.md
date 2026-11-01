![Intro scenery: the bridge at dusk, bowl empty, bell unrung, a ring of toadstools at the bridge foot](intro-banner.png)

# Sandboxed-Brave-Browser

![Wordmark banner: the toll board at the near end of the bridge carrying the project name, a troll and a goat mid negotiation](banner.png)

![Animated scene: the gorge in profile, lanterns flickering, the bell swaying, a goat crossing, the river sliding below](scene.svg)

A custom sandboxed brave browser.

`sandbox.sh` runs Brave inside Firejail. It needs both `firejail` and
`brave` on PATH; if either is missing it says so and exits instead of
launching Brave without the sandbox. Any arguments are passed through to
Brave: `./sandbox.sh https://example.com`

![Separator](sep-heavy.svg)

> **Toll keeper's margin note:** if firejail or brave is missing, the script says so and exits instead of launching Brave without the sandbox.

> **Toll keeper's margin note:** arguments pass through unchanged, quoted as `"$@"`, so an argument with spaces stays one argument.
