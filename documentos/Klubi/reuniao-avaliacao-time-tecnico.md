# Reunião: Avaliação de Capacidade Técnica - Growth Marketing

---

## 🔎 INTELIGÊNCIA PRÉVIA (Análise do Site)

**O que já sabemos antes da reunião:**

### Stack Atual Detectado

| Ambiente | GTM | GA4 | Facebook | Outros |
|----------|-----|-----|----------|--------|
| www.klubi.com.br | `GTM-K2K4NNFM` | `G-XWSJC2D2LV` | ❌ Ausente | Amplitude, Hotjar |
| consorcio.klubi.com.br | `GTM-KLB89Q96` + `GTM-NDFLBMH` | `G-QWJVNVRTZ0` + `G-X7PPLXH3CY` | ✅ Ativo | - |

### 🚨 Problemas Identificados para Questionar

1. **Arquitetura fragmentada** — 2 domínios, GTMs diferentes, GA4s diferentes
2. **Facebook Pixel só no funnel** — Perdendo dados de topo de funil
3. **Múltiplos containers GTM no funnel** — Risco de conflito
4. **Sem eventos customizados visíveis** — Só eventos padrão no dataLayer
5. **CAPI não detectado** — Provável perda de dados pós-iOS 14

### ✅ Pontos Positivos Identificados

- Consent Mode v2 configurado (LGPD ok)
- Google Ads conversion tag presente
- Amplitude para product analytics
- Hotjar para behavior analytics

---

## 1. Stack de Tecnologia

- [ ] **Qual é o stack de tecnologia que vocês usam?**
  - *Ouvir:* Node, Python, Cloud (AWS/GCP/Azure), bancos de dados

- [ ] **Vocês usam algum CDP (Customer Data Platform)?**
  - *Exemplos:* Segment, RudderStack, mParticle
  - *Red flag:* Nunca ouviram falar ou só usam GA4

- [ ] **Como vocês gerenciam tags hoje? Usam GTM Server-Side?**
  - *Ideal:* GTM Server-Side configurado
  - *Red flag:* Só GTM client-side sem conhecimento de server-side

---

## 2. Tagueamento e Implementação

- [ ] **Quando temos um parceiro (ex: Vivo), quem coloca a página no ar - vocês têm capacidade de implementar todas as tags necessárias?**
  - *Ouvir:* Autonomia vs dependência do cliente

- [ ] **Como vocês estruturam a nomenclatura de eventos?**
  - *Ideal:* Taxonomia documentada (ex: `purchase`, `lead`, `add_to_cart`)
  - *Red flag:* "Cada projeto é diferente" sem padrão

- [ ] **Vocês implementam Enhanced Conversions do Google?**
  - *Verificar:* Conhecem? Já fizeram?

- [ ] **Como vocês lidam com consent mode e LGPD nas tags?**
  - *Ideal:* Consent mode v2 implementado
  - *Red flag:* "O cliente cuida disso"

---

## 3. APIs de Conversão (CAPI)

- [ ] **Vocês implementam Facebook Conversions API (CAPI)?**
  - *Follow-up:* Server-side ou via parceiro (Shopify, etc)?

- [ ] **Qual o Event Match Quality (EMQ) médio que vocês conseguem?**
  - *Ideal:* Acima de 6.0
  - *Red flag:* Não sabem o que é EMQ

- [ ] **Vocês trabalham com Google Ads Offline Conversion Import?**
  - *Ouvir:* GCLID tracking, upload de conversões offline

- [ ] **Como vocês passam dados de CRM/vendas de volta para as plataformas?**
  - *Ideal:* Pipeline automatizado
  - *Red flag:* "Fazemos manual" ou "não fazemos"

- [ ] **Vocês usam deduplicação entre pixel e CAPI?**
  - *Verificar:* Entendem event_id?

---

## 4. Data Lake e Match de Dados

- [ ] **Me fale mais sobre o data lake de vocês. Como ele é construído?**
  - *Ouvir:* BigQuery, Snowflake, Redshift, Databricks

- [ ] **Quais são as fontes que alimentam o data lake?**
  - *Ideal:* CRM, plataformas de mídia, site, app, call center

- [ ] **Vocês têm bases externas para match/enriquecimento?**
  - *Exemplos:* Serasa, Neoway, BigDataCorp
  - *Follow-up:* Taxa de match média?

- [ ] **Como vocês fazem identity resolution entre canais?**
  - *Ouvir:* Têm um ID único? Usam email hash? Phone hash?

- [ ] **Qual a latência dos dados? Real-time ou batch?**
  - *Ideal para growth:* Near real-time (minutos)
  - *Aceitável:* Batch diário
  - *Red flag:* "Depende do cliente"

---

## 5. Capacidade de Execução

- [ ] **Qual o tempo médio para subir uma landing page com tracking completo?**
  - *Ideal:* 24-48h
  - *Red flag:* "Depende" sem dar número

- [ ] **Se eu precisar de uma mudança urgente em produção, qual o SLA?**
  - *Ouvir:* Processo de deploy, autonomia

- [ ] **Quantas pessoas no time sabem implementar CAPI do zero?**
  - *Verificar:* Dependência de uma pessoa só

- [ ] **Vocês têm ambiente de staging/homologação?**
  - *Ideal:* Sim, com validação de tags antes de prod

- [ ] **Como vocês validam se as tags estão disparando corretamente?**
  - *Ideal:* Facebook Test Events, GA4 DebugView, Tag Assistant
  - *Red flag:* "Olhamos no painel depois"

---

## 6. Integrações e Automação

- [ ] **Vocês integram com algum CRM? Qual?**
  - *Exemplos:* Salesforce, HubSpot, Pipedrive, RD Station

- [ ] **Têm experiência com Zapier, Make ou n8n?**
  - *Ouvir:* Automações de dados entre sistemas

- [ ] **Vocês já construíram dashboards de atribuição próprios?**
  - *Follow-up:* Qual modelo? Last-click, data-driven, custom?

---

## 7. Perguntas de Profundidade (se tiver tempo)

- [ ] **Me dá um exemplo de um problema complexo de tracking que vocês resolveram**
  - *Ouvir:* Nível de detalhe técnico, raciocínio

- [ ] **Como vocês lidam com iOS 14+ e a perda de dados?**
  - *Ideal:* CAPI, modelagem de conversão, SKAdNetwork
  - *Red flag:* "Não tem muito o que fazer"

- [ ] **Vocês trabalham com públicos de primeira parte (1P audiences)?**
  - *Verificar:* Upload de listas, custom audiences, lookalikes de CRM

---

## 🚩 Red Flags a Observar

| Sinal | O que significa |
|-------|-----------------|
| Não conhecem CAPI/EMQ | Time não está atualizado |
| Só GTM client-side | Perda de dados significativa |
| Sem data lake próprio | Dependência total do cliente |
| Deploy manual | Execução lenta |
| "Depende do cliente" para tudo | Sem proatividade técnica |
| Não falam de consent/LGPD | Risco de compliance |

---

## ✅ Green Flags

| Sinal | O que significa |
|-------|-----------------|
| GTM Server-Side implementado | Maturidade técnica alta |
| EMQ acima de 6.0 | Sabem passar sinal de qualidade |
| Pipeline automatizado CRM → Plataformas | Execução escalável |
| Falam de deduplicação e event_id | Entendem profundamente |
| Tempo de deploy claro (24-48h) | Capacidade de execução real |

---

## 🎯 Perguntas Diretas Baseadas na Análise

Use estas perguntas para confrontar educadamente o que você descobriu:

- [ ] **"Vi que vocês têm GTM containers diferentes no site e no funnel. Por que essa escolha? Como garantem consistência?"**

- [ ] **"O Facebook Pixel só está no consorcio.klubi.com.br, não no site principal. Isso é intencional? Vocês compensam com CAPI?"**

- [ ] **"Existem 2 propriedades GA4 no funnel. Como vocês consolidam o funil completo? Usam BigQuery?"**

- [ ] **"No dataLayer só vi eventos padrão (gtm.js, gtm.dom). Onde estão os eventos de negócio como `generate_lead`, `begin_checkout`?"**

- [ ] **"Como vocês passam o GCLID do site principal para o funnel no subdomínio? O cross-domain tracking está funcionando?"**

---

## Anotações da Reunião

**Data:** _______________
**Participantes:** _______________

### Stack confirmado:
-

### Respostas sobre a arquitetura fragmentada:
-

### Principais pontos positivos:
-

### Principais gaps identificados:
-

### Próximos passos:
-

---

*Checklist + análise técnica preparados para reunião de Growth Marketing*
*Análise do site realizada em 30/01/2026*
