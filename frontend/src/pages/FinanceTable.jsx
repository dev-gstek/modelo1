export default function FinanceTable() {
  return (
    <>
      <header className="topbar">
        <div>
          <h1>DRE por Venda (Tempo Real)</h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>Tabela com 12 indicadores financeiros</p>
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
                  <th>Taxas/Frete</th>
                  <th>Custo Prod.</th>
                  <th>Imposto</th>
                  <th>Caixa Gerado</th>
                  <th>Lucro Líq.</th>
                  <th>Margem %</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>01/10/26 14:30</td>
                  <td><span className="badge-canal canal-ml">Mercado Livre</span></td>
                  <td style={{ fontFamily: 'monospace', color: 'var(--primary)' }}>#ML-99281</td>
                  <td>João Silva</td>
                  <td><strong>Caneca Mágica</strong><br/><span style={{ fontSize: '0.75rem', color: '#9CA3AF' }}>SKU: CAN-MAG-01</span></td>
                  <td className="money">45,00</td>
                  <td className="money text-red">- 8,50</td>
                  <td className="money text-red">- 12,00</td>
                  <td className="money text-red">- 2,70</td>
                  <td className="money">36,50</td>
                  <td className="money lucro-col text-green">R$ 21,80</td>
                  <td className="lucro-col text-green">48,4%</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </>
  );
}
