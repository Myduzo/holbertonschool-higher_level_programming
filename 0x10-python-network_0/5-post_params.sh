#!/bin/bash
# this script sends a POST request to the passed URL, and displays the body of the response.
curl -s "$1" --data "email=hr@holbertonschool.com&subject=I will always be here for PLD"
