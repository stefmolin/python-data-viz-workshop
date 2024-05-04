"""Utility functions for the workshop."""

import datetime as dt


def despine(ax):
    """Hide the top and right spines on a Matplotlib Axes object."""
    ax.spines[['top', 'right']].set_visible(False)
    return ax

def mpl_svg_config(hashsalt):
    """Help configure the SVG backend for Matplotlib and make it reproducible."""
    from matplotlib import rc
    rc('svg', hashsalt=hashsalt)

    return {
        'metadata': {
            'Date': f'(c) 2021-{dt.date.today().year} Stefanie Molin'
        }
    }

def save_plot(fig, filename):
    """Save the figure with a white background."""
    fig.savefig(filename, facecolor='white', bbox_inches='tight')
