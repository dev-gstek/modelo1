import { Link, useLocation } from 'react-router-dom';

export default function Sidebar() {
  const location = useLocation();

  return (
    <aside className="sidebar">
      <Link to="/" className="logo">
        <svg width="24" height="24" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" />
        </svg>
        DomLux<span>ERP</span>
      </Link>
      
      <Link to="/" className={`nav-item ${location.pathname === '/' ? 'active' : ''}`}>
        Dashboard BI
      </Link>
      
      <Link to="/finance" className={`nav-item ${location.pathname === '/finance' ? 'active' : ''}`}>
        Inteligência Financeira
      </Link>
      
      <div className="nav-item">Gestão de Estoque</div>
      <div className="nav-item">Custos e SKUs</div>
      <div className="nav-item">Configurações</div>
    </aside>
  );
}
