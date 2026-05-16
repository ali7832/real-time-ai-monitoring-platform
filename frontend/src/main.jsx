import React, { useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Activity, AlertTriangle, Bell, BrainCircuit, CircleDollarSign, Gauge, LineChart as LineIcon, MonitorDot, RadioTower, Rocket, ShieldCheck, Siren, Zap } from 'lucide-react';
import { Area, AreaChart, Bar, BarChart, CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import './styles.css';

const pages = ['Overview', 'Metric Lab', 'Incidents', 'Drift Center', 'Cost & Latency', 'SLOs', 'Playbooks'];
const healthTrend = [{t:'09:00',health:96,latency:520,drift:12},{t:'10:00',health:94,latency:560,drift:14},{t:'11:00',health:88,latency:710,drift:21},{t:'12:00',health:91,latency:640,drift:18},{t:'13:00',health:97,latency:490,drift:10}];
const services = [
  ['rag-assistant','prod','us-east','97','healthy','No action required'],
  ['fraud-scorer','prod','eu-west','82','degraded','Investigate latency spike'],
  ['support-copilot','staging','us-east','91','watch','Review drift signal'],
  ['claims-agent','prod','ap-south','74','critical','Create incident and rollback model']
];
const incidents = [
  ['INC-7781','claims-agent','critical','Drift above threshold','Rollback model and notify owner'],
  ['INC-7782','fraud-scorer','degraded','P95 latency breached','Scale workers and inspect queue'],
  ['INC-7783','support-copilot','watch','Cost per request rising','Review prompt version']
];

function fallbackMetric(form){
  let health = 100;
  const reasons = [];
  if (Number(form.latency_ms) > 700) { health -= 22; reasons.push('Latency above target threshold'); }
  if (Number(form.error_rate) > 2) { health -= 24; reasons.push('Error rate is elevated'); }
  if (Number(form.drift_score) > 20) { health -= 28; reasons.push('Model drift score exceeded monitoring threshold'); }
  if (Number(form.cost_per_1k) > 1.5) { health -= 12; reasons.push('Cost per 1K requests is above budget'); }
  const status = health < 75 ? 'critical' : health < 88 ? 'degraded' : health < 95 ? 'watch' : 'healthy';
  return { incident_id: status === 'healthy' ? null : `INC-${Date.now().toString().slice(-5)}`, health_score: Math.max(health, 1), status, recommended_action: status === 'critical' ? 'Create incident, page owner, and consider rollback.' : status === 'degraded' ? 'Open investigation and scale the impacted service.' : status === 'watch' ? 'Monitor closely and review recent model changes.' : 'No action required.', reasons: reasons.length ? reasons : ['Service is operating within defined thresholds'] };
}

function App(){
  const [active,setActive] = useState('Overview');
  const [form,setForm] = useState({ service_name:'claims-agent', environment:'prod', latency_ms:820, error_rate:3.1, throughput_rps:118, drift_score:26, cost_per_1k:1.8 });
  const [result,setResult] = useState(fallbackMetric(form));
  const metrics = useMemo(()=>[
    ['Services Monitored','42','+6',MonitorDot],['Fleet Health','93.4%','+2.1%',ShieldCheck],['Open Incidents','3','-5 today',Siren],['Cost Efficiency','87%','+9%',CircleDollarSign]
  ],[]);
  const submitMetric = async()=>{
    try{
      const response = await fetch('/metrics',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(form)});
      if(!response.ok) throw new Error('offline');
      setResult(await response.json());
    }catch{setResult(fallbackMetric(form));}
  };
  return <main className="app-shell"><aside className="sidebar"><div className="brand"><RadioTower/><div><strong>AIOps Monitor</strong><span>Real-Time AI Reliability</span></div></div>{pages.map(p=><button className={active===p?'active':''} onClick={()=>setActive(p)} key={p}>{p}</button>)}</aside><section className="workspace"><header className="topbar"><div><p className="eyebrow">AI production monitoring</p><h1>{active}</h1></div><button onClick={submitMetric}>Submit metric</button></header>{active==='Overview'&&<Overview metrics={metrics}/>} {active==='Metric Lab'&&<MetricLab form={form} setForm={setForm} result={result} submitMetric={submitMetric}/>} {active==='Incidents'&&<Incidents/>} {active==='Drift Center'&&<DriftCenter/>} {active==='Cost & Latency'&&<CostLatency/>} {active==='SLOs'&&<SLOs/>} {active==='Playbooks'&&<Playbooks/>}</section></main>
}
function Overview({metrics}){return <><section className="metrics">{metrics.map(([l,v,d,Icon])=><article className="card" key={l}><Icon/><span>{l}</span><strong>{v}</strong><small>{d}</small></article>)}</section><section className="grid"><Panel title="Fleet health trend" icon={<Activity/>}><ResponsiveContainer width="100%" height={260}><AreaChart data={healthTrend}><CartesianGrid strokeDasharray="3 3" stroke="#24384b"/><XAxis dataKey="t" stroke="#9cafc4"/><YAxis stroke="#9cafc4"/><Tooltip/><Area dataKey="health" stroke="#22c55e" fill="#14532d"/></AreaChart></ResponsiveContainer></Panel><Panel title="Service fleet" icon={<MonitorDot/>}><Table rows={services}/></Panel></section></>}
function MetricLab({form,setForm,result,submitMetric}){return <section className="grid"><Panel title="Metric submission lab" icon={<Gauge/>}>{Object.entries(form).map(([k,v])=><label key={k}>{k.replaceAll('_',' ')}<input value={v} onChange={e=>setForm({...form,[k]:e.target.value})}/></label>)}<button onClick={submitMetric}>Evaluate health</button></Panel><Panel title="Health decision" icon={<Bell/>}><div className="score"><span className={result.status}>{result.status}</span><strong>{result.health_score}%</strong><p>{result.recommended_action}</p><small>{result.incident_id || 'No incident generated'}</small></div>{result.reasons.map(r=><div className="reason" key={r}>{r}</div>)}</Panel></section>}
function Incidents(){return <Panel title="Incident response queue" icon={<AlertTriangle/>}><Table rows={incidents}/></Panel>}
function DriftCenter(){return <section className="grid"><Panel title="Drift signals" icon={<BrainCircuit/>}><ResponsiveContainer width="100%" height={260}><LineChart data={healthTrend}><XAxis dataKey="t" stroke="#9cafc4"/><YAxis stroke="#9cafc4"/><Tooltip/><Line dataKey="drift" stroke="#fb7185" strokeWidth={3}/></LineChart></ResponsiveContainer></Panel><Panel title="Drift actions" icon={<Rocket/>}><div className="reason">Compare production distribution with baseline window.</div><div className="reason">Trigger retraining review if drift remains elevated for 3 intervals.</div><div className="reason">Rollback high-risk model releases when drift and error rate rise together.</div></Panel></section>}
function CostLatency(){return <section className="grid"><Panel title="Latency profile" icon={<LineIcon/>}><ResponsiveContainer width="100%" height={260}><AreaChart data={healthTrend}><XAxis dataKey="t" stroke="#9cafc4"/><YAxis stroke="#9cafc4"/><Tooltip/><Area dataKey="latency" stroke="#38bdf8" fill="#0e7490"/></AreaChart></ResponsiveContainer></Panel><Panel title="Cost controls" icon={<CircleDollarSign/>}><div className="reason">Prompt cost budget: 87% healthy.</div><div className="reason">Claims-agent cost spike linked to prompt version v17.</div><div className="reason">Batch summarization jobs should be rate-limited during peak windows.</div></Panel></section>}
function SLOs(){return <section className="grid"><Panel title="SLO scorecard" icon={<ShieldCheck/>}><ResponsiveContainer width="100%" height={260}><BarChart data={[{slo:'Uptime',v:99.95},{slo:'P95 Latency',v:94},{slo:'Error Budget',v:88},{slo:'Drift',v:91}]}><XAxis dataKey="slo" stroke="#9cafc4"/><YAxis stroke="#9cafc4"/><Tooltip/><Bar dataKey="v" fill="#38bdf8"/></BarChart></ResponsiveContainer></Panel><Panel title="Error budget policy" icon={<Zap/>}><div className="reason">Freeze releases when error budget falls below 15%.</div><div className="reason">Page service owner for critical service degradation.</div><div className="reason">Create post-incident review after repeated SLO violations.</div></Panel></section>}
function Playbooks(){return <section className="grid"><Panel title="Operational playbooks" icon={<Rocket/>}><div className="reason">Latency spike: scale workers, inspect queue, reduce batch jobs.</div><div className="reason">Drift event: compare baseline, inspect data source, trigger retraining review.</div><div className="reason">Cost anomaly: inspect prompt version, model route, and request volume.</div></Panel><Panel title="Recommended response" icon={<Bell/>}><div className="response">AIOps Monitor converts telemetry into incident context, likely cause, and response guidance for operations teams.</div></Panel></section>}
function Table({rows}){return <div className="table">{rows.map(row=><div className="row" key={row[0]}>{row.map(cell=><span key={cell}>{cell}</span>)}</div>)}</div>}
function Panel({title,icon,children}){return <article className="panel"><div className="panel-title">{icon}<h2>{title}</h2></div>{children}</article>}

createRoot(document.getElementById('root')).render(<App/>);
