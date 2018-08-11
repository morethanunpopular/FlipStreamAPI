# FlipStreamAPI
The FlipStream API is a rest API for creating Story-style content.

# Endpoints
## Pages
Pages are the basic unit of a FlipStream Story. They are documents that represent a single "view" in a story. Below you will find an example:
```
{
    "_updated": "Sat, 11 Aug 2018 17:19:52 GMT",
    "title": "lol2",
    "pages": [
        "5b6f1295585d02678800f93d"
    ],
    "_links": {
        "self": {
            "href": "stories/5b6f1ab8585d028051a75a98",
            "title": "page"
        },
        "collection": {
            "href": "stories?pretty=",
            "title": "stories"
        },
        "parent": {
            "href": "/",
            "title": "home"
        }
    },
    "_created": "Sat, 11 Aug 2018 17:19:52 GMT",
    "_id": "5b6f1ab8585d028051a75a98",
    "_etag": "a8994118e350727047ca571dc3a86d76640c8e87"
}
```

# Stories
Stories are collections of Pages to be viewed in sucession. You can request a story like so:
```
$ curl http://127.0.0.1:5000/stories/5b6f1ab8585d028051a75a98?pretty
{
    "_updated": "Sat, 11 Aug 2018 17:25:11 GMT",
    "title": "lol2",
    "pages": [
        "5b6f1295585d02678800f93d",
        "5b6f1070585d02676700cb43"
    ],
    "_links": {
        "self": {
            "href": "stories/5b6f1ab8585d028051a75a98",
            "title": "page"
        },
        "collection": {
            "href": "stories?pretty=",
            "title": "stories"
        },
        "parent": {
            "href": "/",
            "title": "home"
        }
    },
    "_created": "Sat, 11 Aug 2018 17:19:52 GMT",
    "_id": "5b6f1ab8585d028051a75a98",
    "_etag": "d6f7a35553d070cc5c3f6e1e1eb152b613a113ca"
```

Passing an "Embedded" clause as a query paramter to the GET request will embed the full docunment for each page in a story, so that all information needed to render a story can be retrieved in a single request:
```
$ curl 'http://127.0.0.1:5000/stories/5b6f1ab8585d028051a75a98?embedded={"pages":1}&pretty'
{
    "_updated": "Sat, 11 Aug 2018 17:25:11 GMT",
    "title": "lol2",
    "pages": [
        {
            "_updated": "Sat, 11 Aug 2018 16:45:09 GMT",
            "background_image": "http://google.com/img.png",
            "body_text": "lol body text",
            "call_to_action": {
                "url": "http://google.com",
                "text": "click me"
            },
            "_created": "Sat, 11 Aug 2018 16:45:09 GMT",
            "_id": "5b6f1295585d02678800f93d",
            "_etag": "8b1a9c55e196623ca595e942d897ef50794d26e3"
        },
        {
            "_updated": "Sat, 11 Aug 2018 16:36:00 GMT",
            "_created": "Sat, 11 Aug 2018 16:36:00 GMT",
            "_id": "5b6f1070585d02676700cb43",
            "_etag": "f3bc578a7e77f89cde1a3d310f8ce2b798395825",
            "title_text": "lol"
        }
    ],
    "_links": {
        "self": {
            "href": "stories/5b6f1ab8585d028051a75a98",
            "title": "page"
        },
        "collection": {
            "href": "stories?pretty=",
            "title": "stories"
        },
        "parent": {
            "href": "/",
            "title": "home"
        }
    },
    "_created": "Sat, 11 Aug 2018 17:19:52 GMT",
    "_id": "5b6f1ab8585d028051a75a98",
    "_etag": "d6f7a35553d070cc5c3f6e1e1eb152b613a113ca"
}
```

