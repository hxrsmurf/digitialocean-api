# digitialocean-api

Uses [DigitalOcean](https://digitalocean.com) [API V2](https://developers.digitalocean.com/documentation/v2/) and Python to create and delete droplets.

I use this to create a quick jump box.

1. Create a (personal access token)(https://www.digitalocean.com/docs/apis-clis/api/create-personal-access-token/)
2. PowerShell (most up-to-date) and Python version
3. Useful functions I use

## Functions

- getDroplet
- listDomains
- listDomainRecords
- getDomainRecords
- createDomainRecord
- updateDomainRecord
- deleteDomainRecord
- bulkDeleteDomainRecords
- createDroplet
- deleteDroplet
- myIP (get's myIP and updates the DNS records, this is a WIP as the update APi doesn't seem to like data)

# PyQt5 GUI

![](pyqt5\pyqt5.png)