import matplotlib.pyplot as plt
import numpy as np
from pHcalc import System


def generate_sillen(acids, names, acids_names, pHbar, labels, pKabar):
    # initialize pH for plotting
    pHs = np.linspace(0, 14, 1000)
    conc_H = -pHs
    conc_OH = -(14 - pHs)

    # initialize plotting
    fig, ax = plt.subplots()

    # create output path
    output_path = "Output/" + " ".join(acids_names) + ".png"

    # Major ticks every 2, minor ticks every 1
    major_ticks = np.arange(0, 14, 2)
    minor_ticks = np.arange(0, 14, 1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(-major_ticks)
    ax.set_yticks(-minor_ticks, minor=True)

    ax.set_xlim((0, 14))
    ax.set_xlabel("pH")

    ax.set_ylim((-14, 0))
    ax.set_ylabel("log(conc/M)")

    ax.grid(which="minor", alpha=0.2)
    ax.grid(which="major", alpha=0.5)

    # plot pH and pOH
    ax.plot(pHs, conc_H, color="blue", alpha=0.1)
    ax.plot(pHs, conc_OH, color="blue", alpha=0.1)

    for i, acid in enumerate(acids):
        conc_acid = np.log10(acid.alpha(pHs) * acid.conc)
        regions = np.shape(conc_acid)[1]
        # separate different regions
        # for region in conc_acid[:]
        for ri in range(regions):
            if labels:
                ax.plot(
                    pHs,
                    conc_acid[:, ri],
                    color="C%s" % (i + 1),
                    alpha=0.2 + 0.8 * (ri / regions),
                    label=names[i] + "_" + str(ri),
                )
            else:
                ax.plot(
                    pHs,
                    conc_acid[:, ri],
                    color="C%s" % (i + 1),
                    alpha=0.2 + 0.8 * (ri / regions),
                )

    # plot the pH of the system if pHbar is true
    if pHbar:
        system = System(*acids)
        system.pHsolve()
        plt.axvline(x=system.pH, linestyle="dashed", color="red")
        ax.annotate("pH= " + str(round(system.pH, 1)), xy=(system.pH + 0.5, -0.5))

    if pKabar:
        for acid in acids:
            for pKa in acid.pKa:
                plt.axvline(x=pKa, linestyle="dashed", color="blue")

    ax.legend()

    fig.savefig(output_path)

    plt.show()


def generate_Verteilung(acids, names, acids_names):
    # initialize pH for plotting
    pHs = np.linspace(0, 14, 1000)

    # initialize plotting
    fig, ax = plt.subplots()

    # create output path
    output_path = "Output/" + " ".join(acids_names) + " Verteilungsdiagram.png"

    # Major ticks every 2, minor ticks every 1
    ax.set_xticks(np.arange(0, 14, 2))
    ax.set_xticks(np.arange(0, 14, 1), minor=True)
    ax.set_yticks(np.arange(0, 100, 10))
    ax.set_yticks(np.arange(0, 100, 5), minor=True)

    # Set labels and scale
    ax.set_xlim((0, 14))
    ax.set_xlabel("pH")

    ax.set_ylim((0, 100))
    ax.set_ylabel("alpha [%]")

    ax.grid(which="minor", alpha=0.2)
    ax.grid(which="major", alpha=0.5)

    # Plot alpha values
    fracs = acids.alpha(pHs) * 100
    plt.plot(pHs, fracs)

    # Check at which pH the alpha values are around 90% and print the results
    array = np.where(np.around(fracs, decimals=0, out=None) == 90)[0] / 1000 * 14
    print(array)
    plt.vlines(x=array, ymin=0, ymax=100, colors="purple", alpha=0.2)
    ax.legend(names)

    fig.savefig(output_path)

    plt.show()
