Character
=========

.. py:class:: ryzomapi.character.Character(api_key=None, from_file=None)

   :param api_key: the character's api key
   :type api_key: str
   :param from_file: xml file name containing the character's data
   :type from_file: str

   .. note::
      The from_file parameter is intended for unit testing purposes only, you should not use it in your applications.

   .. py:attribute:: id

      (int) The character's id.

   .. py:attribute:: name

      (string) The character's name.

   .. py:attribute:: shard

      (string) The shard's name.

   .. py:attribute:: race

      (string) The character's race.

   .. py:attribute:: gender

      (string) The character's gender.


Examples
--------

Displaying basic informations:

.. code-block:: python

   from ryzomapi.character import Character

   c = Character('cf2a0ac0a6024b0b42c62149609500eab317ffb75')
   print(c.name)
   if c.race:
       print("My name is %(name)s and I'm a %(race)s." % c.__dict__)

