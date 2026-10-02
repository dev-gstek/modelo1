import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import FinanceTable from './pages/FinanceTable';
import './index.css';

function App() {
  return (
    <Router>
      <Sidebar />
      <main className="main">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/finance" element={<FinanceTable />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
