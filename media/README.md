# About the media files

With the exception of the [`figure_anatomy.png`](./figure_anatomy.png) file generated from Matplotlib's code [here](https://matplotlib.org/stable/gallery/showcase/anatomy.html), all media files in this directory were created using content from this workshop. Any video files from screen recordings were converted to GIF files using the following command:

```shell
$ ffmpeg -i file.ext -pix_fmt rgb8 -r 10 file.gif
```

To play in reverse before looping, use the following command:

```shell
$ ffmpeg -i file.ext -filter_complex "[0]reverse[r];[0][r]concat=n=2:v=1:a=0" file.gif
```
