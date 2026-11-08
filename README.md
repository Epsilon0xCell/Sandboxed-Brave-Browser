![Intro: a closer look through the terrarium glass, water beading on the inside of the pane, the miniature desk and its glowing screen lit among the ferns behind the droplets](intro-banner.png)


# Sandboxed-Brave-Browser

<p align="center"><img src="logo.png" alt="Sandboxed-Brave-Browser logo: a drawn round emblem of a glass terrarium, a green fern and rocks over soil inside the dome on a steel base, on a dark ground" width="200"></p>

![Banner: a large glass terrarium with a steel frame on a wooden workbench, ferns and sand planted inside it, and a miniature desk with a glowing computer screen among the plants](banner.png)

![Animated scene: the gorge in profile, lanterns flickering, the bell swaying, a goat crossing, the river sliding below](scene.svg)

A custom sandboxed brave browser.

`sandbox.sh` runs Brave inside Firejail. It needs both `firejail` and
`brave` on PATH; if either is missing it says so and exits instead of
launching Brave without the sandbox. Any arguments are passed through to
Brave: `./sandbox.sh https://example.com`

![Separator](sep-heavy.svg)

> **Toll keeper's margin note:** if firejail or brave is missing, the script says so and exits instead of launching Brave without the sandbox.

> **Toll keeper's margin note:** arguments pass through unchanged, quoted as `"$@"`, so an argument with spaces stays one argument.
