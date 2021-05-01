#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .order import Order
from .subproduct import Subproduct
from .product import Product
from sys import stderr
import json


class TroveOrder(Order):

    TROVE_GAMEKEY = "Humble-trove-games"

    def __init__(self, trove_data_element, hapi):
        """
            Parameterized constructor for the Order object.

            :param trove_page_html_text: The plain text/html page of the humble trove
            :param hapi: humble bundle api handle. Used to read the trove dummy gamekey and signing URL.
        """

        super(Order, self).__init__(trove_data_element)

        subproducts = []
        
        for trove_data in trove_data_element:
            product = {'human_name': trove_data['human-name'],
                       'machine_name': trove_data['machine_name'],
                       'downloads': [],
                       'payee': {}  # TODO: put something better here
                       }
            for platform, platform_data in trove_data['downloads'].items():
                pp = dict()
                pp['platform'] = platform
                pp['download_identifier'] = platform_data['url']['web']
                pp['machine_name'] = platform_data['machine_name']
                signed = hapi.get_signed_trove_url(pp['machine_name'], pp['download_identifier'])
                pp['download_struct'] = [{
                    'url': {
                        'web': signed.get('signed_url', None),
                        'bittorrent': signed.get('signed_torrent_url', None)
                    },
                    'file_size': platform_data.get('file_size'),
                    'human_size': platform_data.get('size'),
                    'md5': platform_data.get('md5'),
                    'sha1': platform_data.get('sha1')
                }]
                pp['options_dict'] = None  # TODO: What is this?
                product['downloads'].append(pp)
            subproducts.append(Subproduct(product))  # TODO: check that the data formats actually match

        self.subscriptions = None
        self.created = None
        self.amount_to_charge = None
        self.gamekey = TroveOrder.TROVE_GAMEKEY
        self.subproducts = subproducts

        product_data = {
            'human_name': 'Humble Trove Games',
            'machine_name': 'trove_games',
            'category': 'trove'
        }
        self.product = Product(product_data)
