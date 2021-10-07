from plagiarize.core import plagiarize


def test_plagiarize():
    text = (
        "The Chernobyl disaster was caused by a nuclear accident that occurred on "
        "Saturday 26 April 1986, at the No. 4 reactor in the Chernobyl Nuclear "
        "Power Plant, near the city of Pripyat in the north of the Ukrainian SSR. "
        "It is considered the worst nuclear disaster in history and was caused by "
        "one of only two nuclear energy accidents rated at seven—the maximum "
        "severity—on the International Nuclear Event Scale, the other being "
        "the 2011 Fukushima Daiichi nuclear disaster in Japan."
    )
    clean_text = plagiarize(text)
    assert text != clean_text
