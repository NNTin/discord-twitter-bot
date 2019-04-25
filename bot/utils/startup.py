"""
The methods bordered() and _get_startup_screen_specs() were copied from https://github.com/Cog-Creators/Red-DiscordBot/
redbot/core/utils/chat_formatting.py     @tekulvw
It is licensed under GNU General Public License v3.0

The rest is unrelated to their project and was written by me.
"""

from typing import Sequence
import itertools
import codecs
import sys


def bordered(*columns: Sequence[str], ascii_border: bool = False) -> str:
    """Get two blocks of text in a borders.
    Note
    ----
    This will only work with a monospaced font.
    Parameters
    ----------
    *columns : `sequence` of `str`
        The columns of text, each being a list of lines in that column.
    ascii_border : bool
        Whether or not the border should be pure ASCII.
    Returns
    -------
    str
        The bordered text.
    """
    borders = {
        "TL": "-" if ascii_border else "┌",  # Top-left
        "TR": "-" if ascii_border else "┐",  # Top-right
        "BL": "-" if ascii_border else "└",  # Bottom-left
        "BR": "-" if ascii_border else "┘",  # Bottom-right
        "HZ": "-" if ascii_border else "─",  # Horizontal
        "VT": "|" if ascii_border else "│",  # Vertical
    }

    sep = " " * 4  # Separator between boxes
    widths = tuple(max(len(row) for row in column) + 9 for column in columns)  # width of each col
    colsdone = [False] * len(columns)  # whether or not each column is done
    lines = [sep.join("{TL}" + "{HZ}" * width + "{TR}" for width in widths)]

    for line in itertools.zip_longest(*columns):
        row = []
        for colidx, column in enumerate(line):
            width = widths[colidx]
            done = colsdone[colidx]
            if column is None:
                if not done:
                    # bottom border of column
                    column = "{HZ}" * width
                    row.append("{BL}" + column + "{BR}")
                    colsdone[colidx] = True  # mark column as done
                else:
                    # leave empty
                    row.append(" " * (width + 2))
            else:
                column += " " * (width - len(column))  # append padded spaces
                row.append("{VT}" + column + "{VT}")

        lines.append(sep.join(row))

    final_row = []
    for width, done in zip(widths, colsdone):
        if not done:
            final_row.append("{BL}" + "{HZ}" * width + "{BR}")
        else:
            final_row.append(" " * (width + 2))
    lines.append(sep.join(final_row))

    return "\n".join(lines).format(**borders)


def _get_startup_screen_specs():
    """Get specs for displaying the startup screen on stdout.
    This is so we don't get encoding errors when trying to print unicode
    emojis to stdout (particularly with Windows Command Prompt).
    Returns
    -------
    `tuple`
        Tuple in the form (`str`, `str`, `bool`) containing (in order) the
        on symbol, off symbol and whether or not the border should be pure ascii.
    """
    encoder = codecs.getencoder(sys.stdout.encoding)
    check_mark = "\N{SQUARE ROOT}"
    try:
        encoder(check_mark)
    except UnicodeEncodeError:
        on_symbol = "[X]"
        off_symbol = "[ ]"
    else:
        on_symbol = check_mark
        off_symbol = "X"

    try:
        encoder("┌┐└┘─│")  # border symbols
    except UnicodeEncodeError:
        ascii_border = True
    else:
        ascii_border = False

    return on_symbol, off_symbol, ascii_border


def pprint(config):
    on_symbol, off_symbol, ascii_border = _get_startup_screen_specs()

    follow = []
    track = []
    location = []
    webhook_urls = []
    for element in config["Discord"]:
        follow.extend(x for x in element.get("twitter_ids", []) if x not in follow)
        track.extend(x for x in element.get("track", []) if x not in track)
        location.extend(x for x in element.get("location", []))
        webhook_urls.extend(x for x in element.get("webhook_urls", []))

    INFO = [
        "        _   _ _   _ _____ _                 ____ _____ ____",
        "       | \ | | \ | |_   _(_)_ __           |  _ \_   _| __ )",
        "       |  \| |  \| | | | | | '_ \   _____  | | | || | |  _ \\",
        "       | |\  | |\  | | | | | | | | |_____| | |_| || | | |_) |",
        "       |_| \_|_| \_| |_| |_|_| |_|         |____/ |_| |____/",
        "",
        "Discord-Twitter-Bot has a detailed documentation, found here:",
        "https://nntin.github.io/discord-twitter-bot",
        "",
        "Twitter Users: {}".format(len(follow)),
        "Tracked Words: {}".format(len(track)),
        "Location Boxes: {}".format(int(len(location) / 4)),
        "Webhook URLs: {}".format(len(webhook_urls)),
        "Defined Feeds: {}".format(len(config["Discord"])),
    ]
    print(bordered(INFO, ascii_border=ascii_border))

    INFOS = []
    for instance in config["Discord"]:
        instance_info = []
        options = (
            ("Include Reply To User", instance.get("IncludeReplyToUser", True)),
            ("Include User Reply", instance.get("IncludeUserReply", True)),
            ("Include Retweet", instance.get("IncludeRetweet", True)),
            ("Custom Message", True if instance.get("custom_message", "") is not "" else False),
            ("Keyword Sets", True if instance.get("keyword_sets", "") is not "" else False),
            ("Blackword Sets", True if instance.get("blackword_sets", "") is not "" else False),
        )
        for option, enabled in options:
            enabled = on_symbol if enabled else off_symbol
            instance_info.append("{} {}".format(enabled, option))

        if instance.get("twitter_ids", []):
            instance_info.append("Twitter Users: {}".format(len(instance["twitter_ids"])))
        if instance.get("track", []):
            instance_info.append("Track Words: {}".format(len(instance["track"])))
        if instance.get("location", []):
            instance_info.append("Location Boxes: {}".format(int(len(instance["location"]) / 4)))
        if instance.get("webhook_urls", []):
            instance_info.append("Webhook URLs: {}".format(len(instance["webhook_urls"])))

        INFOS.append(instance_info)

    i = 0
    while i < len(INFOS):
        print(bordered(*INFOS[i : i + 2], ascii_border=ascii_border))
        i += 2


if __name__ == "__main__":
    import sys

    sys.path.append("..")
    from config import config, auth
    from bot.utils.twitter_id_converter import Converter

    c = Converter(config, auth)
    pprint(c.convert())
