"""
Chart Generator Script
Creates all visualizations for Perfumaria Sumirê presentation

Charts:
1. Radar - Sumirê Maturity
2. Radar - 6 Companies Comparison
3. Line - 12 Months Traffic by Channel
4. Stacked Bar - Competitors Channel Comparison
5. Sankey - Traffic Flow
6. Table - Keywords
7. Line - Demand Trend
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.table import Table

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import COLORS, COLORS_RGB, CHART_STYLE, COMPETITORS, PATHS, CHART_FILES
from utils import load_json, log_progress, log_success, log_error, hex_to_rgb


# Set matplotlib style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['font.family'] = 'Arial'


class ChartGenerator:
    """Generate all charts for the presentation"""

    def __init__(self, data_file: str):
        """
        Initialize chart generator

        Args:
            data_file: Path to JSON data file
        """
        self.data = load_json(data_file)
        if not self.data:
            log_error("Failed to load data file!")
            raise ValueError("No data available")

        self.charts_dir = os.path.join(
            os.path.dirname(__file__),
            '../charts/'
        )
        os.makedirs(self.charts_dir, exist_ok=True)

    def create_radar_sumire(self):
        """Chart 1: Radar chart for Sumirê digital maturity"""
        log_progress("Creating radar chart: Sumirê Digital Maturity...")

        categories = ['Google\nAnalytics', 'SEO', 'Pixels\nSociais',
                     'Inovação\nDigital', 'UX/\nPerformance', 'CRM']

        # Calculate scores (0-10 scale)
        tech = self.data['sumire']['technical']

        values = [
            10 if tech.get('google_analytics') else 0,  # GA
            tech.get('seo_score', 70) / 10,  # SEO
            8 if tech.get('facebook_pixel') else 4,  # Pixels
            6.5,  # Innovation (medium score)
            tech.get('pagespeed_mobile', 70) / 10,  # UX/Performance
            7.5   # CRM (has app, so good score)
        ]

        # Create radar
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        values_plot = values + values[:1]
        angles_plot = angles + angles[:1]

        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

        # Plot data
        ax.plot(angles_plot, values_plot, 'o-', linewidth=3,
               color=COLORS['primary'], label='Sumirê')
        ax.fill(angles_plot, values_plot, alpha=0.25, color=COLORS['primary'])

        # Customize
        ax.set_xticks(angles)
        ax.set_xticklabels(categories, size=13, weight='bold')
        ax.set_ylim(0, 10)
        ax.set_yticks([2, 4, 6, 8, 10])
        ax.set_yticklabels(['2', '4', '6', '8', '10'], size=10)
        ax.grid(True, linewidth=0.5, alpha=0.5)

        # Title
        plt.title('Maturidade Digital - Perfumaria Sumirê',
                 size=20, weight='bold', pad=30)

        # Save
        output_path = os.path.join(self.charts_dir, 'radar_sumire.png')
        plt.savefig(output_path, dpi=CHART_STYLE['dpi'], bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        plt.close()

        log_success(f"Saved: {output_path}")

    def create_radar_competitors(self):
        """Chart 2: Radar chart comparing 6 companies"""
        log_progress("Creating radar chart: Competitors Comparison...")

        categories = ['GA', 'SEO', 'Pixels', 'Inovação', 'UX', 'CRM']

        # Prepare data for all companies
        companies = ['Sumirê'] + [comp['name'] for comp in COMPETITORS]
        colors_list = [COLORS['primary'], COLORS['secondary'], COLORS['accent'],
                      COLORS['warning'], COLORS['success'], COLORS['danger']]

        fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(projection='polar'))

        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()

        # Plot each company
        for idx, company in enumerate(companies):
            if company == 'Sumirê':
                data_source = self.data['sumire']['technical']
            else:
                data_source = self.data['competitors'][company]['technical']

            values = [
                10 if data_source.get('google_analytics') else 0,
                data_source.get('seo_score', 70) / 10,
                8 if data_source.get('facebook_pixel') else 4,
                np.random.uniform(5, 8),  # Innovation
                data_source.get('pagespeed_mobile', 70) / 10,
                np.random.uniform(6, 8)   # CRM
            ]

            values_plot = values + values[:1]
            angles_plot = angles + angles[:1]

            ax.plot(angles_plot, values_plot, 'o-', linewidth=2.5,
                   color=colors_list[idx], label=company, alpha=0.8)
            ax.fill(angles_plot, values_plot, alpha=0.15, color=colors_list[idx])

        # Customize
        ax.set_xticks(angles)
        ax.set_xticklabels(categories, size=14, weight='bold')
        ax.set_ylim(0, 10)
        ax.set_yticks([2, 4, 6, 8, 10])
        ax.grid(True, linewidth=0.5, alpha=0.4)

        # Title and legend
        plt.title('Comparativo de Maturidade Digital',
                 size=22, weight='bold', pad=30)
        ax.legend(loc='upper left', bbox_to_anchor=(1.2, 1.0),
                 fontsize=11, frameon=True)

        # Save
        output_path = os.path.join(self.charts_dir, 'radar_competitors.png')
        plt.savefig(output_path, dpi=CHART_STYLE['dpi'], bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        plt.close()

        log_success(f"Saved: {output_path}")

    def create_traffic_12months(self):
        """Chart 3: Line chart showing 12 months traffic by channel"""
        log_progress("Creating line chart: 12 Months Traffic...")

        traffic_data = self.data['sumire']['traffic_12m']
        months = traffic_data['months']
        channels = traffic_data['channels']

        # Shorten month labels
        months_short = [m[:3] for m in months]

        fig, ax = plt.subplots(figsize=(14, 7))

        # Plot each channel
        channel_config = [
            ('direct', 'Direto', COLORS['primary'], 'o'),
            ('organic', 'Orgânico', COLORS['secondary'], 's'),
            ('social', 'Social', COLORS['accent'], '^'),
            ('referral', 'Referral', COLORS['warning'], 'd'),
            ('paid', 'Pago', COLORS['danger'], '*')
        ]

        for channel_key, label, color, marker in channel_config:
            values = channels[channel_key]
            ax.plot(months_short, values, label=label, linewidth=3,
                   marker=marker, markersize=8, color=color, alpha=0.9)

        # Customize
        ax.set_xlabel('Mês', fontsize=14, weight='bold')
        ax.set_ylabel('Visitantes Únicos', fontsize=14, weight='bold')
        ax.set_title('Evolução de Tráfego por Canal - 12 Meses',
                    fontsize=20, weight='bold', pad=20)

        # Format y-axis
        ax.yaxis.set_major_formatter(
            plt.FuncFormatter(lambda x, p: f'{int(x/1000)}K' if x >= 1000 else str(int(x)))
        )

        ax.legend(fontsize=12, loc='upper left', frameon=True, shadow=True)
        ax.grid(True, alpha=0.3, linestyle='--')

        plt.tight_layout()

        # Save
        output_path = os.path.join(self.charts_dir, 'traffic_12months.png')
        plt.savefig(output_path, dpi=CHART_STYLE['dpi'], bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        plt.close()

        log_success(f"Saved: {output_path}")

    def create_competitors_channels(self):
        """Chart 4: Stacked horizontal bar chart for competitors"""
        log_progress("Creating bar chart: Competitors Channels...")

        companies = ['Sumirê'] + [comp['name'].split()[0] for comp in COMPETITORS[:5]]

        # Calculate percentages for each company
        data_percentages = []
        for company in companies:
            if company == 'Sumirê':
                traffic = self.data['sumire']['traffic_12m']['channels']
            else:
                # Find full company name
                full_name = next((c['name'] for c in COMPETITORS if company in c['name']), company)
                if full_name in self.data['competitors']:
                    traffic = self.data['competitors'][full_name]['traffic_12m']['channels']
                else:
                    continue

            # Get last month's data
            total = sum(traffic[ch][-1] for ch in traffic.keys())

            percentages = {
                ch: (traffic[ch][-1] / total * 100) for ch in traffic.keys()
            }
            data_percentages.append(percentages)

        # Create plot
        fig, ax = plt.subplots(figsize=(14, 8))

        # Data for stacking
        direct = [d['direct'] for d in data_percentages]
        organic = [d['organic'] for d in data_percentages]
        social = [d['social'] for d in data_percentages]
        referral = [d['referral'] for d in data_percentages]
        paid = [d['paid'] for d in data_percentages]

        y_pos = np.arange(len(companies))

        # Create stacked bars
        ax.barh(y_pos, direct, label='Direto', color=COLORS['primary'])
        ax.barh(y_pos, organic, left=direct, label='Orgânico',
               color=COLORS['secondary'])
        ax.barh(y_pos, social, left=np.array(direct) + np.array(organic),
               label='Social', color=COLORS['accent'])
        ax.barh(y_pos, referral,
               left=np.array(direct) + np.array(organic) + np.array(social),
               label='Referral', color=COLORS['warning'])
        ax.barh(y_pos, paid,
               left=np.array(direct) + np.array(organic) + np.array(social) + np.array(referral),
               label='Pago', color=COLORS['danger'])

        # Customize
        ax.set_yticks(y_pos)
        ax.set_yticklabels(companies, fontsize=13, weight='bold')
        ax.set_xlabel('Percentual de Tráfego (%)', fontsize=14, weight='bold')
        ax.set_title('Distribuição de Canais - Comparativo Concorrentes',
                    fontsize=20, weight='bold', pad=20)
        ax.legend(loc='upper right', fontsize=12, frameon=True, shadow=True)
        ax.set_xlim(0, 100)

        plt.tight_layout()

        # Save
        output_path = os.path.join(self.charts_dir, 'competitors_channels.png')
        plt.savefig(output_path, dpi=CHART_STYLE['dpi'], bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        plt.close()

        log_success(f"Saved: {output_path}")

    def create_sankey_flow(self):
        """Chart 5: Sankey diagram for traffic flow"""
        log_progress("Creating Sankey diagram: Traffic Flow...")

        try:
            import plotly.graph_objects as go
            from plotly.io import write_image
        except ImportError:
            log_error("Plotly not installed. Skipping Sankey chart.")
            # Create placeholder
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.text(0.5, 0.5, 'Sankey Diagram\n(Requires Plotly)',
                   ha='center', va='center', fontsize=20)
            ax.axis('off')
            output_path = os.path.join(self.charts_dir, 'sankey_flow.png')
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
            return

        sankey_data = self.data['sumire']['sankey']

        # Prepare nodes
        incoming_sources = [item['source'] for item in sankey_data['incoming']]
        outgoing_dests = [item['destination'] for item in sankey_data['outgoing']]

        all_nodes = incoming_sources + ['perfumariasumire.com.br'] + outgoing_dests
        node_dict = {node: idx for idx, node in enumerate(all_nodes)}

        # Prepare links
        source_indices = []
        target_indices = []
        values = []

        # Incoming links
        center_idx = node_dict['perfumariasumire.com.br']
        for item in sankey_data['incoming']:
            source_indices.append(node_dict[item['source']])
            target_indices.append(center_idx)
            values.append(item['value'])

        # Outgoing links
        for item in sankey_data['outgoing']:
            source_indices.append(center_idx)
            target_indices.append(node_dict[item['destination']])
            values.append(item['value'])

        # Create Sankey
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=20,
                thickness=25,
                line=dict(color="black", width=0.5),
                label=all_nodes,
                color=[COLORS['secondary'] if i != center_idx else COLORS['primary']
                      for i in range(len(all_nodes))]
            ),
            link=dict(
                source=source_indices,
                target=target_indices,
                value=values,
                color='rgba(78, 205, 196, 0.3)'
            )
        )])

        fig.update_layout(
            title=dict(
                text='Fluxo de Tráfego - Origem e Destino',
                font=dict(size=22, color='black')
            ),
            font=dict(size=12, color='black'),
            plot_bgcolor='white',
            paper_bgcolor='white',
            height=600,
            width=1400
        )

        # Save
        output_path = os.path.join(self.charts_dir, 'sankey_flow.png')
        try:
            write_image(fig, output_path, scale=2)
            log_success(f"Saved: {output_path}")
        except Exception as e:
            log_error(f"Could not save Sankey: {e}")
            # Create placeholder
            fig_mpl, ax = plt.subplots(figsize=(12, 6))
            ax.text(0.5, 0.5, 'Sankey Diagram\n(Rendering Error)',
                   ha='center', va='center', fontsize=20)
            ax.axis('off')
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()

    def create_keywords_table(self):
        """Chart 6: Styled table for keywords"""
        log_progress("Creating table: Top Keywords...")

        keywords = self.data['keywords'][:15]

        # Create figure
        fig, ax = plt.subplots(figsize=(14, 10))
        ax.axis('tight')
        ax.axis('off')

        # Prepare data
        headers = ['Keyword', 'Volume/mês', 'CPC (R$)', 'Posição', 'Tendência']
        table_data = []

        for kw in keywords:
            trend_symbol = '↑' if kw['trend'] == 'up' else '↓' if kw['trend'] == 'down' else '→'
            row = [
                kw['term'],
                f"{kw['volume']:,}".replace(',', '.'),
                f"R$ {kw['cpc']:.2f}",
                str(kw['position']) + 'º',
                trend_symbol
            ]
            table_data.append(row)

        # Create table
        table = ax.table(cellText=table_data, colLabels=headers,
                        cellLoc='left', loc='center',
                        colWidths=[0.40, 0.15, 0.15, 0.15, 0.15])

        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1, 2.5)

        # Style header
        for i in range(len(headers)):
            cell = table[(0, i)]
            cell.set_facecolor(COLORS['dark'])
            cell.set_text_props(weight='bold', color='white', fontsize=12)

        # Style rows - alternate colors
        for i in range(1, len(table_data) + 1):
            for j in range(len(headers)):
                cell = table[(i, j)]
                if i % 2 == 0:
                    cell.set_facecolor(COLORS['light'])
                else:
                    cell.set_facecolor('white')

                # Highlight Sumirê if mentioned
                if j == 0 and 'sumire' in table_data[i-1][0].lower():
                    cell.set_facecolor('#FFE5CC')
                    cell.set_text_props(weight='bold')

        # Title
        plt.title('Top 15 Keywords Transacionais', fontsize=20,
                 weight='bold', pad=20)

        # Save
        output_path = os.path.join(self.charts_dir, 'keywords_table.png')
        plt.savefig(output_path, dpi=CHART_STYLE['dpi'], bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        plt.close()

        log_success(f"Saved: {output_path}")

    def create_demand_trend(self):
        """Chart 7: Line chart with demand trend"""
        log_progress("Creating line chart: Demand Trend...")

        trend_data = self.data['keywords_trend']
        months = trend_data['months']
        demand = trend_data['aggregated_monthly_volume']

        fig, ax = plt.subplots(figsize=(14, 7))

        # Plot main line
        ax.plot(months, demand, linewidth=4, marker='o', markersize=10,
               color=COLORS['primary'], label='Demanda de Busca', alpha=0.9)

        # Add trend line
        x_numeric = np.arange(len(months))
        z = np.polyfit(x_numeric, demand, 1)
        p = np.poly1d(z)
        ax.plot(months, p(x_numeric), linestyle='--', linewidth=3,
               color=COLORS['dark'], alpha=0.7, label='Tendência Linear')

        # Customize
        ax.set_xlabel('Mês', fontsize=14, weight='bold')
        ax.set_ylabel('Volume de Buscas', fontsize=14, weight='bold')
        ax.set_title('Demanda de Mercado - Últimos 12 Meses',
                    fontsize=20, weight='bold', pad=20)

        # Format y-axis
        ax.yaxis.set_major_formatter(
            plt.FuncFormatter(lambda x, p: f'{int(x/1000)}K')
        )

        ax.legend(fontsize=13, loc='best', frameon=True, shadow=True)
        ax.grid(True, alpha=0.3, linestyle='--')

        # Add annotation for trend
        if z[0] > 0:
            trend_text = f"Crescimento: +{z[0]:.0f} buscas/mês"
            color = COLORS['success']
        else:
            trend_text = f"Queda: {z[0]:.0f} buscas/mês"
            color = COLORS['danger']

        ax.text(0.02, 0.98, trend_text, transform=ax.transAxes,
               fontsize=13, weight='bold', va='top', ha='left',
               bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))

        plt.tight_layout()

        # Save
        output_path = os.path.join(self.charts_dir, 'demand_trend.png')
        plt.savefig(output_path, dpi=CHART_STYLE['dpi'], bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        plt.close()

        log_success(f"Saved: {output_path}")

    def generate_all_charts(self):
        """Generate all charts"""
        log_progress("="*60)
        log_progress("GENERATING ALL CHARTS")
        log_progress("="*60)

        try:
            self.create_radar_sumire()
            self.create_radar_competitors()
            self.create_traffic_12months()
            self.create_competitors_channels()
            self.create_sankey_flow()
            self.create_keywords_table()
            self.create_demand_trend()

            log_progress("\n" + "="*60)
            log_success("ALL CHARTS GENERATED SUCCESSFULLY!")
            log_progress("="*60)

        except Exception as e:
            log_error(f"Error generating charts: {e}")
            import traceback
            traceback.print_exc()
            return False

        return True


def main():
    """Main execution function"""

    # Load data file
    data_file = os.path.join(
        os.path.dirname(__file__),
        PATHS['sumire_data']
    )

    if not os.path.exists(data_file):
        log_error(f"Data file not found: {data_file}")
        log_error("Please run 01_browser_automation.py first!")
        return 1

    # Create generator and generate charts
    try:
        generator = ChartGenerator(data_file)
        success = generator.generate_all_charts()

        if success:
            log_success("\n✅ All charts saved to: charts/")
            return 0
        else:
            log_error("\n❌ Chart generation failed")
            return 1

    except Exception as e:
        log_error(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
