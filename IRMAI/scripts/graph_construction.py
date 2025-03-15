from py2neo import Graph, Node, Relationship
from scripts.data_collection import load_data

# Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "neo4j"))

def create_graph(data):
    """
    Create a graph in Neo4j using the FX trade data.
    """
    for index, row in data.iterrows():
        # Create a node for each trade
        trade = Node("Trade", 
                     timestamp=row.name,  # Use the index (timestamp) as the trade ID
                     open=row['open'], 
                     high=row['high'], 
                     low=row['low'], 
                     close=row['close'])
        graph.create(trade)

        # Create relationships (e.g., consecutive trades)
        if index > 0:
            prev_trade = graph.nodes.match("Trade", timestamp=data.index[index-1]).first()
            rel = Relationship(prev_trade, "NEXT", trade)
            graph.create(rel)

# Example usage
if __name__ == "__main__":
    file_path = "../data/fx_trades.csv"
    fx_data = load_data(file_path)
    fx_data=fx_data.dropna()
    create_graph(fx_data)
    print("Graph construction completed!")