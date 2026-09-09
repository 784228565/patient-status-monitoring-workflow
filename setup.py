# -*- coding: utf-8 -*-
"""
患者状态监测工作流 - 初始化向导
用法: python setup.py
"""
import sys
import os

REQUIRED_DIRS = ['data', 'output', '原始资料']
OPTIONAL_DEPS = [
    ('pdfplumber', '提取检验报告 PDF 文本（推荐）'),
    ('fitz', 'PDF 转图片（PyMuPDF，推荐）'),
    ('reportlab', '生成家属版 PDF 报告（推荐）'),
]


def main():
    print('=' * 50)
    print(' 患者状态监测工作流 - 初始化向导')
    print('=' * 50)

    # 1. Python version
    v = sys.version_info
    ok = v >= (3, 8)
    print(f"\n[1/3] Python 版本: {v.major}.{v.minor}.{v.micro} ... {'OK' if ok else '需要 3.8+，请升级'}")
    if not ok:
        sys.exit(1)

    # 2. directories
    print('\n[2/3] 创建目录:')
    root = os.path.dirname(os.path.abspath(__file__))
    parent = os.path.dirname(root)
    for d in REQUIRED_DIRS:
        # data/ output/ inside workflow folder; 原始资料/ at project root (parent)
        path = os.path.join(root, d) if d in ('data', 'output') else os.path.join(parent, d)
        os.makedirs(path, exist_ok=True)
        print(f'  ✓ {os.path.relpath(path, parent)}')

    # 3. optional deps
    print('\n[3/3] 可选依赖检查:')
    missing = []
    for mod, desc in OPTIONAL_DEPS:
        try:
            __import__(mod)
            print(f'  ✓ {mod} — {desc}')
        except ImportError:
            print(f'  ✗ {mod} — {desc}（未安装）')
            missing.append(mod)
    if missing:
        pkgs = {'pdfplumber': 'pdfplumber', 'fitz': 'PyMuPDF', 'reportlab': 'reportlab'}
        print('\n  安装缺失依赖:  pip install ' + ' '.join(pkgs[m] for m in missing))

    print('\n' + '=' * 50)
    print(' 初始化完成！下一步:')
    print(' 1. 把检验报告照片/PDF 放入 原始资料/')
    print(' 2. 用 AI 助手（如 Kimi CLI）打开本项目目录')
    print(' 3. 说: "执行患者状态监测工作流"')
    print(' 详细说明见 SETUP.md')
    print('=' * 50)


if __name__ == '__main__':
    main()
