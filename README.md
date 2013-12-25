pybasis
=======

Python script for downloading Basis Band watch data


You can learn more about Basis at [http://www.mybasis.com/](http://www.mybasis.com/)

## Instructions

### Finding Your Basis User ID
- Log into your Basis account at [http://www.mybasis.com](http://gist.github.com).
- Right-click and access your web browser's developer tools by selecting "Inspect Element" (on Chrome - you can also access this by going to the "View->Developer->Developer Tools" menu):

![basis export step 1](http://www....png)

- You should now see the Developer Tools pane:

![basis export step 2](http://www....png)

- Go to the "Data" menu and select "Details":

![basis export step 3](http://www....png)

- Click on the "Network" tab in the Developer Tools frame and reload the page:

![basis export step 4](http://www....png)

Scroll down the list of network requests and look for a request that beings with:
"https://app.mybasis.com/api/v1/chart/123a4567b89012345678d9e.json?summary=true..."

The letters after "...chart/" and preceding ".json?..." are your Basis user id! Note this string.
