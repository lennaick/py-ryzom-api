.. _guild:

Guild
=====

.. py:class:: ryzomapi.Guild(api_key=None, from_file=None)

   :param api_key: the guild's api key
   :type api_key: str
   :param from_file: xml file name containing the guild's data
   :type from_file: str

   .. note::
      The from_file parameter is intended for unit testing purposes only, you should not use it in your applications.

   .. py:attribute:: ryzomapi.Guild.id

      (int) the guild's id

   .. py:attribute:: ryzomapi.Guild.gid

      (int) Alias for `id`

   .. py:attribute:: ryzomapi.Guild.name

      (str) the guild's name

   .. py:attribute:: ryzomapi.Guild.race

      (str) the guild's race

   .. py:attribute:: ryzomapi.Guild.icon

      (str) Guild icon id

   .. py:attribute:: ryzomapi.Guild.description

      (str) the guild's description

   .. py:attribute:: ryzomapi.Guild.creation_date

      (:ref:`ryzomdate`) the guild's creation date

   .. py:attribute:: ryzomapi.Guild.shard

      (str) the guild's shard

   .. py:attribute:: ryzomapi.Guild.motd

      (str) the guild's message of the day

   .. py:attribute:: ryzomapi.Guild.money

      (int) number of dappers owned by the guild

   .. py:attribute:: ryzomapi.Guild.members

      (list) list of :ref:`GuildMember <guildmember>`

   .. py:method:: ryzomapi.Guild.icon_link(size='b', escape_url=False)

      :param size: icon's size ('s' for small, 'b' for big)
      :type size: str
      :param escape_url: whether the returned url should be escaped or not
      :type escape_url: bool
      :return: link to the guild's icon

   .. py:staticmethod:: ryzomapi.Guild.list_all(from_file=None)

      :param from_file: xml file name containing the guild's data
      :type from_file: str
      :return: the list of every existing guilds

      .. note::
         The from_file parameter is intended for unit testing purposes only, you should not use it in your applications.


.. _guildmember:

.. py:class:: ryzomapi.GuildMember()

   .. py:attribute:: ryzomapi.Guild.name

      (str) character's name

   .. py:attribute:: ryzomapi.Guild.grade

      (str) character's grade

   .. py:attribute:: ryzomapi.Guild.joined

      (:ref:`ryzomdate`) character's joined date
