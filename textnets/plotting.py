import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def set_chinese_font():
    try:
        plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
        plt.rcParams['axes.unicode_minus'] = False
    except:
        try:
            plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac
        except:
            plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # Linux

def plot_network(network, **kwargs):
    set_chinese_font()
    
    # Adjust node spacing for Chinese characters
    kwargs.setdefault('node_size', 800)
    kwargs.setdefault('font_size', 10)
    kwargs.setdefault('width', 0.5)
    
    # Original plotting code with Chinese support
    pos = nx.spring_layout(network, k=0.15, iterations=50)
    nx.draw_networkx_nodes(network, pos, **kwargs)
    nx.draw_networkx_edges(network, pos, alpha=0.2, **kwargs)
    
    # Improved Chinese label drawing
    labels = {n: n for n in network.nodes()}
    nx.draw_networkx_labels(
        network, pos, labels,
        font_family=plt.rcParams['font.sans-serif'][0],
        **kwargs
    )
