import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# بياناتك من الصورة
data = [
    # Selection Sort
    {"Algorithm": "Selection", "Type": "Asc", "Size": 100, "Comparisons": 4950, "Displacements": 0, "Time": 0.001001},
    {"Algorithm": "Selection", "Type": "Const", "Size": 100, "Comparisons": 4950, "Displacements": 0, "Time": 0.000000},
    {"Algorithm": "Selection", "Type": "Desc", "Size": 100, "Comparisons": 4950, "Displacements": 50, "Time": 0.000000},

    # Bubble Sort
    {"Algorithm": "Bubble", "Type": "Asc", "Size": 100, "Comparisons": 4950, "Displacements": 0, "Time": 0.000000},
    {"Algorithm": "Bubble", "Type": "Const", "Size": 100, "Comparisons": 4950, "Displacements": 0, "Time": 0.000998},
    {"Algorithm": "Bubble", "Type": "Desc", "Size": 100, "Comparisons": 4950, "Displacements": 4950, "Time": 0.000000},

    # Larger sizes
    {"Algorithm": "Selection", "Type": "Asc", "Size": 1000, "Comparisons": 499500, "Displacements": 0,
     "Time": 0.024003},
    {"Algorithm": "Selection", "Type": "Const", "Size": 1000, "Comparisons": 499500, "Displacements": 0,
     "Time": 0.023508},
    {"Algorithm": "Selection", "Type": "Desc", "Size": 1000, "Comparisons": 499500, "Displacements": 500,
     "Time": 0.023002},

    {"Algorithm": "Bubble", "Type": "Asc", "Size": 1000, "Comparisons": 499500, "Displacements": 0, "Time": 0.026997},
    {"Algorithm": "Bubble", "Type": "Const", "Size": 1000, "Comparisons": 499500, "Displacements": 0, "Time": 0.026002},
    {"Algorithm": "Bubble", "Type": "Desc", "Size": 1000, "Comparisons": 499500, "Displacements": 499500,
     "Time": 0.066504},

    {"Algorithm": "Selection", "Type": "Asc", "Size": 10000, "Comparisons": 49995000, "Displacements": 0,
     "Time": 2.313800},
    {"Algorithm": "Selection", "Type": "Const", "Size": 10000, "Comparisons": 49995000, "Displacements": 0,
     "Time": 2.627824},
]


def create_performance_charts():
    """إنشاء الرسوم البيانية للأداء"""

    # تحويل البيانات إلى DataFrame
    df = pd.DataFrame(data)

    # 1. مخطط وقت التنفيذ للمقارنة
    plt.figure(figsize=(12, 8))

    # تجميع البيانات حسب الخوارزمية والحجم
    algorithms = df['Algorithm'].unique()
    sizes = df['Size'].unique()
    colors = {'Selection': '#FF6B6B', 'Bubble': '#4ECDC4'}
    markers = {'Asc': 'o', 'Const': 's', 'Desc': '^'}

    for algo in algorithms:
        algo_data = df[df['Algorithm'] == algo]
        for data_type in ['Asc', 'Desc']:
            type_data = algo_data[algo_data['Type'] == data_type]
            if len(type_data) > 0:
                plt.plot(type_data['Size'], type_data['Time'],
                         marker=markers[data_type], color=colors[algo],
                         linewidth=2, markersize=8,
                         label=f'{algo} {data_type}')

    plt.xlabel('حجم البيانات', fontsize=12, fontweight='bold')
    plt.ylabel('وقت التنفيذ (ثانية)', fontsize=12, fontweight='bold')
    plt.title('مقارنة أداء خوارزميات الفرز', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

    # 2. مخطط عدد المقارنات
    plt.figure(figsize=(12, 8))

    for algo in algorithms:
        algo_data = df[df['Algorithm'] == algo]
        for data_type in ['Asc', 'Desc']:
            type_data = algo_data[algo_data['Type'] == data_type]
            if len(type_data) > 0:
                plt.plot(type_data['Size'], type_data['Comparisons'],
                         marker=markers[data_type], color=colors[algo],
                         linewidth=2, markersize=8,
                         label=f'{algo} {data_type}')

    plt.xlabel('حجم البيانات', fontsize=12, fontweight='bold')
    plt.ylabel('عدد المقارنات', fontsize=12, fontweight='bold')
    plt.title('عدد المقارنات في خوارزميات الفرز', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('comparisons_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

    # 3. مخطط عدد التبديلات
    plt.figure(figsize=(12, 8))

    for algo in algorithms:
        algo_data = df[df['Algorithm'] == algo]
        for data_type in ['Asc', 'Desc']:
            type_data = algo_data[algo_data['Type'] == data_type]
            if len(type_data) > 0:
                plt.plot(type_data['Size'], type_data['Displacements'],
                         marker=markers[data_type], color=colors[algo],
                         linewidth=2, markersize=8,
                         label=f'{algo} {data_type}')

    plt.xlabel('حجم البيانات', fontsize=12, fontweight='bold')
    plt.ylabel('عدد التبديلات', fontsize=12, fontweight='bold')
    plt.title('عدد التبديلات في خوارزميات الفرز', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('displacements_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

    # 4. مخطط أعمدة للأداء
    plt.figure(figsize=(10, 6))

    # تجميع أوقات التنفيذ للحجم 1000
    times_1000 = []
    labels = []

    for algo in algorithms:
        for data_type in ['Asc', 'Desc']:
            time_data = df[(df['Algorithm'] == algo) & (df['Type'] == data_type) & (df['Size'] == 1000)]
            if len(time_data) > 0:
                times_1000.append(time_data['Time'].values[0])
                labels.append(f'{algo}\n{data_type}')

    colors_bars = ['#FF6B6B', '#FF9999', '#4ECDC4', '#88D8C0']
    bars = plt.bar(labels, times_1000, color=colors_bars, alpha=0.8)

    plt.xlabel('الخوارزمية ونوع البيانات', fontsize=12, fontweight='bold')
    plt.ylabel('وقت التنفيذ (ثانية)', fontsize=12, fontweight='bold')
    plt.title('مقارنة الأداء لحجم 1000 عنصر', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')

    # إضافة القيم على الأعمدة
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height + 0.001,
                 f'{height:.3f}s', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig('performance_bars.png', dpi=300, bbox_inches='tight')
    plt.show()


def create_detailed_analysis():
    """إنشاء تحليل مفصل"""

    df = pd.DataFrame(data)

    # 5. تحليل تأثير نوع البيانات
    plt.figure(figsize=(10, 8))

    algorithms = df['Algorithm'].unique()
    data_types = df['Type'].unique()

    # تجميع البيانات للحجم 1000
    size_1000_data = df[df['Size'] == 1000]

    x = np.arange(len(algorithms))
    width = 0.25

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # وقت التنفيذ
    for i, data_type in enumerate(data_types):
        times = []
        for algo in algorithms:
            algo_data = size_1000_data[(size_1000_data['Algorithm'] == algo) &
                                       (size_1000_data['Type'] == data_type)]
            if len(algo_data) > 0:
                times.append(algo_data['Time'].values[0])
            else:
                times.append(0)

        ax1.bar(x + i * width, times, width, label=data_type, alpha=0.8)

    ax1.set_xlabel('الخوارزمية', fontweight='bold')
    ax1.set_ylabel('وقت التنفيذ (ثانية)', fontweight='bold')
    ax1.set_title('تأثير نوع البيانات على وقت التنفيذ (حجم 1000)', fontweight='bold')
    ax1.set_xticks(x + width)
    ax1.set_xticklabels(algorithms)
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='y')

    # عدد التبديلات
    for i, data_type in enumerate(data_types):
        displacements = []
        for algo in algorithms:
            algo_data = size_1000_data[(size_1000_data['Algorithm'] == algo) &
                                       (size_1000_data['Type'] == data_type)]
            if len(algo_data) > 0:
                displacements.append(algo_data['Displacements'].values[0])
            else:
                displacements.append(0)

        ax2.bar(x + i * width, displacements, width, label=data_type, alpha=0.8)

    ax2.set_xlabel('الخوارزمية', fontweight='bold')
    ax2.set_ylabel('عدد التبديلات', fontweight='bold')
    ax2.set_title('تأثير نوع البيانات على عدد التبديلات (حجم 1000)', fontweight='bold')
    ax2.set_xticks(x + width)
    ax2.set_xticklabels(algorithms)
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig('data_type_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()


def generate_all_charts():
    """توليد جميع الرسوم البيانية"""
    print("🚀 بدء توليد الرسوم البيانية...")
    print("=" * 50)

    create_performance_charts()
    create_detailed_analysis()

    print("✅ تم إنشاء جميع الرسوم البيانية بنجاح!")
    print("\n📊 الملفات المُنشأة:")
    print("1. performance_comparison.png - مقارنة الأداء الشاملة")
    print("2. comparisons_analysis.png - تحليل المقارنات")
    print("3. displacements_analysis.png - تحليل التبديلات")
    print("4. performance_bars.png - مخطط الأعمدة")
    print("5. data_type_analysis.png - تحليل تأثير نوع البيانات")
    print("=" * 50)


# كود سريع للتشغيل
if __name__ == "__main__":
    generate_all_charts()