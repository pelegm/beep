"""
.. beep.py

Implementations of beeps.
"""

import subprocess as sp


def beep(freq=1000, time=1, block=False):
    """ Beep through the computer's speaker, with frequency *freq*, for the
    duration of *time* seconds. If *block*, do it via a blocking process;
    otherwise do it via a non-blocking process. """
    miliseconds = int(time * 1000)
    command = sp.call if block else sp.Popen
    args = ["beep", "-f", str(freq), "-l", str(miliseconds)]
    command(args)


def beep_seq(freqs, times):
    """ Beep a sequence of frequency-time pairs; block while doing that. """
    [beep(freq=f, time=t, block=True) for f, t in zip(freqs, times)]


def sirene(low=100, high=2000, time=1, block=True):
    """ Make a sirene-like sequence of beeps. """
    parts = 20
    part = 1.0 * (high - low) / (parts - 1)
    part_time = 1.0 * time / (2 * parts)
    up_seq = [low + n*part for n in xrange(parts)]
    down_seq = [high - n*part for n in xrange(parts)][1:]
    freqs = up_seq + down_seq
    beep_seq(freqs=freqs, times=[part_time]*len(freqs))

