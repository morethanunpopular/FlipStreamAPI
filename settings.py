#Global Settings
XML = False
DEBUG = True
X_DOMAINS = [ "http://127.0.0.1:5000"]
X_HEADERS = [ "Origin", "X-Requested-With", "Content-Type", "Accept", "Authorization", "If-Match" ]
#Database Settings
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'flipstream'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Page Schema
page_schema = {
  'title_text': {
    'type': 'string',
    'minlength': 1,
    'maxlength': 100,
    'required': False,
  },
  'body_text': {
    'type': 'string',
    'minlength': 1,
    'maxlength': 100,
    'required': False,
  },
  'footer_text': {
    'type': 'string',
    'minlength': 1,
    'maxlength': 100,
    'required': False,
  },
  'call_to_action': {
     'type': 'dict',
     'schema': {
       'text': {'type': 'string', 'required': True},
       'url': {'type': 'string', 'required': True}
     },
     'required': False
   },
   'background_image': {
      'type': 'string',
      'required': False
    },
}
page = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'page',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': page_schema
}

story_schema = {
  "title": {
    "type": "string",
    "required": True
  },
  "pages": {
    "type": "list", 
    "schema": {
      "type": "objectid",
      'data_relation': {
        'resource': 'pages',
        'field': '_id',
        'embeddable': True
      }
    }
  }
}
story = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'page',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': story_schema
}

DOMAIN = {
  'pages': page,
  'stories': story
}
