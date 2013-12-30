pybasis
=======

Python script for downloading Basis Band watch data


You can learn more about Basis at [http://www.mybasis.com/](http://www.mybasis.com/)

## Instructions

### Finding Your Basis User ID
- Log into your Basis account at [http://www.mybasis.com](http://www.mybasis.com).
- Right-click and access your web browser's developer tools by selecting "Inspect Element" (on Chrome - you can also access this by going to the "View->Developer->Developer Tools" menu):


- You should now see the Developer Tools pane:
- Go to the "Data" menu and select "Details":
- Click on the "Network" tab in the Developer Tools frame and reload the page:

Scroll down the list of network requests and look for a request that beings with:
"https://app.mybasis.com/api/v1/chart/123a4567b89012345678d9e.json?summary=true..."

The letters after "...chart/" and preceding ".json?..." are your Basis user id! Note this string.


## Credits

This script is mostly based off of work by others:

[http://www.quantifiedbob.com/2013/04/liberating-your-data-from-the-basis-b1-band.html?cid=6a017d3d7cbf3f970c019aff43c05a970c#comment-6a017d3d7cbf3f970c019aff43c05a970c](http://www.quantifiedbob.com/2013/04/liberating-your-data-from-the-basis-b1-band.html?cid=6a017d3d7cbf3f970c019aff43c05a970c#comment-6a017d3d7cbf3f970c019aff43c05a970c)

[https://github.com/btroia/basis-data-export/blob/master/README.md](https://github.com/btroia/basis-data-export/blob/master/README.md)
