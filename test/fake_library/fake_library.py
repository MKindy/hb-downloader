#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__license__ = "MIT"

from glob import iglob
import httpretty
from os import path


class FakeLibrary:

    gamekeys_list = []
    local_path = ""

    def __init__(self, hapi):
        self.local_path = path.dirname(__file__)
        self.update_gamekeys(hapi)
        self.prepare_fake_answer_list_gamekeys(hapi)
        self.prepare_fake_answers_keys(hapi)
        self.prepare_fake_answer_trove(hapi)

    def update_gamekeys(self, hapi):
        self.gamekeys_list = []
        for filename in iglob(path.join(self.local_path, "*.key")):
            self.gamekeys_list.append(path.basename(filename)[0:-4])
        self.gamekeys_list.append(hapi.TROVE_GAMEKEY)

    def prepare_fake_answer_trove(self, hapi):
        httpretty.register_uri(
            httpretty.GET,
            hapi.TROVE_PAGE_URL,
            self.readfile("trove.html")
        )
        httpretty.register_uri(
            httpretty.POST,
            hapi.TROVE_SIGN_URL,
            self.readfile("sign_answer_OK.json")
        )

    def prepare_fake_answers_keys(self, hapi):
        for key in self.gamekeys_list[0:-1]:
            httpretty.register_uri(
                httpretty.GET,
                hapi.ORDER_URL.format(order_id=key),
                body=self.get_answer_for(key)
            )

    def get_answer_for(self, key):
        return self.readfile(key + ".key")

    def prepare_fake_answer_list_gamekeys(self, hapi):
        string = "[\n"
        for key in self.gamekeys_list[:-1]:  # Skip the trove key, as it is not reported by the API
            string = string + '{\n"gamekey":"' + key + '"\n},\n'
        if len(self.gamekeys_list) > 1:  # Trove does not count, as we skipped it
            string = string[:-2] + '\n]'
        else:
            string = string + '\n]'
        httpretty.register_uri(
            httpretty.GET,
            hapi.ORDER_LIST_URL,
            body=string
        )

    def readfile(self, relative_path):
        abs_path = path.join(self.local_path, relative_path)
        file = open(abs_path, "r")
        text = file.read()
        file.close()
        return text
