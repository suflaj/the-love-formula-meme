import argparse
from pathlib import Path

import matplotlib.pyplot as plt
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
    1.000001,
    0.0001,
)
lower_y = lower_heart_boundary(x)
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


fig, ax = plt.subplots(
    2,
    1,
    figsize=(8.27, 11.69),
    height_ratios=[1, 3],
    dpi=600,
)


ax[0].set_axis_off()
p = plt.Rectangle(
    (0, 0),
    1,
    1,
    fill=False,
    edgecolor="white",
)
p.set_transform(ax[0].transAxes)
p.set_clip_on(False)
ax[0].add_patch(p)
ax[0].text(
    0.5,
    1.0,
    "THE LOVE FORMULA",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax[0].transAxes,
    fontsize=48,
    fontweight="light",
)
ax[0].text(
    0.5,
    0.5,
    "$\\mathbf{x^2 + {\\left( y - \\sqrt[3]{x^2} \\right)}^2 = 1}$",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax[0].transAxes,
    fontsize=32,
    color="#9b1528",
    usetex=True,
)

rc = {
    "xtick.direction": "inout",
    "ytick.direction": "inout",
    "xtick.major.size": 5,
    "ytick.major.size": 5,
}
with plt.rc_context(rc):
    """
    ax[1].plot(x, lower_y, color="#9b1528", linewidth=5)
    ax[1].plot(x, upper_y, color="#9b1528", linewidth=5)
    """

    ax[1].spines["left"].set_position("zero")
    ax[1].spines["right"].set_visible(False)
    ax[1].spines["bottom"].set_position("zero")
    ax[1].spines["top"].set_visible(False)

    ax[1].xaxis.get_major_ticks()[2].set_visible(False)
    ax[1].xaxis.get_major_ticks()[4].set_visible(False)
    ax[1].xaxis.get_major_ticks()[5].set_visible(False)
    # ax[1].xaxis.get_major_ticks()[6].set_visible(False)
    # ax[1].xaxis.get_major_ticks()[8].set_visible(False)

    ax[1].yaxis.get_major_ticks()[3].set_visible(False)

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

    ax[1].plot(
        x,
        lower_y,
        color="#9b1528",
        linewidth=5,
        zorder=100,
    )
    ax[1].plot(
        x,
        upper_y,
        color="#9b1528",
        linewidth=5,
        zorder=100,
    )

output_path = Path(arguments.output_path).resolve()
output_path.parent.mkdir(
    parents=True,
    exist_ok=True,
)

fig.savefig(str(output_path))
