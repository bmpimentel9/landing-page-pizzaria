# Análise Técnica Pré-Reunião: Klubi

**Data:** 30/01/2026
**Site analisado:** klubi.com.br + consorcio.klubi.com.br

---

## 🔍 Resumo Executivo

A Klubi tem uma estrutura de tracking fragmentada entre dois domínios, com containers GTM e propriedades GA4 diferentes em cada ambiente. Isso representa **risco significativo de perda de dados** no funil de conversão e dificulta a otimização de campanhas.

---

## 📊 Stack de Tracking Identificado

### Site Principal (www.klubi.com.br)

| Ferramenta | ID/Status |
|------------|-----------|
| GTM | `GTM-K2K4NNFM` |
| GA4 | `G-XWSJC2D2LV` |
| Google Ads | `AW-362695272` |
| Amplitude | ✅ Ativo |
| Hotjar | ✅ Ativo (ID 2312000) |
| Facebook Pixel | ❌ **NÃO DETECTADO** |
| Consent Mode | ✅ Configurado |

### Funnel de Conversão (consorcio.klubi.com.br)

| Ferramenta | ID/Status |
|------------|-----------|
| GTM | `GTM-KLB89Q96` + `GTM-NDFLBMH` ⚠️ (2 containers!) |
| GA4 | `G-QWJVNVRTZ0` + `G-X7PPLXH3CY` ⚠️ (2 propriedades!) |
| Facebook Pixel | ✅ Carregado (fbq detectado) |

---

## 🚨 Problemas Críticos Identificados

### 1. **Arquitetura Cross-Domain Fragmentada**
- Site principal: `www.klubi.com.br`
- Funnel: `consorcio.klubi.com.br`
- **Impacto:** Perda de atribuição se cross-domain tracking não estiver 100% configurado

### 2. **GTM Containers Diferentes**
- Site usa `GTM-K2K4NNFM`
- Funnel usa `GTM-KLB89Q96` + `GTM-NDFLBMH`
- **Impacto:** Dificuldade de manutenção, regras inconsistentes

### 3. **GA4 Properties Fragmentadas**
- Site: `G-XWSJC2D2LV`
- Funnel: `G-QWJVNVRTZ0` + `G-X7PPLXH3CY`
- **Impacto:** Funil quebrado no GA4, métricas dispersas

### 4. **Facebook Pixel Ausente no Site Principal**
- Pixel só carrega no funnel (consorcio.klubi.com.br)
- **Impacto:** Audiências de retargeting limitadas, perda de eventos de topo de funil

### 5. **Eventos de Conversão Não Detectados**
- DataLayer mostra apenas eventos padrão: `gtm.js`, `gtm.dom`, `gtm.load`, `gtm.scrollDepth`
- Não vi eventos customizados como: `generate_lead`, `begin_checkout`, `purchase`
- **Impacto:** Plataformas de mídia recebendo sinal fraco

### 6. **Sem Evidência de CAPI (Conversions API)**
- Facebook CAPI não detectado
- Google Offline Conversions não detectado
- **Impacto:** Perda significativa de dados pós-iOS 14

---

## ✅ Pontos Positivos

- Consent Mode v2 configurado (LGPD compliance)
- Amplitude para product analytics
- Hotjar para behavior analytics
- Cookies cross-domain parecem estar funcionando (_ga compartilhado)
- Google Ads conversion tag presente

---

## ❓ Perguntas Estratégicas para a Reunião

Baseado na análise, recomendo adicionar estas perguntas ao seu checklist:

### Sobre a Arquitetura Fragmentada
> "Vi que vocês têm GTM containers diferentes no site principal e no funnel de conversão. Isso foi intencional? Como vocês garantem consistência entre os dois ambientes?"

### Sobre Facebook
> "O Facebook Pixel só está no funnel, não no site principal. Vocês usam CAPI para compensar? Qual o EMQ (Event Match Quality) atual?"

### Sobre GA4
> "Existem múltiplas propriedades GA4. Como vocês consolidam os dados do funil completo? Usam BigQuery para unificar?"

### Sobre Eventos de Conversão
> "Quais eventos vocês disparam no dataLayer além dos padrões? Vocês têm eventos de `generate_lead`, `begin_checkout` configurados?"

### Sobre Google Ads
> "Vocês fazem upload de conversões offline do CRM para o Google Ads? Como passam o GCLID para o funil?"

---

## 🎯 Red Flags a Confirmar na Reunião

- [ ] Cross-domain tracking entre www e consorcio está funcionando 100%?
- [ ] Existe uma GA4 property consolidada ou os dados estão fragmentados?
- [ ] CAPI do Facebook está implementado?
- [ ] Eventos de conversão estão sendo disparados corretamente?
- [ ] Existe pipeline automatizado CRM → Plataformas de mídia?

---

## 📱 Informações Adicionais do Site

- **Produto:** Consórcio (Imóvel, Auto, Moto, Celular, Viagem, Seguros)
- **Nota Reclame Aqui:** 9.6/10 (RA1000)
- **Regulamentação:** Autorizado pelo Banco Central
- **Chat:** Widget de WhatsApp integrado

---

*Análise realizada via inspeção de código-fonte e JavaScript em 30/01/2026*
