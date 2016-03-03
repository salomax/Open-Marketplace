#!/usr/bin/env python
# coding: utf-8
#
# Copyright 2016, Marcos Salomão.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from protorpc import messages
from protorpc import message_types


__author__ = "Marcos Salomão"
__email__ = "salomao.marcos@gmail.com"
__copyright__ = "Copyright 2016, Marcos Salomão"
__license__ = "Apache 2.0"


class ProductKeyMessage(messages.Message):
    """ GET message for key product.
    """
    id = messages.IntegerField(1)


class ProductGetMessage(messages.Message):
    """ GET message for product.
    """

    id = messages.IntegerField(1)

    code = messages.StringField(2, required=True)

    name = messages.StringField(3, required=True)

    created_date = message_types.DateTimeField(4, required=True)


class ProductPostMessage(messages.Message):
    """ POST message for product. 
    """

    id = messages.IntegerField(1)

    code = messages.StringField(2, required=True)

    name = messages.StringField(3, required=True)


class ProductSearchMessage(messages.Message):
    """ POST message for search product.
    """

    code = messages.StringField(1, required=False)

    name = messages.StringField(2, required=False)


class ProductCollectionMessage(messages.Message):
    """ Products collection.
    """

    items = messages.MessageField(ProductGetMessage, 1, repeated=True)
