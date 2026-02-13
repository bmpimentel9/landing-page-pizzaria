# Fontes de Dados - Guia Completo

## REGRA DE OURO

> **NUNCA invente dados. Se não encontrar, declare "Dados não disponíveis publicamente" e use estimativas conservadoras baseadas em benchmarks do setor.**

---

## 1. Análise Técnica (Tags & Tracking)

### BuiltWith
- **URL**: `https://builtwith.com/{domínio}`
- **Query**: `site:builtwith.com "{domínio}"`
- **Dados**: Stack tecnológico completo, tags de marketing
- **Confiabilidade**: Alta
- **Exemplo**: "BuiltWith indica presença de GA4, GTM e Meta Pixel"

### PageSpeed Insights
- **URL**: `https://pagespeed.web.dev/analysis?url={url}`
- **Query**: `pagespeed insights {domínio}` ou web_fetch direto
- **Dados**: Core Web Vitals, performance score
- **Confiabilidade**: Alta (dados do Google)
- **Exemplo**: "PageSpeed Insights: LCP 2.1s (bom), FID 45ms (bom), CLS 0.15 (precisa melhorar)"

### Análise Direta do HTML
- **Método**: web_fetch na URL do prospect
- **Buscar**:
  ```
  gtag | google-analytics | GA4       → Google Analytics
  gtm.js | GTM-                       → Google Tag Manager
  fbq | connect.facebook.net          → Meta Pixel
  googleadservices | AW-              → Google Ads
  snap.licdn.com | _linkedin_         → LinkedIn Insight
  analytics.tiktok.com                → TikTok Pixel
  hotjar | clarity                    → Heatmaps
  application/ld+json                 → Schema Markup
  ```
- **Confiabilidade**: Alta (verificação direta)

---

## 2. Tráfego e Keywords

### SimilarWeb (Dados Públicos)
- **Query**: `site:similarweb.com {domínio}`
- **Dados**: Tráfego estimado, origens, geografia, top keywords
- **Confiabilidade**: Média (estimativas)
- **Limitações**: Dados gratuitos limitados a overview
- **Exemplo**: "Segundo SimilarWeb, tráfego estimado de ~50K visitas/mês"

### SEMrush (Dados Públicos)
- **Query**: `site:semrush.com {domínio}`
- **Dados**: Keywords orgânicas, backlinks, tráfego orgânico estimado
- **Confiabilidade**: Média (estimativas)
- **Exemplo**: "SEMrush estima ~200 keywords ranqueadas"

### Ubersuggest (Dados Públicos)
- **Query**: `{domínio} ubersuggest` ou `site:neilpatel.com {domínio}`
- **Dados**: Keywords, volume, dificuldade
- **Confiabilidade**: Média

### Google Search (Páginas Indexadas)
- **Query**: `site:{domínio}`
- **Dados**: Número aproximado de páginas indexadas
- **Confiabilidade**: Alta (dado do Google)
- **Exemplo**: "Google indexou aproximadamente 1.200 páginas"

### Google Trends
- **URL**: `https://trends.google.com`
- **Query**: `{marca} google trends brasil`
- **Dados**: Interesse ao longo do tempo, sazonalidade
- **Confiabilidade**: Alta

---

## 3. Keywords Transacionais

### Metodologia para Coleta

1. **Identificar nicho do prospect**
2. **Buscar dados de volume**:
   ```
   "{nicho} keywords volume brasil"
   "{nicho} palavras-chave transacionais"
   "melhores keywords {nicho} google ads"
   ```
3. **Verificar quem domina**:
   ```
   Buscar a keyword no Google e anotar:
   - Posição 1 (orgânico)
   - Posição 2 (orgânico)
   - Posição 3 (orgânico)
   - Anunciantes visíveis
   ```

### Fontes de Volume/CPC

| Fonte | Acesso | Confiabilidade |
|-------|--------|----------------|
| Google Keyword Planner | Pago/restrito | Alta |
| SEMrush | Pago/parcial gratuito | Alta |
| Ubersuggest | Gratuito limitado | Média |
| KeywordTool.io | Gratuito limitado | Média |
| AnswerThePublic | Gratuito limitado | Média |

### Formato da Tabela de Keywords

```
| Keyword | Volume/mês | CPC (R$) | Dificuldade | Posição 1 | Posição 2 | Posição 3 |
|---------|------------|----------|-------------|-----------|-----------|-----------|
| [termo] | [número]   | [valor]  | [0-100]     | [quem]    | [quem]    | [quem]    |
```

**Nota**: Se não conseguir dados exatos de volume, usar intervalos:
- "100-500/mês"
- "1K-5K/mês"
- "10K+/mês"

---

## 4. Análise de Concorrência

### Identificação de Concorrentes

**Queries**:
```
"concorrentes de {empresa} brasil"
"{nicho} maiores empresas brasil ranking"
"top 10 {nicho} brasil"
"alternativas a {empresa}"
site:similarweb.com {domínio} competitors
```

### Meta Ad Library
- **URL**: `https://www.facebook.com/ads/library`
- **Buscar**: Nome da empresa
- **Dados**: Anúncios ativos, criativos, data de início
- **Confiabilidade**: Alta (dados do Meta)
- **Exemplo**: "Meta Ad Library mostra 15 anúncios ativos desde jan/2024"

### Google Ads Transparency Center
- **URL**: `https://adstransparency.google.com`
- **Buscar**: Nome do anunciante
- **Dados**: Anúncios ativos no Google
- **Confiabilidade**: Alta (dados do Google)

### Análise SERP

Para cada keyword transacional importante:
```
1. Buscar no Google
2. Anotar:
   - Quem aparece nos ads (topo)
   - Quem domina orgânico (1-3)
   - Tipo de conteúdo (produto, blog, landing)
```

---

## 5. Redes Sociais

### IMPORTANTE: Verificação Obrigatória

> **NUNCA assuma que uma rede social é do prospect sem verificar.**
> 
> Passos obrigatórios:
> 1. Buscar `{empresa} instagram oficial`
> 2. Verificar se o perfil menciona a marca no bio
> 3. Verificar link do site no perfil
> 4. Conferir se o conteúdo é consistente

### Instagram
- **Busca**: `{empresa} instagram` ou `site:instagram.com {empresa}`
- **Dados**: @handle, seguidores, posts, bio, link
- **Verificação**: Bio menciona a empresa? Link correto?

### LinkedIn
- **Busca**: `{empresa} linkedin company`
- **Dados**: Seguidores, funcionários, posts
- **Verificação**: Nome oficial? Setor correto?

### Facebook
- **Busca**: `{empresa} facebook página oficial`
- **Dados**: Curtidas, seguidores, reviews
- **Verificação**: Página verificada? Link do site?

### YouTube
- **Busca**: `{empresa} youtube canal oficial`
- **Dados**: Inscritos, vídeos, views
- **Verificação**: Link na descrição? Conteúdo consistente?

### TikTok
- **Busca**: `{empresa} tiktok`
- **Dados**: Seguidores, likes, vídeos
- **Verificação**: Bio menciona a marca?

### X/Twitter
- **Busca**: `{empresa} twitter oficial`
- **Dados**: Seguidores, tweets
- **Verificação**: Bio e link corretos?

---

## 6. Dados Empresariais

### Receita Federal (CNPJ)
- **Busca**: `{empresa} cnpj consulta`
- **Dados**: Razão social, sócios, capital, situação
- **Confiabilidade**: Alta (dado público oficial)
- **Uso**: Apenas para contexto, não expor dados sensíveis

### LinkedIn
- **Busca**: `{nome do CEO/fundador} {empresa} linkedin`
- **Dados**: Cargo, histórico, conexões
- **Uso**: Identificar decisores para cold call

---

## 7. SEO Avançado

### Domain Authority (Estimado)
- **Fontes**: Moz, Ahrefs (dados públicos limitados)
- **Query**: `{domínio} domain authority` ou `site:moz.com {domínio}`
- **Alternativa**: Usar Domain Rating do Ahrefs
- **Confiabilidade**: Média (métricas proprietárias)

### Backlinks
- **Query**: `site:ahrefs.com {domínio} backlinks`
- **Dados**: Número estimado de backlinks
- **Confiabilidade**: Média

---

## 8. Citações e Fontes no Deck

### Formato Padrão de Citação

```
Fonte: [Nome da Fonte] | Acesso em [Data] | Análise V4 Company
```

### Exemplos por Tipo de Dado

| Tipo de Dado | Citação |
|--------------|---------|
| Tráfego | "Fonte: SimilarWeb (dados públicos), Jan/2024" |
| Keywords | "Fonte: Pesquisa SERP + dados públicos SEMrush" |
| Tags técnicas | "Fonte: Análise técnica via BuiltWith" |
| Performance | "Fonte: PageSpeed Insights (Google)" |
| Anúncios | "Fonte: Meta Ad Library, consulta em [data]" |
| Redes sociais | "Fonte: Dados públicos das plataformas" |

### Disclaimer Recomendado (Slide 10)

```
* Dados estimados baseados em fontes públicas. 
  Números exatos podem variar.
* Análise realizada em [data].
* Para diagnóstico completo, recomenda-se 
  acesso a ferramentas premium.
```

---

## 9. Fallbacks (Quando Não Encontrar Dados)

### Hierarquia de Fallback

1. **Fonte primária indisponível** → Tentar fonte secundária
2. **Nenhuma fonte disponível** → Usar benchmark do setor
3. **Sem benchmark** → Declarar "Dados não disponíveis"

### Benchmarks por Setor (Para Referência)

| Setor | Tráfego Médio | Conversão Média | CPC Médio |
|-------|--------------|-----------------|-----------|
| E-commerce moda | 50-200K/mês | 1-3% | R$ 0,50-1,50 |
| SaaS B2B | 10-50K/mês | 2-5% | R$ 5-20 |
| Varejo físico | 20-100K/mês | 0,5-2% | R$ 0,30-1,00 |
| Serviços locais | 5-30K/mês | 3-8% | R$ 2-10 |
| Educação | 30-150K/mês | 1-4% | R$ 1-5 |

### Linguagem para Dados Estimados

✅ CORRETO:
- "Tráfego estimado entre 30-50K visitas/mês"
- "Baseado em benchmarks do setor..."
- "Dados públicos sugerem..."

❌ INCORRETO:
- "O tráfego é de 47.832 visitas" (precisão falsa)
- "Com certeza..." (sem base para certeza)
- Inventar números específicos

---

## 10. Checklist de Coleta

Antes de gerar o deck, verificar:

- [ ] Dados técnicos coletados via web_fetch
- [ ] Tecnologias verificadas via BuiltWith
- [ ] Tráfego estimado via SimilarWeb
- [ ] Keywords pesquisadas com volume
- [ ] Concorrentes identificados
- [ ] Anúncios verificados em Ad Libraries
- [ ] Redes sociais VERIFICADAS (não assumidas)
- [ ] Todas as fontes documentadas
- [ ] Nenhum dado inventado
