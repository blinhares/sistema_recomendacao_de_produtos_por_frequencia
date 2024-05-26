import random
import pandas as pd
import matplotlib.pyplot as plt

class RecomendaProdutos:
    def __init__(self) -> None:
        self._list_produtos = [
            'arroz',
            'feijão',
            'macarrão',
            'carne',
            'frango',
            'banana',
            'maçã',
            'cerveja',
            'refrigerante',
            'água',
        ]
        self._num_max_itens:int = int(len(self._list_produtos)/2)
        self._num_carrinhos:int = 500
        self._compras_df = pd.DataFrame()
        self._criar_compras_df()
        self._gerar_amostras()

    @property
    def list_produtos(self):
        '''Retorna a lista de produtos'''
        return self._list_produtos
    @list_produtos.setter
    def list_produtos(self, list_produtos:list[str]):
        '''Define a lista de produtos'''
        self._list_produtos = list_produtos
        self.num_max_itens = int(len(self._list_produtos)/2)
    
    @property
    def num_max_itens(self):
        '''Retorna o número máximo de itens dentro de cada carrinho'''
        return self._num_max_itens
    @num_max_itens.setter
    def num_max_itens(self,num_max_itens:int):
        '''Define o número máximo de itens dentro de cada carrinho.
        O num_max_itens deve ser menor que o comprimento da lista de itens
        Se num_max_itens = 5, cada carrinho de compra tera no máximo 5 itens'''
        if num_max_itens > len(self._list_produtos)/2:
            raise ValueError(
                'O número máximo de itens deve ser menor número de produtos dividido por 2')
        self._num_max_itens = num_max_itens
        #redefine DataFrame
        self._criar_compras_df()

    @property
    def num_carrinhos(self):
        '''Retorna o numero de carrinhos que vao ser gerados'''
        return self._num_carrinhos
    @num_carrinhos.setter
    def num_carrinhos(self, num_carrinhos:int):
        '''Define o numero de carrinhos que vao ser gerados'''
        self._num_carrinhos = num_carrinhos
        self._criar_compras_df()
        
    def _criar_compras_df(self):
        '''Cria o DataFrame de compras com numero de colunas igual a
        @num_max_itens'''
        self._compras_df = pd.DataFrame(
            columns=range(1,self._num_max_itens + 1))

    def _gera_carrinho(self):
        '''Gera um carrinho de compras aleatório nom número de itens igual
        num_max_itens sem itens repetidos'''
        return random.sample(
            self._list_produtos,
            k=self._num_max_itens)
    
    def _add_to_compras_df(self, carrinho:list[str], _index:int=0):
        '''Adiciona um carrinho de compras ao DataFrame de compras'''
        df = pd.DataFrame(data=[carrinho],
                          index=[_index],
                          columns=range(
                              1,self._num_max_itens + 1))
        self._compras_df = pd.concat([ #type:ignore
            self._compras_df,
            df
            ])

    def _gerar_amostras(self):
        '''Gera uma lista de carrinhos (de tamanho igual a @num_carrinhos) de
          compras aleatórios com o número de itens igual a determinado adiciona
          ao DataFrame de compras'''
        for i in range(self._num_carrinhos):
            carrinho = self._gera_carrinho()
            self._add_to_compras_df(carrinho,
                                   _index=i)
    
    def _is_produto_valido(self, produto:str):
        '''Verifica se o produto é válido'''
        return produto in self._list_produtos

    def _filtrar_compras_por_produtos(self, produtos:list[str]):
        '''Filtrar o DataFrame de compras eliminando as linhas que nao
         contem nenhum dos produtos listados'''
        
        _compras_df_filtered = self._compras_df.copy()
        for produto in produtos:
            if not self._is_produto_valido(produto):
                raise ValueError(f'O valor {produto} não é um produto valido')

            linhas_que_contem:list[bool] = (
                _compras_df_filtered. 
                isin([produto]). # type:ignore - Cria DF com boleano onde o termo foi encontrado
                any(axis=1). # transforma em lista onde um dos valores for True
                        values) #type:ignore
            _compras_df_filtered = _compras_df_filtered.loc[
                linhas_que_contem]
        return _compras_df_filtered
    
    def retornar_sujestoes(self,produtos:list[str]):
        '''Retorna uma lista de produtos sugeridos para compra dado a lista
        de produtos fornecidas'''
        df_filtrado = self._filtrar_compras_por_produtos(produtos)
        df = pd.DataFrame()
        for column in df_filtrado.columns:
            df = pd.concat([  # type: ignore
                    df,
                    df_filtrado.value_counts(subset=column)])
        df.reset_index(inplace=True)
        df = (
            df.groupby(['index']). # type: ignore - agrupa os valores por nome produto
            sum()) # type: ignore
        
        for produto in produtos:
            df.drop(labels=produto,axis=0, inplace=True) # type: ignore
        nome_coluna = '%'
        df.rename(columns={'count':nome_coluna},
                  inplace=True)
        df.index.rename('Produto',
                  inplace=True)
        df.sort_values(by=nome_coluna,ascending=False, inplace=True)
        
        return df*100/df.sum()
        
        


if __name__ == '__main__':
        

    p1 = RecomendaProdutos()
    produtos_buscados = ['arroz']
    df=p1.retornar_sujestoes(produtos_buscados)
    print(df.sort_values(by='%',ascending=False))
    # df.plot.bar()
    # plt.show()

    
    



