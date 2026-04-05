# -*- coding: UTF-8 -*-
from Plugins.Plugin import PluginDescriptor
from importlib import reload
from . import netzkino


def main(session, **kwargs):
    reload(netzkino)
    session.open(netzkino.netzkino)


def Plugins(**kwargs):
    return PluginDescriptor(name="NetzKino", description="Netzkino Plugin", where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU], icon="logo.png", fnc=main)
