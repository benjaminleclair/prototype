import sys
sys.path.append("..")
from nologic.base import state_selector


def base_case():

    def _inner(lis):
        return [lis]
       
    return (False, _inner)


def recurse_case():

    def _concat(e, perms):
        for p in perms:
            for i in range(len(p)+1):
                yield p[:i] + [e] + p[i:]

    def _inner(lis):
        head, tail = lis[0], lis[1:]
        perms = permute(tail)
        result = list(_concat(head, perms))
        return result

    return (True, _inner)


def permute(lis):

    s = len(lis) > 1
    f = state_selector(s, [base_case, recurse_case])
    return f(lis)


if __name__ == '__main__':

    print(permute([1,2,3]))
