import Layout from '../../components/Layout';

const checklist = [
  '3 Shares',
  'Receipt included',
  'Location included',
  'Menu included',
  'Community impact',
  'HD video/audio'
];

export default function SubmitEntryPage() {
  return (
    <Layout>
      <div className="card">
        <h2>Submit Talent Entry</h2>
        <ul>
          {checklist.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
    </Layout>
  );
}
