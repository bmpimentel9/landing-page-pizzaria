---
name: prospect-analyzer-v2
description: |
  Análise completa de prospects para vendas B2B da V4 Company. 
  Gera deck de 10 slides com análise técnica, keywords, concorrência, SEO/GEO, CRM e redes sociais.
  TRIGGER: Quando usuário fornecer URL para análise de prospect, consultoria gratuita, ou preparação de cold call/email.
  INPUT: Apenas a URL do prospect.
  OUTPUT: Deck PPTX profissional com até 10 slides visuais (radares, tabelas, gráficos).
---

# Prospect Analyzer V2 - Consultoria Gratuita V4 Company

## Overview

Este skill analisa prospects para preparação de cold calls e emails, gerando um deck profissional de consultoria gratuita. O objetivo é demonstrar maturidade digital do prospect e como a V4 pode ajudá-lo.

**FILOSOFIA**: Menos é mais. 10 slides no máximo. Cada slide deve ter um insight claro e acionável.

## Input Único

O skill precisa de APENAS UMA INFORMAÇÃO do usuário:

```
URL do prospect (ex: https://www.exemplo.com.br)
```

Após receber a URL, TODAS as decisões são tomadas automaticamente.

## Workflow Completo

### FASE 0: Preparação (OBRIGATÓRIO)

1. **Ler documentação de PPTX**:
   - `view /mnt/skills/public/pptx/SKILL.md`
   - `view /mnt/skills/public/pptx/html2pptx.md`
   - `view /mnt/skills/public/pptx/css.md`

2. **Ler referências deste skill**:
   - `view references/scoring-criteria.md` - Critérios de pontuação
   - `view references/data-sources.md` - Fontes de dados
   - `view references/slide-templates.md` - Templates dos slides
   - `view references/guardrails.md` - O que NÃO fazer

3. **Ler cores V4**:
   - `view assets/color-palette.txt`

### FASE 1: Coleta de Dados (Paralela)

Executar TODAS as buscas de uma vez para eficiência:

```
# Busca 1: Dados técnicos do site
web_fetch: URL do prospect (analisar HTML, meta tags, scripts)

# Busca 2: Tecnologias e tracking
web_search: "site:builtwith.com {domínio}"
web_search: "{domínio} tecnologias site analytics"

# Busca 3: Keywords e tráfego
web_search: "site:similarweb.com {domínio}"
web_search: "{domínio} palavras-chave principais"
web_search: "{nicho} keywords transacionais brasil volume"

# Busca 4: Concorrentes
web_search: "concorrentes de {empresa} brasil"
web_search: "{nicho} maiores empresas brasil ranking"

# Busca 5: SEO
web_search: "site:{domínio}" (páginas indexadas)
web_search: "{domínio} domain authority"

# Busca 6: Redes sociais
web_search: "{empresa} instagram oficial"
web_search: "{empresa} linkedin oficial"
web_search: "{empresa} facebook oficial"
web_search: "{empresa} youtube oficial"

# Busca 7: Anúncios
web_search: "site:facebook.com/ads/library {empresa}"
web_search: "site:adstransparency.google.com {empresa}"
```

### FASE 2: Análise por Especialista

O skill simula 6 diretores especialistas:

#### 2.1 DIRETOR DE DATA (Slide 2-3)
**Foco**: Mensuração e coleta de dados

Verificar e pontuar (0-10):
- [ ] Google Analytics 4 instalado e configurado
- [ ] Google Tag Manager implementado
- [ ] Meta Pixel (Facebook/Instagram)
- [ ] Google Ads Conversion Tag
- [ ] Eventos de conversão configurados
- [ ] Enhanced e-commerce (se aplicável)
- [ ] Core Web Vitals (LCP, FID, CLS)
- [ ] Schema markup
- [ ] Hotjar/Clarity/ferramentas de heatmap

**Output**: Radar de maturidade de dados + slide detalhando cada item

#### 2.2 DIRETOR DE PERFORMANCE (Slide 4)
**Foco**: Demanda e keywords transacionais

Identificar 25 keywords transacionais:
| Keyword | Volume/mês | CPC (R$) | Posição 1 | Posição 2 | Posição 3 |
|---------|-----------|----------|-----------|-----------|-----------|
| [termo] | [número]  | [valor]  | [quem]    | [quem]    | [quem]    |

**Critérios para seleção de keywords**:
- Alta intenção de compra
- Volume mínimo 100/mês
- Relevância direta para o negócio
- Mix de head, middle e long tail

**Output**: Tabela visual com 25 keywords + oportunidades

#### 2.3 DIRETOR DE MERCADO (Slide 5)
**Foco**: Análise regional e concorrência

Mapear:
- Região foco do prospect
- 3 principais concorrentes na região
- Share of voice estimado
- Quem está comprando as keywords transacionais
- Gaps de mercado

**Output**: Mapa de concorrência + análise SWOT simplificada

#### 2.4 DIRETOR DE SEO/GEO (Slide 6)
**Foco**: Visibilidade orgânica tradicional e em LLMs

**SEO Tradicional**:
- Páginas indexadas
- Domain Authority estimado
- Posicionamento em keywords principais
- Oportunidades de conteúdo

**GEO (Generative Engine Optimization)**:
- Presença em respostas de IA (ChatGPT, Claude, Perplexity)
- Citações e menções em fontes de treinamento
- Oportunidades de aparecer em respostas generativas
- Estratégia de Answer Engine Optimization

**Output**: Dashboard SEO + introdução ao GEO

#### 2.5 DIRETOR DE CRM (Slide 7)
**Foco**: Relacionamento e automação

Analisar:
- Presença de CRM identificável
- Captura de leads (popups, formulários, newsletter)
- Automações de email visíveis
- Estratégia de relacionamento aparente

Propor:
- Régua de boas-vindas (5-7 emails)
  1. Email 1 (D+0): Boas-vindas + entrega do prometido
  2. Email 2 (D+2): Valor educacional
  3. Email 3 (D+5): Case de sucesso
  4. Email 4 (D+7): Oferta soft
  5. Email 5 (D+10): Urgência/escassez
  6. Email 6 (D+14): Reengajamento
  7. Email 7 (D+21): Última chance

**Output**: Diagnóstico CRM + régua de boas-vindas visual

#### 2.6 DIRETOR DE SOCIAL (Slide 8)
**Foco**: Presença em redes sociais

Mapear e analisar:
- Instagram: @handle, seguidores, frequência, engajamento
- LinkedIn: página empresa, seguidores, posts
- Facebook: página, seguidores, reviews
- YouTube: canal, inscritos, views
- TikTok: perfil, seguidores
- X/Twitter: perfil, seguidores

**IMPORTANTE**: Verificar se as redes são REALMENTE do prospect. Não assumir.

**Output**: Panorama de redes + oportunidades

### FASE 3: Consolidação

#### 3.1 Score de Maturidade Digital

```
Score Geral = Média ponderada:
- Data/Analytics: 25%
- Performance/Keywords: 20%
- SEO: 20%
- Social: 15%
- CRM: 10%
- Inovação: 10%
```

**Classificação**:
| Score | Nível | Ação Sugerida |
|-------|-------|---------------|
| 0-3 | Iniciante | Estruturação completa |
| 4-5 | Básico | Quick wins urgentes |
| 6-7 | Intermediário | Otimização avançada |
| 8-9 | Avançado | Refinamento e escala |
| 10 | Expert | Manutenção e inovação |

### FASE 4: Geração do Deck

**ESTRUTURA OBRIGATÓRIA (10 slides)**:

```
SLIDE 1: CAPA
- Logo V4 Company (vermelho)
- "Análise de Maturidade Digital"
- Nome do prospect
- Data
- "Consultoria Gratuita"

SLIDE 2: RADAR DE MATURIDADE
- Gráfico radar comparando 6 dimensões
- Score geral destacado
- Benchmark vs mercado
- Fonte: Análise V4 Company

SLIDE 3: DIAGNÓSTICO DE DADOS
- Checklist visual de tags/pixels
- Nota por item
- Pontos de atenção em destaque
- Fonte: Análise técnica via BuiltWith, PageSpeed Insights

SLIDE 4: DEMANDA DE MERCADO (KEYWORDS)
- Tabela com 15-20 keywords (as mais relevantes)
- Volume, CPC, quem domina
- Oportunidades destacadas
- Fonte: Estimativas baseadas em dados públicos de SEMrush/SimilarWeb

SLIDE 5: ANÁLISE DE CONCORRÊNCIA
- 3 principais concorrentes
- Matriz de posicionamento
- Quem está comprando demanda
- Fonte: Pesquisa de mercado V4

SLIDE 6: SEO & GEO
- Métricas de SEO atual
- Introdução ao GEO
- Oportunidades em IA
- Fonte: Google Search, análise de IA generativa

SLIDE 7: CRM & AUTOMAÇÃO
- Diagnóstico atual
- Régua de boas-vindas proposta
- Potencial de conversão
- Fonte: Análise de jornada do usuário

SLIDE 8: REDES SOCIAIS
- Panorama das redes identificadas
- Métricas principais
- Gaps vs concorrentes
- Fonte: Dados públicos das plataformas

SLIDE 9: PLANO DE AÇÃO
- 5 quick wins priorizados
- Impacto estimado
- Timeline sugerido
- Fonte: Metodologia V4 Company

SLIDE 10: PRÓXIMOS PASSOS
- CTA para reunião
- Contato V4 Company
- QR Code para agendamento (opcional)
```

### FASE 5: Produção Visual

**ANTES DE CRIAR OS SLIDES**:
1. Ler `/mnt/skills/public/pptx/SKILL.md` completamente
2. Ler `/mnt/skills/public/pptx/html2pptx.md` completamente
3. Ler `/mnt/skills/public/pptx/css.md` completamente

**USAR**: Workflow html2pptx conforme documentação do skill de PPTX

**PALETA DE CORES**:
- Primário: #C41E3A (Vermelho V4)
- Secundário: #8B0000 (Vermelho escuro)
- Acento: #FF6B6B (Coral)
- Texto: #FFFFFF (Branco)
- Fundo alternativo: #1A1A1A (Preto)

**ELEMENTOS VISUAIS OBRIGATÓRIOS**:
- Slide 2: Gráfico radar (Chart.js)
- Slide 3: Checklist visual ou tabela
- Slide 4: Tabela de keywords
- Slide 5: Matriz 2x2 de concorrência
- Slide 6: Dashboard com métricas
- Slide 7: Timeline visual da régua
- Slide 8: Grid de redes sociais
- Slide 9: Lista priorizada

**RODAPÉ EM TODOS OS SLIDES**:
```
Fonte: [especificar fonte] | Análise V4 Company | Data: [data atual]
```

### FASE 6: Validação Final

**CHECKLIST OBRIGATÓRIO**:
- [ ] Todos os dados são verificáveis
- [ ] Nenhum dado foi inventado
- [ ] Fontes citadas em cada slide
- [ ] Máximo 10 slides
- [ ] Cada slide tem insight claro
- [ ] Visual consistente
- [ ] Cores V4 aplicadas
- [ ] Rodapé em todos os slides

**VALIDAÇÃO VISUAL**:
```bash
# Converter para PDF e imagens
soffice --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide

# Verificar cada slide visualmente
```

## Guardrails (O QUE NÃO FAZER)

Ver `references/guardrails.md` para lista completa.

**CRÍTICO**:
1. ❌ NUNCA inventar dados de tráfego, volume ou métricas
2. ❌ NUNCA assumir redes sociais sem verificar
3. ❌ NUNCA usar mais de 10 slides
4. ❌ NUNCA omitir fontes
5. ❌ NUNCA usar cores fora da paleta V4

## Fontes de Dados Aceitas

Ver `references/data-sources.md` para lista completa.

**CONFIÁVEIS**:
- SimilarWeb (dados públicos)
- SEMrush (dados públicos)
- BuiltWith
- PageSpeed Insights
- Google Search (site:)
- Meta Ad Library
- Google Ads Transparency
- Redes sociais (dados públicos)

**NÃO ACEITAS**:
- Estimativas sem base
- "Parece que..."
- Dados desatualizados
- Fontes não verificáveis

## Exemplo de Execução

```
USUÁRIO: Analise https://www.marca-exemplo.com.br

CLAUDE:
1. ✅ Leu documentação PPTX
2. ✅ Leu referências do skill
3. ✅ Executou 7+ buscas paralelas
4. ✅ Analisou como 6 diretores
5. ✅ Consolidou scores
6. ✅ Gerou deck 10 slides
7. ✅ Validou visualmente
8. ✅ Entregou arquivo PPTX

OUTPUT: prospect-analysis-marca-exemplo-[data].pptx
```

## Integração com Outros Skills

Este skill DEVE usar:
- `/mnt/skills/public/pptx/` - Para geração do deck
- `/mnt/skills/user/professional-slides/` - Para padrões visuais V4

## Métricas de Qualidade

**Deck bem-sucedido**:
- Cliente entende sua maturidade em < 2 min
- Pelo menos 3 insights acionáveis
- Sem objeções sobre credibilidade
- Call-to-action claro

**Red flags**:
- Cliente questiona dados
- Slides genéricos sem especificidade
- Falta de fonte em qualquer slide
- Visual inconsistente
