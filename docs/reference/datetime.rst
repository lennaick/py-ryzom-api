RyzomDate
=========

.. py:class:: ryzomapi.RyzomDate(tick=None)

   :param tick: the server tick, or the current one if not specified
   :type tick: int


Methods
-------

   .. py:method:: ryzomapi.RyzomDate.locale(locale)

      :param locale: the locale to use to display the date
      :type locale: str


Examples
--------

Displaying the current date in various languages:

.. code-block:: python

   from ryzomapi import RyzomDate

   dt = RyzomDate()
   print(dt) # defaut: en
   print(dt.locale('fr'))
   print(dt.locale('de'))


Displaying a specific server tick:

.. code-block:: python

   from ryzomapi import RyzomDate

   dt = RyzomDate(541327147)
   print(dt)
