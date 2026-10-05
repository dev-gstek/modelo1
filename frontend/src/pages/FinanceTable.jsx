import { useState, useEffect } from 'react';

export default function FinanceTable() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/v1/dashboard/financials/')
      .then(res => res.json())
      .then(data => {
        setOrders(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Erro ao puxar tabela:", err);
        setLoading(false);
      });
  }, []);

  const formatBRL = (value) => {
    return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
  };

  const getCanalClass = (canalName) => {
    if (!canalName) return '';
    const name = canalName.toLowerCase();
    if (name.includes('livre')) return 'canal-ml';
    if (name.includes('shopee')) return 'canal-shopee';
    if (name.includes('nuvem')) return 'canal-nuvem';
    return 'canal-wpp';
  };

  return (
    <>
      <header className="topbar">
        <div>
          <h1>DRE por Venda (Tempo Real)</h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>Conectado diretamente ao Motor Financeiro do Backend</p>
        </div>
      </header>

      <section className="content">
        <div className="table-container">
          <div className="table-header">
            <div className="filters" style={{ display: 'flex', gap: '1rem' }}>
              <input type="text" placeholder="Buscar SKU ou Pedido..." style={{ width: '250px' }} />
              <select>
                <option>Todos os Canais</option>
                <option>Mercado Livre</option>
                <option>Shopee</option>
              </select>
            </div>
            <button className="btn-export">Exportar Relatório</button>
          </div>

          <div className="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Data/Hora</th>
                  <th>Canal</th>
                  <th>Nº Pedido</th>
                  <th>Cliente</th>
                  <th>Produto (SKU)</th>
                  <th>Venda (R$)</th>
                  <th>Custo Prod.</th>
                  <th>Imposto</th>
                  <th>Caixa Gerado</th>
                  <th>Lucro Líq.</th>
                  <th>Margem %</th>
                </tr>
              </thead>
              <tbody>
                {loading && (
                    <tr><td colSpan="11" style={{textAlign:'center'}}>Carregando API...</td></tr>
                )}
                
                {!loading && orders.length === 0 && (
                    <tr><td colSpan="11" style={{textAlign:'center'}}>Nenhum pedido processado ainda. Venda algo!</td></tr>
                )}

                {orders.map(order => (
                  <tr key={order.id}>
                    <td style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>
                        {new Date(order.order_date).toLocaleString('pt-BR')}
                    </td>
                    <td>
                        <span className={`badge-canal ${getCanalClass(order.canal)}`}>{order.canal || 'N/A'}</span>
                    </td>
                    <td style={{ fontFamily: 'monospace', color: 'var(--primary)' }}>{order.external_order_id}</td>
                    <td>{order.customer_name}</td>
                    <td><strong>{order.produto_str}</strong></td>
                    <td className="money">{formatBRL(order.total_amount)}</td>
                    <td className="money text-red">- {formatBRL(order.total_product_cost)}</td>
                    <td className="money text-red">- {formatBRL(order.calculated_tax)}</td>
                    <td className="money text-green">{formatBRL(order.caixa)}</td>
                    <td className="money lucro-col text-green">{formatBRL(order.net_profit)}</td>
                    <td className="lucro-col text-green">{parseFloat(order.profit_margin).toFixed(1)}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </>
  );
}
