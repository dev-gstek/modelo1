import { useState, useEffect } from 'react';
import {
  Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, 
  BarElement, Title, Tooltip, Legend, ArcElement
} from 'chart.js';
import { Line, Doughnut } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale, LinearScale, PointElement, LineElement, 
  BarElement, Title, Tooltip, Legend, ArcElement
);

ChartJS.defaults.font.family = "'Outfit', sans-serif";
ChartJS.defaults.color = '#6B7280';

export default function Dashboard() {
  const [metrics, setMetrics] = useState({
    total_revenue: 0,
    net_profit: 0,
    total_orders: 0,
    avg_margin: 0
  });
  
  const [loading, setLoading] = useState(true);

  // Estados vazios aguardando a API
  const [lineData, setLineData] = useState({
    labels: [],
    datasets: []
  });

  const [doughnutData, setDoughnutData] = useState({
    labels: [],
    datasets: []
  });

  useEffect(() => {
    // Busca na API do Django
    fetch('http://localhost:8000/api/v1/dashboard/financials/')
      .then(res => res.json())
      .then(data => {
        // Agrupa os KPIs gerais a partir dos pedidos que vieram do backend
        let revenue = 0;
        let profit = 0;
        
        // Separa faturamento por canal para o gráfico Doughnut
        const canaisDict = {};

        // Para simplificar o gráfico de linha, vamos usar as próprias datas dos pedidos
        const labelsLinha = [];
        const receitaLinha = [];
        const lucroLinha = [];

        data.forEach(order => {
            const valVenda = parseFloat(order.total_amount);
            const valLucro = parseFloat(order.net_profit);
            
            revenue += valVenda;
            profit += valLucro;

            const canalName = order.canal || 'Outros';
            canaisDict[canalName] = (canaisDict[canalName] || 0) + valVenda;

            // Pega dia/mes para o grafico
            const dateStr = new Date(order.order_date).toLocaleDateString('pt-BR', {day:'2-digit', month:'short'});
            labelsLinha.push(dateStr);
            receitaLinha.push(valVenda);
            lucroLinha.push(valLucro);
        });

        // Atualiza Cards
        setMetrics({
          total_revenue: revenue,
          net_profit: profit,
          total_orders: data.length,
          avg_margin: revenue > 0 ? (profit / revenue) * 100 : 0
        });

        // Monta Gráfico de Donuts
        setDoughnutData({
          labels: Object.keys(canaisDict),
          datasets: [{
            data: Object.values(canaisDict),
            backgroundColor: ['#FBBF24', '#F97316', '#3B82F6', '#22C55E'],
            borderWidth: 0,
          }]
        });

        // Monta Gráfico de Linha (Pega os ultimos pedidos revertidos cronologicamente)
        setLineData({
          labels: labelsLinha.reverse().slice(-10), // Ultimos 10 periodos
          datasets: [
            {
              label: 'Venda Bruta (R$)',
              data: receitaLinha.reverse().slice(-10),
              borderColor: '#4F46E5',
              backgroundColor: 'rgba(79, 70, 229, 0.1)',
              borderWidth: 3, fill: true, tension: 0.4
            },
            {
              label: 'Lucro Líquido (R$)',
              data: lucroLinha.reverse().slice(-10),
              borderColor: '#10B981',
              backgroundColor: 'rgba(16, 185, 129, 0.1)',
              borderWidth: 3, fill: true, tension: 0.4
            }
          ]
        });

        setLoading(false);
      })
      .catch(err => {
        console.error("Erro ao puxar dados da API:", err);
        setLoading(false);
      });
  }, []);

  return (
    <>
      <header className="topbar">
        <div>
          <h1>Business Intelligence</h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>Visão consolidada da operação multicanal (Conectado com API)</p>
        </div>
      </header>

      <section className="content">
        {loading ? (
            <div style={{ textAlign: 'center', padding: '3rem' }}>Conectando com Motor Financeiro (Django)...</div>
        ) : (
            <>
                <div className="kpi-grid">
                <div className="kpi-card bordered">
                    <div className="kpi-title">Faturamento Bruto</div>
                    <div className="kpi-value">
                      {new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(metrics.total_revenue)}
                    </div>
                </div>
                <div className="kpi-card bordered success">
                    <div className="kpi-title">Lucro Líquido Real</div>
                    <div className="kpi-value" style={{ color: 'var(--success)' }}>
                      {new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(metrics.net_profit)}
                    </div>
                </div>
                <div className="kpi-card bordered wpp">
                    <div className="kpi-title">Margem de Lucro Média</div>
                    <div className="kpi-value">{metrics.avg_margin.toFixed(1)}%</div>
                </div>
                <div className="kpi-card bordered shopee">
                    <div className="kpi-title">Volume de Pedidos</div>
                    <div className="kpi-value">{metrics.total_orders}</div>
                </div>
                </div>

                <div className="charts-grid">
                <div className="chart-card">
                    <div className="chart-header">
                    <div className="chart-title">Evolução: Venda Bruta x Lucro Líquido</div>
                    </div>
                    <div className="chart-container">
                    <Line data={lineData} options={{ responsive: true, maintainAspectRatio: false }} />
                    </div>
                </div>
                <div className="chart-card">
                    <div className="chart-header">
                    <div className="chart-title">Faturamento por Canal</div>
                    </div>
                    <div className="chart-container">
                    {doughnutData.labels.length > 0 ? (
                        <Doughnut data={doughnutData} options={{ responsive: true, maintainAspectRatio: false, cutout: '70%' }} />
                    ) : (
                        <div style={{ textAlign:'center', marginTop:'80px', color:'#9ca3af' }}>Sem vendas registradas</div>
                    )}
                    </div>
                </div>
                </div>
            </>
        )}
      </section>
    </>
  );
}
