Quick Start Guide
=================

This guide is intended to give users a basic idea of Fusion Python SDK usage
through examples.


Before You Begin
----------------

You should already have the Pure Storage Fusion Python SDK installed.

This includes installing the  package dependencies.

See :doc:`installation` for more information.


Example: Creating a Tenant
------------------

To verify the Fusion Python SDK package is installed and importable, try executing
the following in a Python interpreter:

.. code-block:: python

    >>> import fusion


If that succeeds without an ImportError, you are ready to start using the
Fusion Python SDK.

In order to run some example code, import these as well:

.. code-block:: python

    >>> import time
    >>> from fusion.rest import ApiException
    >>> from pprint import pprint

We will need to do the following for authentication purposes as well:

.. code-block:: python

    >>> configuration = fusion.Configuration()
    >>> configuration.private_key_file='<path-to-private-key.pem>'
    >>> configuration.issuer_id='<your-issuer-id>'
    >>> configuration.token_endpoint = '<your-token-endpoint>'
    >>> configuration.host="<your-host>"

Now, we will need to create an instance of the API Client: we will use this to call the API.

.. code-block:: python

    >>> api_instance = fusion.TenantsApi(fusion.ApiClient(configuration))

The next step is to make the request body and send the POST request.

.. code-block:: python

    body = fusion.TenantPost(name="t") # TenantPost | 

    try:
        # Creates a Tenant.
        api_response = api_instance.create_tenant(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenantsApi->create_tenant: %s\n" % e)

Now, we should get a returned operation which is something that the caller can wait on
for any next steps. You can find examples of waiting for an operation in our examples on Github.
