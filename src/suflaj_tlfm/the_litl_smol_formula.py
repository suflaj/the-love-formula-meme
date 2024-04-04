import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arrow
import numpy as np


def upper_heart_boundary(x):
    return (1 - x**2) ** (1 / 2) + (x ** (2 / 3))


def lower_heart_boundary(x):
    return -((1 - x**2) ** (1 / 2)) + (x ** (2 / 3))


parser = argparse.ArgumentParser()
parser.add_argument(
    "output_path",
    type=str,
    help="Where to save the PNG",
    metavar="FILE",
)
arguments = parser.parse_args()

x = np.arange(
    0,
    1.0001,
    0.001,
)
lower_y = lower_heart_boundary(x)
lower_y[0] = lower_y[0] / 1.007
upper_y = upper_heart_boundary(x)


x = np.concatenate(
    [
        -x[::-1],
        x,
    ],
)
lower_y = np.concatenate(
    [
        lower_y[::-1],
        lower_y,
    ],
)
upper_y = np.concatenate(
    [
        upper_y[::-1],
        upper_y,
    ],
)

small_x = x * 0.25
small_lower_y = lower_y * 0.25
small_upper_y = upper_y * 0.25

x_arrow = np.arange(
    -1,
    -0.05,
    0.05,
)
x_arrow_continuation = np.arange(
    0.5,
    1.0001,
    0.05,
)
y_arrow = x_arrow + 0.5
y_arrow_continuation = x_arrow_continuation + 0.5

x += 1.5
lower_y += 1.5
upper_y += 1.5
x_arrow += 1.5
y_arrow += 1.5
x_arrow_continuation += 1.5
y_arrow_continuation += 1.5

x_mirrored = -x
lower_y_mirrored = -lower_y
upper_y_mirrored = -upper_y
x_arrow_mirrored = -x_arrow
y_arrow_mirrored = -y_arrow
x_arrow_continuation_mirrored = -x_arrow_continuation
y_arrow_continuation_mirrored = -y_arrow_continuation


fig, ax = plt.subplots(
    1,
    3,
    figsize=(11.69, 8.27),
    width_ratios=[1, 9, 1],
    dpi=600,
)


ax[0].set_axis_off()
ax[2].set_axis_off()


rc = {
    "xtick.direction": "inout",
    "ytick.direction": "inout",
    "xtick.major.size": 5,
    "ytick.major.size": 5,
}
with plt.rc_context(rc):
    ax[1].spines["left"].set_position("zero")
    ax[1].spines["right"].set_visible(False)
    ax[1].spines["bottom"].set_position("zero")
    ax[1].spines["top"].set_visible(False)

    # Remove 0 ticks on axis
    ax[1].xaxis.get_major_ticks()[3].set_visible(False)
    ax[1].yaxis.get_major_ticks()[4].set_visible(False)

    ax[1].xaxis.set_ticks_position("bottom")
    ax[1].yaxis.set_ticks_position("left")

    # make arrows
    ax[1].plot(
        (1),
        (0),
        ls="",
        marker=">",
        ms=10,
        color="k",
        transform=ax[1].get_yaxis_transform(),
        clip_on=False,
        zorder=1,
    )
    ax[1].plot(
        (0),
        (1),
        ls="",
        marker="^",
        ms=10,
        color="k",
        transform=ax[1].get_xaxis_transform(),
        clip_on=False,
        zorder=1,
    )

    ax[1].fill(
        small_x - 2,
        small_lower_y + 2,
        color="#9b1528",
        zorder=100,
    )
    ax[1].fill(
        small_x - 2,
        small_upper_y + 2,
        color="#9b1528",
        zorder=100,
    )
    ax[1].fill(
        small_x - 1,
        small_lower_y + 1,
        color="#9b1528",
        zorder=100,
    )
    ax[1].fill(
        small_x - 1,
        small_upper_y + 1,
        color="#9b1528",
        zorder=100,
    )
    ax[1].fill(
        small_x + 2,
        small_lower_y - 2,
        color="#9b1528",
        zorder=100,
    )
    ax[1].fill(
        small_x + 2,
        small_upper_y - 2,
        color="#9b1528",
        zorder=100,
    )
    ax[1].fill(
        small_x + 1,
        small_lower_y - 1,
        color="#9b1528",
        zorder=100,
    )
    ax[1].fill(
        small_x + 1,
        small_upper_y - 1,
        color="#9b1528",
        zorder=100,
    )

    ax[1].fill(
        x,
        lower_y,
        color="#c496f0",
        zorder=100,
    )
    ax[1].fill(
        x,
        upper_y,
        color="#c496f0",
        zorder=100,
    )
    ax[1].plot(
        x,
        lower_y,
        color="#ffb7ce",
        linewidth=5,
        zorder=101,
    )
    ax[1].plot(
        x,
        upper_y,
        color="#ffb7ce",
        linewidth=5,
        zorder=101,
    )
    ax[1].plot(
        x_arrow,
        y_arrow,
        color="#885511",
        linewidth=3,
        zorder=101,
    )
    ax[1].plot(
        x_arrow_continuation,
        y_arrow_continuation,
        color="#885511",
        linewidth=3,
        zorder=99,
    )
    ax[1].arrow(
        x_arrow_continuation[-1],
        y_arrow_continuation[-1],
        0.001,
        0.001,
        edgecolor="#555555",
        facecolor="#777777",
        head_width=0.2,
        width=0.03,
        zorder=100,
    )

    ax[1].fill(
        x_mirrored,
        lower_y_mirrored,
        color="#c496f0",
        zorder=100,
    )
    ax[1].fill(
        x_mirrored,
        upper_y_mirrored,
        color="#c496f0",
        zorder=100,
    )
    ax[1].plot(
        x_mirrored,
        lower_y_mirrored,
        color="#ffb7ce",
        linewidth=5,
        zorder=101,
    )
    ax[1].plot(
        x_mirrored,
        upper_y_mirrored,
        color="#ffb7ce",
        linewidth=5,
        zorder=101,
    )
    ax[1].plot(
        x_arrow_mirrored,
        y_arrow_mirrored,
        color="#885511",
        linewidth=3,
        zorder=101,
    )
    ax[1].plot(
        x_arrow_continuation_mirrored,
        y_arrow_continuation_mirrored,
        color="#885511",
        linewidth=3,
        zorder=99,
    )
    ax[1].arrow(
        x_arrow_continuation_mirrored[-1],
        y_arrow_continuation_mirrored[-1],
        -0.001,
        -0.001,
        edgecolor="#555555",
        facecolor="#777777",
        head_width=0.2,
        width=0.03,
        zorder=100,
    )

output_path = Path(arguments.output_path).resolve()
output_path.parent.mkdir(
    parents=True,
    exist_ok=True,
)

fig.savefig(str(output_path))
