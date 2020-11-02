#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "45a456d1-bc01-4df8-8b53-fee8e55c6394")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "-IeQ2JFi.fL4x_8R42XA6DvV._3IWRKLWD")
