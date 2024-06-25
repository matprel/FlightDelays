import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._allAeroporti = DAO.getAllAirports()
        self._idMap = {}
        for a in self._allAeroporti:
            self._idMap[a.ID] = a

    def buildGraph(self, min):
        nodi = DAO.getAllNodes(min, self._idMap)
        self._grafo.add_nodes_from(nodi)

        allConnessioni = DAO.getAllEdgesV1(self._idMap)
        for c1 in allConnessioni:
            for c2 in allConnessioni:
                if c1.a1.ID == c2.a2.ID and c1.a2.ID == c2.a1.ID:
                    self._grafo.add_edge(c1.a1,c2.a1, weight = c1.n+c2.n)

    def cercaPercorso(self, AeroportoPartenza, AeroportoArrivo):
        percorso = nx.dijkstra_path(self._grafo, source=AeroportoPartenza, target=AeroportoArrivo)
        return percorso

    def getAllNodi(self):
        return self._grafo.nodes()

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

