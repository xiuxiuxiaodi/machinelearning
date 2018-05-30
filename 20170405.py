class TextProcessor(object):
    PLUGINS={}

    def process(self,text,plugins=()):
        if plugins is ():
            for plugins_names in self.PLUGINS.keys():
                text=self.PLUGINS[plugins_names]().process(text)
        else:
            for plugins_names in plugins:
                text=self.PLUGINS[plugins_names]().process(text)
        return text

    @classmethod
    def plugin_register(cls,plugin_names):
        def wrapper(plugin):
            cls.PLUGINS.update({plugin_names:plugin})
            return plugin
        return wrapper

@TextProcessor.plugin_register('plugin1')
class CleanMarkdownBolds(object):
    def process(self,text):
        return text.replace("**","")
if __name__=="__main__":
    processor=TextProcessor()
    print processor.PLUGINS
    processed1=processor.process(text="**foo bar**",plugins=("plugin1",))
    processed2=processor.process(text="** foo bar**")
    print processed1
