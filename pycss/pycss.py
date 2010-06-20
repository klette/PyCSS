
class PyCSS(object):

    @classmethod
    def parse(cls, startnode, parents = None):
        result = []
        nodes_to_parse = [([], startnode)]

        while nodes_to_parse:
            parents, node = nodes_to_parse.pop(0)
            if parents:
                result.append("%s { " % " ".join(parents))
            else:
                parents = []

            for key, value in node.iteritems():
                if value.__class__.__name__ in ('str', 'unicode'):
                    result.append('%s: %s; ' % (key, value))
                elif value.__class__.__name__ == 'function':
                   result.append('%s: %s; ' % (key, value()))
                elif value.__class__.__name__ == 'dict':
                    nodes_to_parse.append(([p for p in parents ] + [key], value))
            if result:
                result.append("}\n")

        return "".join(result)
