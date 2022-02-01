# Let’s implement a simple flask server that finds the correct
# translation for hello in a dictionary of translations.
# We want our server to respond to requests to /translation/<language>.
#
# If the received language doesn’t exist, we want to return a 404
# response.

translations = {
    "en": "hello",
    "es": "hola",
    "it": "ciao",
}