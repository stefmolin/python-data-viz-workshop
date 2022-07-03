"""Utility functions for the workshop."""

def despine(ax):
    """Hide the top and right spines on a Matplotlib Axes object."""
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    return ax
