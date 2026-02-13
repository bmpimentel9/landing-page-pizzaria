# 🍕 Landing Page - Pizzaria Sabor & Delivery

Landing page de alta conversão para captura de leads (email e WhatsApp) com ofertas exclusivas.

## ✨ Funcionalidades

- **Formulário 2 passos**: Captura email (15% OFF) → WhatsApp (cardápio)
- **Contador regressivo**: Cria urgência com timer de 2 horas
- **Popup de abandono**: Aparece após 10 segundos se o usuário não converteu
- **Botão WhatsApp flutuante**: Chat rápido no canto da tela
- **SEO otimizado**: Meta tags, Open Graph, Schema.org
- **Analytics**: Google Analytics 4 + Meta Pixel
- **Validação de formulários**: Feedback visual para o usuário
- **Responsivo**: Mobile-first design
- **Integração Google Sheets**: Salva leads automaticamente
- **UTM tracking**: Rastreia origem do tráfego

## 🚀 Deploy no Vercel

```bash
# 1. Instale o Vercel CLI
npm i -g vercel

# 2. Faça login
vercel login

# 3. Deploy
vercel

# Ou conecte o repositório no https://vercel.com
```

## ⚙️ Configuração

### 1. Google Sheets (Captura de Leads)

1. Crie uma planilha no Google Sheets
2. Acesse Google Forms → Criar formulário
3. Adicione os campos:
   - Email (texto)
   - WhatsApp (texto)
   - UTM Source (texto)
   - UTM Medium (texto)
   - UTM Campaign (texto)
4. Vá em Configurações → Coletar nomes → Desativado
5. Vá em Respostas → Vincular a uma nova planilha
6. Copie o ID da planilha (está na URL: `/d/[ID_DA_PLANILHA]/edit`)
7. No formulário, clique em "Enviar" → "Incorporar" → Copie a URL
8. No código `index.html`, linha ~450, substitua:
   ```javascript
   const GOOGLE_SHEETS_FORM_URL = 'https://docs.google.com/forms/d/YOUR_FORM_ID/formResponse';
   ```
9. Descubra os IDs dos campos (entry.xxx) - use o Inspect do navegador no formulário incorporado

### 2. Google Analytics 4

Substitua `G-XXXXXXXXXX` pelo seu ID GA4 (linha ~40):
```javascript
gtag('config', 'G-SEU_ID_AQUI');
```

### 3. Meta Pixel (Facebook)

Substitua `YOUR_PIXEL_ID` pelo seu ID do Pixel (linha ~50):
```javascript
fbq('init', 'SEU_PIXEL_ID_AQUI');
```

### 4. WhatsApp

Substitua o número em todas as ocorrências (linha ~452):
```javascript
const WHATSAPP_NUMBER = '5511999999999'; // Código país + DDD + número
```

### 5. URL do Site

Atualize o canonical e OG URL (linhas 15, 20):
```html
<link rel="canonical" href="https://seudominio.com.br">
<meta property="og:url" content="https://seudominio.com.br">
```

## 📊 UTM Parameters

Use para rastrear campanhas:
```
https://seudominio.com.br/?utm_source=facebook&utm_medium=cpc&utm_campaign=promocao_pizza
```

## 🎨 Customização

### Cores
Edite no `:root` (linha ~12):
```css
:root {
    --red-primary: #E53935;
    --gold: #FFB300;
    --dark: #1A1A1A;
}
```

### Imagens
Substitua a URL da pizza (linha ~232):
```html
<img src="SUA_IMAGEM_AQUI" alt="Pizza">
```

## 📁 Estrutura

```
landing-page-pizzaria/
├── index.html      # Landing page completa
├── vercel.json     # Configuração Vercel
├── README.md       # Este arquivo
└── PRD_Landing_Pizzaria.md  # Documento de requisitos
```

## 📄 Licença

MIT

---

Feito com ❤️ para Pizzaria Sabor & Delivery
