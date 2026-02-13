import Layout from '../components/Layout';
import { demoState } from '../state/store';

export default function Dashboard() {
  return (
    <Layout>
      <div className="card">
        <h2>Membership Dashboard</h2>
        <p>Stars: {demoState.stars}</p>
        <p>Black Dollars: {demoState.blackDollars}</p>
        <p>Tier: {demoState.tier}</p>
      </div>
    </Layout>
  );
}
