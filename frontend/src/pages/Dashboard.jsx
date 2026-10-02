import {
  Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, 
  BarElement, Title, Tooltip, Legend, ArcElement
} from 'chart.js';
import { Line, Doughnut, Bar, Pie } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale, LinearScale, PointElement, LineElement, 
  BarElement, Title, Tooltip, Legend, ArcElement
);

ChartJS.defaults.font.family = "'Outfit', sans-serif";
ChartJS.defaults.color = '#6B7280';

export default function Dashboard() {
  const lineData = {
    labels: ['Dia 1', 'Dia 5', 'Dia 10', 'Dia 15', 'Dia 20', 'Dia 25', 'Hoje'],
    datasets: [
      {
        label: 'Venda Bruta (R$)',
        data: [4000, 4200, 5100, 4800, 6000, 5800, 6500],
        borderColor: '#4F46E5',
        backgroundColor: 'rgba(79, 70, 229, 0.1)',
        borderWidth: 3,
        fill: true,
        tension: 0.4
      },
      {
        label: 'Lucro Líquido (R$)',
        data: [1600, 1750, 2200, 2050, 2600, 2500, 2800],
        borderColor: '#10B981',
        backgroundColor: 'rgba(16, 185, 129, 0.1)',
        borderWidth: 3,
        fill: true,
        tension: 0.4
      }
    ]
  };

  const doughnutData = {
    labels: ['Mercado Livre', 'Shopee', 'NuvemShop', 'WhatsApp'],
    datasets: [{
      data: [45, 30, 15, 10],
      backgroundColor: ['#FBBF24', '#F97316', '#3B82F6', '#22C55E'],
      borderWidth: 0,
    }]
  };

  return (
    <>
      <header className="topbar">
        <div>
          <h1>Business Intelligence</h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>Visão consolidada da operação multicanal</p>
        </div>
      </header>

      <section className="content">
        {/* KPI Cards */}
        <div className="kpi-grid">
          <div className="kpi-card bordered">
            <div className="kpi-title">Faturamento Bruto</div>
            <div className="kpi-value">R$ 145.230</div>
          </div>
          <div className="kpi-card bordered success">
            <div className="kpi-title">Lucro Líquido Real</div>
            <div className="kpi-value" style={{ color: 'var(--success)' }}>R$ 62.450</div>
          </div>
          <div className="kpi-card bordered wpp">
            <div className="kpi-title">Margem de Lucro Média</div>
            <div className="kpi-value">43,0%</div>
          </div>
          <div className="kpi-card bordered shopee">
            <div className="kpi-title">Volume de Pedidos</div>
            <div className="kpi-value">2.845</div>
          </div>
        </div>

        {/* Charts */}
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
              <Doughnut data={doughnutData} options={{ responsive: true, maintainAspectRatio: false, cutout: '70%' }} />
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
