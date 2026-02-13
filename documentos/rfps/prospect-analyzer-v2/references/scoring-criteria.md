# Critérios de Pontuação (Scoring) - V2

## Dimensão 1: Data & Analytics (0-10)

### Checklist de Verificação

| Item | Peso | Como Verificar |
|------|------|----------------|
| Google Analytics 4 | 2.0 | Buscar `gtag` ou `GA4` no HTML |
| Google Tag Manager | 1.5 | Buscar `gtm.js` ou GTM-XXXX |
| Meta Pixel | 1.5 | Buscar `fbq` ou `connect.facebook.net` |
| Google Ads Tag | 1.0 | Buscar `googleadservices` ou `AW-` |
| Eventos configurados | 1.5 | Verificar eventos no dataLayer |
| Enhanced E-commerce | 1.0 | Verificar `purchase`, `add_to_cart` |
| Core Web Vitals OK | 1.0 | PageSpeed Insights > 80 |
| Schema Markup | 0.5 | Buscar `application/ld+json` |

### Tabela de Notas

| Nota | Descrição | Configuração Típica |
|------|-----------|---------------------|
| 0-1 | Inexistente | Sem nenhum tracking |
| 2-3 | Muito básico | GA4 apenas, sem configuração |
| 4-5 | Básico | GA4 + 1 pixel + GTM básico |
| 6-7 | Intermediário | GTM configurado + 2-3 pixels + eventos |
| 8-9 | Avançado | Stack completo + eventos avançados |
| 10 | Expert | Server-side + CDP + atribuição multi-touch |

### Exemplos Práticos

**Nota 3**: "GA4 instalado mas sem eventos personalizados. Não possui GTM. Meta Pixel presente mas sem eventos de conversão configurados."

**Nota 7**: "GTM bem implementado com GA4 e Meta Pixel. Eventos de add_to_cart e purchase configurados. Falta server-side tracking e CDP."

---

## Dimensão 2: SEO (0-10)

### Checklist de Verificação

| Item | Peso | Como Verificar |
|------|------|----------------|
| Title tags otimizadas | 1.5 | `<title>` único por página, < 60 chars |
| Meta descriptions | 1.0 | `<meta name="description">` relevante |
| Estrutura H1-H6 | 1.0 | Um H1 por página, hierarquia correta |
| URLs amigáveis | 0.5 | Sem IDs, com keywords |
| Sitemap.xml | 0.5 | Presente e atualizado |
| Robots.txt | 0.5 | Configurado corretamente |
| Mobile-friendly | 1.5 | Responsive, viewport correto |
| Core Web Vitals | 1.5 | LCP < 2.5s, FID < 100ms, CLS < 0.1 |
| Páginas indexadas | 1.0 | site:dominio no Google |
| Domain Authority | 1.0 | DR/DA estimado |

### Tabela de Notas

| Nota | Descrição | Situação Típica |
|------|-----------|-----------------|
| 0-1 | Crítico | Site não indexado ou com erros graves |
| 2-3 | Fraco | Meta tags básicas, sem otimização |
| 4-5 | Básico | SEO on-page ok, poucos rankings |
| 6-7 | Bom | Rankings em keywords secundárias |
| 8-9 | Muito bom | Top 10 em keywords principais |
| 10 | Excelente | Domina SERPs, alta autoridade |

---

## Dimensão 3: Performance/Mídia Paga (0-10)

### Checklist de Verificação

| Item | Peso | Como Verificar |
|------|------|----------------|
| Google Ads ativo | 2.0 | Ads Transparency Center |
| Meta Ads ativo | 2.0 | Meta Ad Library |
| Qualidade dos criativos | 2.0 | Avaliação visual dos anúncios |
| Landing pages dedicadas | 1.5 | URLs específicas para campanhas |
| Remarketing ativo | 1.5 | Anúncios segmentados visíveis |
| Diversificação de canais | 1.0 | LinkedIn, TikTok, etc. |

### Tabela de Notas

| Nota | Descrição | Situação Típica |
|------|-----------|-----------------|
| 0-1 | Inexistente | Nenhum anúncio ativo |
| 2-3 | Iniciante | 1 canal, criativos básicos |
| 4-5 | Básico | 2 canais, criativos medianos |
| 6-7 | Bom | Multi-canal, boas landing pages |
| 8-9 | Avançado | Funil completo, remarketing |
| 10 | Expert | Estratégia sofisticada, testes A/B |

---

## Dimensão 4: Conteúdo & Social (0-10)

### Checklist de Verificação

| Item | Peso | Como Verificar |
|------|------|----------------|
| Blog ativo | 1.5 | Frequência de posts |
| Qualidade do conteúdo | 1.5 | Profundidade, originalidade |
| Instagram ativo | 1.5 | Posts/semana, engajamento |
| LinkedIn ativo | 1.0 | Posts, interações |
| YouTube/vídeo | 1.0 | Canal, regularidade |
| Engajamento geral | 1.5 | Likes, comments, shares |
| UGC/comunidade | 1.0 | Reviews, menções |

### Tabela de Notas

| Nota | Descrição | Situação Típica |
|------|-----------|-----------------|
| 0-1 | Ausente | Sem blog, redes inativas |
| 2-3 | Esporádico | Posts irregulares, baixo engajamento |
| 4-5 | Regular | 1-2 posts/semana, algum engajamento |
| 6-7 | Bom | Estratégia clara, comunidade ativa |
| 8-9 | Muito bom | Content marketing robusto |
| 10 | Referência | Thought leadership, alta influência |

---

## Dimensão 5: CRM & Automação (0-10)

### Checklist de Verificação

| Item | Peso | Como Verificar |
|------|------|----------------|
| Captura de leads | 2.0 | Forms, popups, newsletter |
| CRM identificável | 2.0 | Integrações visíveis (HubSpot, RD, etc.) |
| Email marketing | 2.0 | Newsletter, sequências |
| Automações | 2.0 | Fluxos automatizados |
| Personalização | 1.0 | Conteúdo dinâmico |
| Integração omnichannel | 1.0 | WhatsApp, chat, email |

### Tabela de Notas

| Nota | Descrição | Situação Típica |
|------|-----------|-----------------|
| 0-1 | Inexistente | Sem captura de leads |
| 2-3 | Básico | Formulário simples, sem automação |
| 4-5 | Regular | Newsletter + CRM básico |
| 6-7 | Bom | Automações de boas-vindas |
| 8-9 | Avançado | Réguas completas, segmentação |
| 10 | Expert | CDP + personalização avançada |

---

## Dimensão 6: Inovação & Tech (0-10)

### Checklist de Verificação

| Item | Peso | Como Verificar |
|------|------|----------------|
| Plataforma moderna | 2.0 | Stack tecnológico |
| Performance do site | 2.0 | Velocidade, UX |
| Chatbot/IA | 2.0 | Assistentes virtuais |
| Integrações | 1.5 | APIs, webhooks |
| App mobile | 1.0 | Presença em stores |
| Pagamentos diversos | 1.5 | Pix, cartões, boleto |

### Tabela de Notas

| Nota | Descrição | Situação Típica |
|------|-----------|-----------------|
| 0-1 | Desatualizado | Site legado, sem recursos modernos |
| 2-3 | Básico | E-commerce padrão |
| 4-5 | Regular | Plataforma atual, sem diferenciais |
| 6-7 | Bom | Algumas inovações implementadas |
| 8-9 | Avançado | IA, automações, integrações |
| 10 | Vanguarda | Tech-first, early adopter |

---

## Cálculo do Score Geral

### Fórmula

```
Score = (Data × 0.25) + (SEO × 0.20) + (Performance × 0.20) + 
        (Conteúdo × 0.15) + (CRM × 0.10) + (Inovação × 0.10)
```

### Pesos Justificados

| Dimensão | Peso | Justificativa |
|----------|------|---------------|
| Data & Analytics | 25% | Base para todas as decisões |
| SEO | 20% | Tráfego orgânico sustentável |
| Performance | 20% | Geração de demanda imediata |
| Conteúdo | 15% | Brand awareness e autoridade |
| CRM | 10% | Conversão e retenção |
| Inovação | 10% | Diferenciação competitiva |

### Classificação Final

| Score | Maturidade | Perfil do Cliente |
|-------|------------|-------------------|
| 0-2 | Iniciante | Precisa estruturar tudo |
| 3-4 | Básico | Precisa de quick wins |
| 5-6 | Intermediário | Pronto para escalar |
| 7-8 | Avançado | Foco em otimização |
| 9-10 | Expert | Foco em inovação |

---

## Exemplo de Preenchimento

```json
{
  "prospect": "Empresa XYZ",
  "scores": {
    "data": {
      "valor": 5,
      "justificativa": "GA4 instalado, GTM básico, Meta Pixel sem eventos",
      "itens": {
        "ga4": true,
        "gtm": true,
        "meta_pixel": true,
        "eventos": false,
        "ecommerce": false
      }
    },
    "seo": {
      "valor": 6,
      "justificativa": "SEO on-page ok, rankings em long tail",
      "paginas_indexadas": 150,
      "core_web_vitals": "amarelo"
    },
    "performance": {
      "valor": 4,
      "justificativa": "Apenas Google Ads ativo, criativos medianos",
      "canais_ativos": ["google_ads"]
    },
    "conteudo": {
      "valor": 5,
      "justificativa": "Blog com posts mensais, Instagram 3x/semana",
      "instagram_seguidores": 15000
    },
    "crm": {
      "valor": 3,
      "justificativa": "Apenas formulário de contato, sem automação",
      "ferramentas": []
    },
    "inovacao": {
      "valor": 4,
      "justificativa": "E-commerce padrão, sem chatbot ou IA",
      "plataforma": "vtex"
    }
  },
  "score_geral": 4.65,
  "classificacao": "Básico",
  "prioridades": [
    "Configurar eventos de conversão",
    "Implementar régua de CRM",
    "Diversificar canais de mídia"
  ]
}
```
