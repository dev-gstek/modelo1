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
      
      <Link to="/payable" className={`nav-item ${location.pathname === '/payable' ? 'active' : ''}`}>
        Contas a Pagar
      </Link>
      <Link to="/reconciliation" className={`nav-item ${location.pathname === '/reconciliation' ? 'active' : ''}`}>
        Conciliação
      </Link>
      <Link to="/estoque" className={`nav-item ${location.pathname === '/estoque' ? 'active' : ''}`}>
        Gestão de Estoque
      </Link>
      <Link to="/skus" className={`nav-item ${location.pathname === '/skus' ? 'active' : ''}`}>
        Custos e SKUs
      </Link>
      <Link to="/settings" className={`nav-item ${location.pathname === '/settings' ? 'active' : ''}`}>
        Configurações
      </Link>
    </aside>
  );
}
