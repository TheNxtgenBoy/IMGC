![banner](https://raw.githubusercontent.com/TheNxtgenBoy/IMGC/main/image/imgc.svg)

# IMGC - The Image Metadata Remover
- it removes all the information which is hidden in the image like (geo-location, time-date, model, edited or unedited, etc)
- it is very useful if you want to manipulate an image.

## Download -> <a href="https://github.com/TheNxtgenBoy/IMGC/archive/refs/heads/main.zip">Here</a>

### How to install

- Run **main/install.py**.
- Now it is Installed Run it with this command.
```
python -m imgc image_path
```

### How To Use

- Open **CMD** where images are located.
![](https://raw.githubusercontent.com/TheNxtgenBoy/IMGC/main/image/Screenshot1.png)

- After opening **CMD** run this command ```python -m imgc image_path``` and hit enter.
![](https://raw.githubusercontent.com/TheNxtgenBoy/IMGC/main/image/Screenshot%20(307).png)

- After that its prints a message sucess... it means the operation compleated sucessfully.
![](https://raw.githubusercontent.com/TheNxtgenBoy/IMGC/main/image/Screenshot%20(308).png)

- It will make an another image named ```{original_name}_IMGC.png/jpg``` and its that easy.
![](https://raw.githubusercontent.com/TheNxtgenBoy/IMGC/main/image/Screenshot%20(309).png)

# comparison with and without metadata

| Data                        | Normal_Image                              | IMGC_Image                    |
|-----------------------------|-------------------------------------------|-------------------------------|
| Image                       | <img src="https://clck.ru/sKNj7" width=200px>|  <img src="https://clck.ru/sKNke" width=200px>|
| Filename                    | pexels-photo-2246476.jpg                  | pexels-photo-2246476_IMGC.jpg |
| FileDateTime                | 1658148105                                | 1658149082                    |
| FileSize                    | 2880657                                   | 2696645                       |
| FileType                    | 2                                         | 2                             |
| MimeType                    | image/jpeg                                | image/jpeg                    |
| SectionsFound               | ANY_TAG, IFD0, THUMBNAIL, EXIF            |                               |
| html                        | width="5464" height="3643"                | width="5464" height="3643"    |
| Height                      | 3643                                      | 3643                          |
| Width                       | 5464                                      | 5464                          |
| IsColor                     | 1                                         | 1                             |
| ApertureFNumber             | f/8.0                                     |                               |
| Thumbnail.FileType          | 2                                         |                               |
| Thumbnail.MimeType          | image/jpeg                                |                               |
| Make                        | NIKON CORPORATION                         |                               |
| Model                       | NIKON D5200                               |                               |
| XResolution                 | 72/1                                      |                               |
| YResolution                 | 72/1                                      |                               |
| ResolutionUnit              | 2                                         |                               |
| Software                    | Adobe Photoshop Lightroom 6.5.1 (Windows) |                               |
| DateTime                    | 2017:07:06 23:38:32                       |                               |
| Exif_IFD_Pointer            | 218                                       |                               |
| Compression                 | 6                                         |                               |
| JPEGInterchangeFormat       | 986                                       |                               |
| JPEGInterchangeFormatLength | 22258                                     |                               |
| ExposureTime                | 8/1                                       |                               |
| FNumber                     | 8/1                                       |                               |
| ExposureProgram             | 1                                         |                               |
| ISOSpeedRatings             | 100                                       |                               |
| UndefinedTag:0x8830         | 2                                         |                               |
| ExifVersion                 | 0230                                      |                               |
| DateTimeOriginal            | 2017:07:05 17:34:13                       |                               |
| DateTimeDigitized           | 2017:07:05 17:34:13                       |                               |
| ShutterSpeedValue           | -3/1                                      |                               |
| ApertureValue               | 6/1                                       |                               |
| ExposureBiasValue           | 0/6                                       |                               |
| MaxApertureValue            | 16/10                                     |                               |
| MeteringMode                | 5                                         |                               |
| LightSource                 | 0                                         |                               |
| Flash                       | 0                                         |                               |
| FocalLength                 | 190/10                                    |                               |
| SubSecTimeOriginal          | 90                                        |                               |
| SubSecTimeDigitized         | 90                                        |                               |
| ColorSpace                  | 1                                         |                               |
| FocalPlaneXResolution       | 83841555/32768                            |                               |
| FocalPlaneYResolution       | 83841555/32768                            |                               |
| FocalPlaneResolutionUnit    | 3                                         |                               |
| SensingMethod               | 2                                         |                               |
| CustomRendered              | 0                                         |                               |
| ExposureMode                | 1                                         |                               |
| WhiteBalance                | 0                                         |                               |
| DigitalZoomRatio            | 1/1                                       |                               |
| FocalLengthIn35mmFilm       | 28                                        |                               |
| UndefinedTag:0xA431         | 6320090                                   |                               |
| UndefinedTag:0xA432         | 180/10,350/10,18/10,18/10                 |                               |
| UndefinedTag:0xA434         | 18.0-35.0 mm f/1.8                        |                               |
| Name                        | pexels-photo-2246476.jpg                  | pexels-photo-2246476_IMGC.jpg |
| Type                        | image/jpeg                                | image/jpeg                    |
| Size                        | 2880657                                   | 2696645                       |
