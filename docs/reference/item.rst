.. _item:

Item
====

.. py:class:: ryzomapi.Item(sheetid=None, xml=None)

   :param sheetid: the item sheet id
   :type sheetid: str
   :param xml: the item sheet id
   :type xml: XML Element Node

   .. py:attribute:: ryzomapi.Item.sheet

      (str) The sheet id, without .sitem

   .. py:method:: ryzomapi.Item.icon_url(escape_url=False)

      :param escape_url: whether the returned url should be escaped or not
      :type escape_url: bool
      :return: the item's icon url


Item comparison
---------------

It is possible to compare items using the common comparison operators. This comparison is based on the in-game display order.
