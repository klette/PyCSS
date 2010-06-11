import copy

class PyCSS(object):

    @classmethod
    def parse(cls, code):
        result = ''
        result += PyCSS._node_to_string(code, [])
        return result


    @classmethod
    def _node_to_string(cls, node, parents):
        result = ''
        nodes_to_parse = []

        if parents:
            result += "%s { " % " ".join(parents)

        for key, value in node.items():
            if isinstance(value, basestring):
                result += '%s: %s; ' % (key, value)
            elif isinstance(value, type(lambda: 1)):
               result += '%s: %s; ' % (key, value())
            elif isinstance(value, dict):
                nodes_to_parse.append((key, value))
        if result:
            result += "}\n"

        if result.endswith('{ }\n'):
            result = ''


        for n in nodes_to_parse:
            d_parents = copy.copy(parents)
            d_parents.append(n[0])
            result += PyCSS._node_to_string(n[1], d_parents)

        # end of branch?
        end = True
        for value in node.values():
            if not isinstance(value, basestring):
                end = False
                break
        if end:
            parents.pop()

        return result
