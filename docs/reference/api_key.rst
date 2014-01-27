APIKey
======

.. py:class:: ryzomapi.APIKey(api_key, key_type=None)

   :param api_key: the api key
   :type api_key: str
   :param key_type: the api key type
   :type key_type: str

Attributes
----------

   .. py:method:: checkType(key_type)

      :param key_type: the type the api key will be checked against
      :type key_type: str

Examples
--------

Displaying API keys type:

.. code-block:: python

   from ryzomapi import APIKey

   for key_str in ('c0dc2d9a66e656042789abf68704a3d24b54a36b3', 'g0dc2d9a66e656042789abf68704a3d24b54a36b3'):
       k = APIKey(key_str)
       for t in ('guild', 'character'):
           if k.checkType(t):
               print("%s is a %s API Key" % (k, t))

Displaying whether API keys are valid guild API keys or not:

.. code-block:: python

   from ryzomapi.exceptions import InvalidAPIKeyException
   from ryzomapi import APIKey

   for key_str in ('qwerty', 'g0dc2d9a66e656042789abf68704a3d24b54a36b3', '', 'c0dc2d9a66e656042789abf68704a3d24b54a36b3'):
       try:
           APIKey(key_str, 'guild')
           print('%s is a valid guild API Key' % key_str)
       except InvalidAPIKeyException:
           print('%s is an invalid guild API Key' % key_str)
