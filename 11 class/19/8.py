def game(k, s, step):
    if k+s>=45:
        return step % 2 == 0
    if step == 0:
        return 0
    h = [game(k, s + 2, step - 1), game(k, s*3, step - 1), game(k*3, s, step - 1), game(k+2, s, step - 1)]
    return any(h) if (step - 1) % 2 == 0 else all(h)
print('19', len([(k,s) for s in range(1, 44) for k in range(1,44) if game(k,s,2) and k+s <=43]))
