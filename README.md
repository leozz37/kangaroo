# Foxy 🦊

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d0ecfb33e92f46b4aa08ad6713a613f4)](https://www.codacy.com/gh/leozz37/foxy/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=leozz37/foxy&amp;utm_campaign=Badge_Grade)
[![CodeFactor](https://www.codefactor.io/repository/github/leozz37/foxy/badge)](https://www.codefactor.io/repository/github/leozz37/foxy)
![Python](https://github.com/leozz37/foxy/workflows/Python/badge.svg)
[![Documentation](https://codedocs.xyz/leozz37/foxy.svg)](https://codedocs.xyz/leozz37/foxy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Download all images from a website!

## Parameters

| Tag            | Description                                      | Required  |
| -------------- | ------------------------------------------------ | --------- |
| -u, --url      | Target URL of the website to download the images | Yes       |
| -d, --download | Download flag, the images will be downloaded     | No        |

## Running

Install dependencies:

```shell
$ pip install -r requirements.txt
```

Running:

```shell
$ python3 scrapper.py -u $TARGET_URL
```
