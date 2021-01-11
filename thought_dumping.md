# Spinoff
Discord bot to make short lived channels for answering a specific question or topic, think threads done as temporary channels

# How to use
## Basic
- `!spinoff <title>` to start a new topic channel, post an invite/link to the channel
- chat in spinoff topic
- end topic conditions
    - No activity (configurable)
    - explicit finish with `!spinoff done`
- repost the text to the main channel when done (optional)
    - thread with original spinoff, add in as a snippet or something.  Searchable still?
    - archive text to external DB, configurable

## Advance configuration/text
- `!spin-<command>` for setting various other parts to the thread, optional
- description
- Tags, comma separated list
- title
- etc

# Search and Rediscovery
## In Discord
    - Send a `!spinoff search` for the current server-channel, get a DM back with directions
    - Get a DM back with the topics
## Web Page (phase 2)
- search by tag, etc
- add more info to stored spinoffs

# Server Configuration
- No Activity threshold
- Spinoff archive time/count
- rate limit channel creation by user
- Total number of spinoffs active

# scaling cost resources
- archive retention
- active spinoffs

