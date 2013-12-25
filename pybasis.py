#!/usr/bin/python
# -*- coding: utf-8 -*-

import  datetime


#Change to your userid, see README.md on where to get it
userid = '000000000000000000000000'

import_interval = '60'
import_offset = '0'


def import_data( import_date ):
    """ Tries to get data for the particular date specified.  """

    # Request data from Basis for selected date.
    # Note we're requesting all available data.
    dataurl = 'https://app.mybasis.com/api/v1/chart/' \
        + userid + '.json?'                 \
        + 'summary=true'                    \
        + '&interval=' + import_interval    \
        + '&units=s'                        \
        + '&start_date=' + str(import_date) \
        + '&start_offset=' + import_offset  \
        + '&end_offset=' + import_offset    \
        + '&heartrate=true'                 \
        + '&steps=true'                     \
        + '&calories=true'                  \
        + '&gsr=true'                       \
        + '&skin_temp=true'                 \
        + '&air_temp=true'                  \
        + '&bodystates=true'

    import urllib2
    print "Requesting Basis data for %s..  " % str(import_date)
    response = urllib2.urlopen( dataurl )
    jsonstr = response.read()

    import json
    pydat = json.loads( jsonstr )

    return pydat


if __name__=="__main__":

    print import_data( datetime.date(2013, 9, 5) )


