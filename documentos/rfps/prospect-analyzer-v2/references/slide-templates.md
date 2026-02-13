# Templates de Slides - Prospect Analyzer V2

## Estrutura Obrigatória: 10 Slides

Cada slide tem um propósito específico e elementos visuais obrigatórios.

---

## SLIDE 1: CAPA

### Layout
```
┌────────────────────────────────────────┐
│                                        │
│         [LOGO V4 COMPANY]              │
│                                        │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                        │
│    ANÁLISE DE MATURIDADE DIGITAL       │
│                                        │
│         [NOME DO PROSPECT]             │
│                                        │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                        │
│       Consultoria Gratuita             │
│           [Mês/Ano]                    │
│                                        │
└────────────────────────────────────────┘
```

### Elementos
- Fundo: Gradiente vermelho (#C41E3A → #8B0000)
- Logo V4: Topo central, branco
- Título: "ANÁLISE DE MATURIDADE DIGITAL" - Branco, bold, 44pt
- Subtítulo: Nome do prospect - Coral (#FF6B6B), 32pt
- Data: Branco, 18pt

### Não Incluir
- Agenda
- Texto excessivo
- Mais de 1 CTA

---

## SLIDE 2: RADAR DE MATURIDADE

### Layout
```
┌────────────────────────────────────────┐
│  MATURIDADE DIGITAL                    │
│                                        │
│   ┌─────────────────┐  ┌────────────┐  │
│   │                 │  │ SCORE GERAL│  │
│   │    [RADAR]      │  │            │  │
│   │   6 dimensões   │  │    5.2     │  │
│   │                 │  │            │  │
│   │                 │  │ BÁSICO     │  │
│   └─────────────────┘  └────────────┘  │
│                                        │
│   ● Data: 5  ● SEO: 6  ● Mídia: 4     │
│   ● Social: 5 ● CRM: 3 ● Tech: 4      │
│                                        │
│ ────────────────────────────────────── │
│ Fonte: Análise V4 Company | Jan 2024   │
└────────────────────────────────────────┘
```

### Elementos
- Gráfico Radar: 6 eixos (Data, SEO, Mídia, Social, CRM, Tech)
  - Cores: Linha do prospect = Coral (#FF6B6B)
  - Opcional: Linha de benchmark = Branco transparente
- Score destacado: Número grande, classificação abaixo
- Legenda: Notas individuais de cada dimensão
- Rodapé: Fonte

### Código Chart.js (Referência)
```javascript
{
  type: 'radar',
  data: {
    labels: ['Data', 'SEO', 'Mídia', 'Social', 'CRM', 'Tech'],
    datasets: [{
      label: 'Prospect',
      data: [5, 6, 4, 5, 3, 4],
      borderColor: '#FF6B6B',
      backgroundColor: 'rgba(255, 107, 107, 0.2)'
    }]
  }
}
```

---

## SLIDE 3: DIAGNÓSTICO DE DADOS

### Layout
```
┌────────────────────────────────────────┐
│  DIAGNÓSTICO: DATA & ANALYTICS         │
│                                        │
│  ┌──────────────────────────────────┐  │
│  │ ITEM              │ STATUS │NOTA │  │
│  ├──────────────────────────────────┤  │
│  │ Google Analytics 4│   ✓    │ OK  │  │
│  │ Google Tag Manager│   ✓    │ OK  │  │
│  │ Meta Pixel        │   ⚠    │PART │  │
│  │ Eventos Config.   │   ✗    │FALTA│  │
│  │ Core Web Vitals   │   ⚠    │ 65  │  │
│  │ Schema Markup     │   ✗    │FALTA│  │
│  └──────────────────────────────────┘  │
│                                        │
│  ⚠ PONTOS DE ATENÇÃO:                  │
│  • Eventos de conversão não config.    │
│  • Schema markup ausente               │
│                                        │
│ ────────────────────────────────────── │
│ Fonte: BuiltWith + PageSpeed Insights  │
└────────────────────────────────────────┘
```

### Elementos
- Tabela: 3 colunas (Item, Status, Nota)
- Status visual: ✓ (verde), ⚠ (amarelo), ✗ (vermelho)
- Box de alertas: Pontos críticos destacados
- Rodapé: Fonte específica

### Ícones de Status
- ✓ Implementado corretamente → Verde
- ⚠ Implementado parcialmente → Amarelo
- ✗ Não implementado → Vermelho

---

## SLIDE 4: DEMANDA DE MERCADO (KEYWORDS)

### Layout
```
┌────────────────────────────────────────┐
│  DEMANDA: KEYWORDS TRANSACIONAIS       │
│                                        │
│  ┌──────────────────────────────────┐  │
│  │KEYWORD      │VOL │CPC│ TOP 3    │  │
│  ├──────────────────────────────────┤  │
│  │comprar xyz  │10K │2,5│A│B│C     │  │
│  │xyz preço    │5K  │1,8│B│A│D     │  │
│  │xyz online   │3K  │2,1│C│A│B     │  │
│  │melhor xyz   │2K  │3,0│A│D│C     │  │
│  │...          │... │...│...       │  │
│  └──────────────────────────────────┘  │
│                                        │
│  💡 INSIGHT:                           │
│  "{Concorrente A} domina 60% das       │
│   keywords principais. Oportunidade    │
│   em termos de cauda longa."           │
│                                        │
│ ────────────────────────────────────── │
│ Fonte: Dados públicos SEMrush/Similar  │
└────────────────────────────────────────┘
```

### Elementos
- Tabela: Keyword, Volume, CPC, Posições 1-3
- 15-20 keywords (as mais relevantes)
- Insight box: Conclusão acionável
- Rodapé: Fonte

### Formatação da Tabela
- Header: Fundo vermelho escuro
- Linhas alternadas
- Destaque em keywords onde prospect não aparece

---

## SLIDE 5: ANÁLISE DE CONCORRÊNCIA

### Layout
```
┌────────────────────────────────────────┐
│  CONCORRÊNCIA: QUEM ESTÁ DOMINANDO?    │
│                                        │
│   ┌───────────────────────────────┐    │
│   │     ALTA PRESENÇA DIGITAL     │    │
│   │         ┌───┐                 │    │
│   │         │ A │    ┌───┐        │    │
│   │         └───┘    │ B │        │    │
│   │  BAIXO ─────────────── ALTO   │    │
│   │  INVEST.  ┌───┐       INVEST. │    │
│   │           │YOU│               │    │
│   │           └───┘               │    │
│   │     BAIXA PRESENÇA DIGITAL    │    │
│   └───────────────────────────────┘    │
│                                        │
│  TOP 3 CONCORRENTES:                   │
│  1. [Nome] - Forte em: SEO, Mídia      │
│  2. [Nome] - Forte em: Social          │
│  3. [Nome] - Forte em: CRM             │
│                                        │
│ ────────────────────────────────────── │
│ Fonte: Pesquisa de mercado V4          │
└────────────────────────────────────────┘
```

### Elementos
- Matriz 2x2: Presença Digital × Investimento
- Posicionamento do prospect vs concorrentes
- Lista dos 3 principais concorrentes
- Rodapé: Fonte

### Eixos da Matriz
- X: Investimento estimado (baixo → alto)
- Y: Presença digital (baixa → alta)

---

## SLIDE 6: SEO & GEO

### Layout
```
┌────────────────────────────────────────┐
│  SEO & GEO: VISIBILIDADE               │
│                                        │
│  ┌─────────────┐  ┌─────────────────┐  │
│  │ SEO ATUAL   │  │ GEO (IA)        │  │
│  │             │  │                 │  │
│  │ 📊 150      │  │ 🤖 O que é?     │  │
│  │ páginas     │  │                 │  │
│  │ indexadas   │  │ Presença em     │  │
│  │             │  │ respostas de    │  │
│  │ 📈 DA: ~25  │  │ ChatGPT, Claude │  │
│  │             │  │ e buscadores IA │  │
│  │ 🎯 Top 10   │  │                 │  │
│  │ em 5 kw     │  │ ⚡ Oportunidade │  │
│  └─────────────┘  └─────────────────┘  │
│                                        │
│  💡 Estratégia recomendada:            │
│  1. Content hub para keywords [X]      │
│  2. FAQ estruturado para IA            │
│  3. Schema markup completo             │
│                                        │
│ ────────────────────────────────────── │
│ Fonte: Google Search + Análise IA      │
└────────────────────────────────────────┘
```

### Elementos
- Duas colunas: SEO tradicional | GEO novo
- Métricas de SEO: páginas indexadas, DA, rankings
- Introdução ao GEO: O que é, por que importa
- Recomendações: 3 ações específicas
- Rodapé: Fonte

---

## SLIDE 7: CRM & AUTOMAÇÃO

### Layout
```
┌────────────────────────────────────────┐
│  CRM: RELACIONAMENTO & CONVERSÃO       │
│                                        │
│  DIAGNÓSTICO ATUAL:                    │
│  ┌──────────────────────────────────┐  │
│  │ • CRM identificado: [Sim/Não]   │  │
│  │ • Captura de leads: [Básica]    │  │
│  │ • Automações: [Não identificadas]│  │
│  └──────────────────────────────────┘  │
│                                        │
│  RÉGUA DE BOAS-VINDAS PROPOSTA:        │
│  ┌──────────────────────────────────┐  │
│  │ D+0 ──► D+2 ──► D+5 ──► D+7     │  │
│  │  │       │       │       │       │  │
│  │ Welcome Valor  Case   Oferta    │  │
│  │                                  │  │
│  │ D+10 ──► D+14 ──► D+21          │  │
│  │   │       │        │             │  │
│  │ Urgência Reeng. Última          │  │
│  └──────────────────────────────────┘  │
│                                        │
│ ────────────────────────────────────── │
│ Fonte: Análise de jornada V4           │
└────────────────────────────────────────┘
```

### Elementos
- Diagnóstico: Status atual do CRM
- Timeline visual: Régua de 7 emails
- Cores: Cada etapa com cor diferente
- Rodapé: Fonte

### Detalhes da Régua
| Email | Dia | Objetivo | Assunto Exemplo |
|-------|-----|----------|-----------------|
| 1 | D+0 | Boas-vindas | "Bem-vindo! Aqui está..." |
| 2 | D+2 | Valor | "3 dicas para..." |
| 3 | D+5 | Case | "Como [cliente] conseguiu..." |
| 4 | D+7 | Oferta soft | "Preparamos algo especial..." |
| 5 | D+10 | Urgência | "Últimas horas para..." |
| 6 | D+14 | Reengajamento | "Sentimos sua falta!" |
| 7 | D+21 | Última chance | "Última oportunidade..." |

---

## SLIDE 8: REDES SOCIAIS

### Layout
```
┌────────────────────────────────────────┐
│  REDES SOCIAIS: PANORAMA               │
│                                        │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐      │
│  │ 📸  │ │ 💼  │ │ 📘  │ │ 🎬  │      │
│  │ IG  │ │ LI  │ │ FB  │ │ YT  │      │
│  │     │ │     │ │     │ │     │      │
│  │ 15K │ │ 2K  │ │ 8K  │ │ 500 │      │
│  │ seg │ │ seg │ │ seg │ │ ins │      │
│  │     │ │     │ │     │ │     │      │
│  │ 3x  │ │ 1x  │ │ 2x  │ │ 1x  │      │
│  │/sem │ │/sem │ │/sem │ │/mês │      │
│  └─────┘ └─────┘ └─────┘ └─────┘      │
│                                        │
│  📊 ANÁLISE:                           │
│  • Instagram é o principal canal       │
│  • LinkedIn subutilizado               │
│  • YouTube com potencial inexplorado   │
│                                        │
│ ────────────────────────────────────── │
│ Fonte: Dados públicos das plataformas  │
└────────────────────────────────────────┘
```

### Elementos
- Grid de cards: 4-6 redes sociais
- Por rede: Ícone, seguidores, frequência
- Análise: 3 bullet points com insights
- Rodapé: Fonte

### Dados por Rede
| Rede | Métricas | Verificação |
|------|----------|-------------|
| Instagram | Seguidores, posts/sem, engajamento | Bio + link |
| LinkedIn | Seguidores, funcionários | Página oficial |
| Facebook | Curtidas, reviews | Página verificada |
| YouTube | Inscritos, views | Canal oficial |
| TikTok | Seguidores, likes | Bio + link |

---

## SLIDE 9: PLANO DE AÇÃO

### Layout
```
┌────────────────────────────────────────┐
│  PLANO DE AÇÃO: QUICK WINS             │
│                                        │
│  ┌──────────────────────────────────┐  │
│  │ #  │ AÇÃO           │IMP│ PRAZO │  │
│  ├──────────────────────────────────┤  │
│  │ 1  │ Config. eventos│🔴 │ 1 sem │  │
│  │    │ de conversão   │   │       │  │
│  │ 2  │ Implementar    │🔴 │ 2 sem │  │
│  │    │ régua CRM      │   │       │  │
│  │ 3  │ Otimizar 10    │🟡 │ 4 sem │  │
│  │    │ keywords       │   │       │  │
│  │ 4  │ Ativar LinkedIn│🟡 │ 4 sem │  │
│  │ 5  │ Schema markup  │🟢 │ 1 sem │  │
│  └──────────────────────────────────┘  │
│                                        │
│  IMPACTO ESTIMADO:                     │
│  📈 +30% conversões (após items 1-2)   │
│  📈 +50% tráfego org. (após item 3)    │
│                                        │
│ ────────────────────────────────────── │
│ Fonte: Metodologia V4 Company          │
└────────────────────────────────────────┘
```

### Elementos
- Tabela priorizada: Ação, Impacto, Prazo
- Impacto visual: 🔴 Alto, 🟡 Médio, 🟢 Baixo
- Estimativa de resultados: Conservadora
- Rodapé: Metodologia

### Critérios de Priorização
1. Quick wins: Baixo esforço, alto impacto
2. Dependências: O que precisa vir antes
3. ROI estimado: Retorno esperado

---

## SLIDE 10: PRÓXIMOS PASSOS

### Layout
```
┌────────────────────────────────────────┐
│  PRÓXIMOS PASSOS                       │
│                                        │
│                                        │
│        ┌─────────────────────┐         │
│        │                     │         │
│        │   AGENDAR REUNIÃO   │         │
│        │                     │         │
│        │   Diagnóstico       │         │
│        │   completo em       │         │
│        │   30 minutos        │         │
│        │                     │         │
│        └─────────────────────┘         │
│                                        │
│        📧 contato@v4company.com        │
│        📞 (11) XXXX-XXXX               │
│        🌐 v4company.com                │
│                                        │
│                                        │
│ ────────────────────────────────────── │
│ * Dados baseados em fontes públicas.   │
│   Diagnóstico completo requer acesso.  │
└────────────────────────────────────────┘
```

### Elementos
- CTA principal: "AGENDAR REUNIÃO"
- Contatos: Email, telefone, site
- Disclaimer: Dados baseados em fontes públicas
- Rodapé: Nota final

### CTA Alternativo
Se disponível, incluir:
- QR Code para agendamento
- Link direto para calendário

---

## Checklist de Cada Slide

Antes de finalizar, verificar em CADA slide:

- [ ] Título claro e objetivo
- [ ] Máximo 6 bullet points ou linhas de tabela
- [ ] Pelo menos 1 elemento visual (gráfico, tabela, ícone)
- [ ] Fonte citada no rodapé
- [ ] Cores da paleta V4
- [ ] Texto legível (contraste adequado)
- [ ] 1 insight principal claro

---

## Elementos Visuais CSS (Referência)

```css
/* Paleta V4 */
:root {
  --primary: #C41E3A;
  --secondary: #8B0000;
  --accent: #FF6B6B;
  --text: #FFFFFF;
  --bg-alt: #1A1A1A;
}

/* Tipografia */
h1 { font-size: 44pt; font-weight: bold; color: white; }
h2 { font-size: 32pt; color: #FF6B6B; }
p { font-size: 18pt; color: white; }

/* Tabelas */
th { background: #8B0000; color: white; }
tr:nth-child(even) { background: rgba(255,255,255,0.1); }

/* Cards */
.card {
  background: rgba(255,255,255,0.1);
  border-radius: 8px;
  padding: 16px;
}
```
