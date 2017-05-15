fobi.contrib.themes.simple
--------------------------
A ``django-fobi`` theme in a style of Django admin. Relies on Django-admin
and some jQuery UI only.

jQuery UI "Django" theme comes from `here
<http://jqueryui.com/themeroller/#!zThemeParams=5d000001004406000000000000003d8888d844329a8dfe02723de3e5702531794cd29e6ed19a93500bec10499630a65410e41ead4c600a0cf20b340bb5e2f7caf959ed396c92b6035d90d24df6690df466ac448d4e1c19e7fa7c9a0839be4194bf063920ea1af50a8118ad9351aef9ad563b3a37cd36e7495624fe90fc1dea5e04da5c3bc1b05fbaabd52118818b56bf553915a91d00d5f3e6d7170d10432c322c435542e105860d86f5aff187d2c5fd576473852b0a11341f0f25f44acc20995011eacc757f738992c953dbc7a1465ffdb121cb5442e4eab396fc706de223fe0fc9c95a7d117899db8aa67ebf8d5b547778d8301f54035188d6f909c525eba7227394e77fa275211eca51b9a828c4266d31e94e9ad9d094e2d5313fc059abfb69532833a14287184b79fd3e769e36246d5f0b3f8fb23a589e0ce916bb6b074faf8dbac4a8f379a481f14755e3043f7a684ccde3630e138ed0ed7e0e4af40517ffcf11fd3581d7da611c79f6481f3e02d2d1645c776ada5da686c7e62ad51e829cf9ba6ec42e0a7afa3dcaed299f70bd4a28055aa8c0f6d9d1d5f362280aff2c9be5d5355c0e15c5145565ac449331112dd272ba1c7f326f3502465763e229cdc80dec6054935a2c4ef8b62e3f00a7bee54e59377abda70f8f3fbd15004573b3372aaddd79545e195b14abddcb8dc730dc65504265aece22ee6158670dbc2d11f314ffebbc5e3d>`_.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.themes.simple`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.themes.simple',
            # ...
        )

(2) Specify ``simple`` as a default theme in your ``settings.py``:

    .. code-block:: python

        FOBI_DEFAULT_THEME = 'simple'
