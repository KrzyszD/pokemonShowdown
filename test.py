import pickle
import Simulator.pokemon

if __name__ == "__main__":
        
    f = open("ms.pkl", "rb")
    ms = pickle.load(f)
    f.close()

    for p in ms.team1.active:
        print(vars(p))
    print()
    for p in ms.team1.full:
        print(p.name)
    print()
    for p in ms.team2.active:
        print(vars(p))
    print()
    for p in ms.team2.full:
        print(p.name)
        