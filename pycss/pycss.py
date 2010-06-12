import copy

class PyCSS(object):

    @classmethod
    def parse(cls, node, parents = None):
        result = []
        nodes_to_parse = []

        if parents:
            result.append("%s { " % " ".join(parents))
        else:
            parents = []

        for key, value in node.items():
            if value.__class__.__name__ in ('str', 'unicode'):
                result.append('%s: %s; ' % (key, value))
            elif value.__class__.__name__ == 'function':
               result.append('%s: %s; ' % (key, value()))
            elif value.__class__.__name__ == 'dict':
                nodes_to_parse.append((key, value))
        if result:
            result.append("}\n")

        for n in nodes_to_parse:
            result.append(PyCSS.parse(n[1], [p for p in parents] + [n[0]]))

        # end of branch?
        end = True
        for value in node.values():
            if value.__class__.__name__ not in ('str', 'unicode') and value.__class__.__name__ != 'function':
                end = False
                break
        if end:
            parents.pop()

        return "".join(result)
