# coding: utf-8


import keyword
import re


from django import template
from django.template.defaultfilters import escape, safe


register = template.Library()


@register.filter
def fmt_line(line):
    python_kw_set = frozenset(keyword.kwlist)
    _line = escape(line.line).replace(' ', '&nbsp;')
    _line = _line or '&nbsp;'
    for kword in python_kw_set:
        _line = re.sub(r'\b%s\b' % kword, '<b>%s</b>' % kword, _line)
    return safe(_line)


@register.inclusion_tag('tag_diff_to_html.html')
def diff_to_html(diff, commit_number, number_in_commit):
    return {
        "diff": diff,
        "commit_number": commit_number,
        "number_in_commit": number_in_commit,
        "anchor": diff.make_anchor(number_in_commit),
        "enumerated_lines": enumerate(diff.lines),
    }
