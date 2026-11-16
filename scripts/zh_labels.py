#!/usr/bin/env python3
"""Official English → Simplified Chinese labels for nav and front matter."""
from __future__ import annotations

import re

GROUP_ZH = {
    "APIs": "API",
    "Actions": "操作",
    "Appliances": "家电",
    "Architecture": "架构",
    "Async": "异步",
    "Authentication": "认证",
    "Automations and organizing": "自动化与组织",
    "Basics": "基础",
    "Boards": "开发板",
    "Bronze": "青铜",
    "Changing behavior": "变更行为",
    "Community": "社区",
    "Contributing": "贡献",
    "Controls": "控制",
    "Core and integrations": "核心与集成",
    "Data": "数据",
    "Data and updates": "数据与更新",
    "Devices and registries": "设备与注册表",
    "Discovery": "发现",
    "Entities and devices": "实体与设备",
    "Entity cards": "实体卡片",
    "Feedback and status": "反馈与状态",
    "Forms": "表单",
    "Frontend": "前端",
    "Getting started": "入门",
    "Gold": "金",
    "Grouping and layout": "分组与布局",
    "Guides": "指南",
    "Helpers": "助手",
    "How it works": "工作原理",
    "Information": "信息",
    "Input": "输入",
    "Inputs and helpers": "输入与助手",
    "Installation and system": "安装与系统",
    "Integration features": "集成功能",
    "Layout and content": "布局与内容",
    "Lights and climate": "灯光与气候",
    "Media": "媒体",
    "Media and pictures": "媒体与图片",
    "Openings and security": "开合与安防",
    "Pickers": "选择器",
    "Platinum": "铂金",
    "Pull requests": "Pull request",
    "Reference": "参考",
    "Remotes and signals": "遥控与信号",
    "Sensors and status": "传感器与状态",
    "Set up": "开始设置",
    "Setup and configuration": "设置与配置",
    "Ship": "发布上线",
    "Showing values": "数值展示",
    "Silver": "银",
    "Test": "测试",
    "The core": "核心",
    "Voice": "语音",
    "Voice and AI": "语音与 AI",
    "Write code": "编写代码",
}

# Index pages, common titles, and known short labels
LABEL_ZH = {
    **GROUP_ZH,
    "Apps": "应用",
    "Around Core": "核心外围",
    "Automated checks": "自动检查",
    "Automated documentation checks": "文档自动检查",
    "Bashio": "Bashio",
    "Brand": "品牌",
    "Build a Python library": "构建 Python 库",
    "Building integrations": "构建集成",
    "Companion apps": "伴侣应用",
    "Components": "组件",
    "Custom cards and more": "自定义卡片及其他",
    "Dashboards": "仪表盘",
    "Design": "设计",
    "Development": "开发",
    "Development workflow": "开发工作流",
    "Entities": "实体",
    "Epic": "Epic（史诗）",
    "Event loop": "事件循环",
    "Extend the frontend": "扩展前端",
    "Feature request": "功能请求",
    "Fork": "Fork（复刻）",
    "Foundations": "基础",
    "From idea to release": "从构想到发布",
    "Get started": "开始贡献",
    "Glossary": "术语表",
    "Home Assistant OS": "Home Assistant OS",
    "How core works": "核心如何工作",
    "Inside Core": "核心内部",
    "Integration quality scale": "集成质量等级",
    "Issue": "Issue（议题）",
    "Marketplace": "应用市场",
    "Mobile app API": "移动应用 API",
    "More info": "更多信息",
    "OS and Supervisor": "OS 与 Supervisor",
    "Opportunity": "机会项",
    "Patterns": "模式",
    "REST API": "REST API",
    "Releases": "发布",
    "Review and release": "审查与发布",
    "Roadmap": "路线图",
    "Security": "安全",
    "Siren": "警报器",
    "Siren entity": "警报器实体",
    "States": "状态",
    "Structure a page": "组织页面结构",
    "Supervisor": "Supervisor",
    "Supervisor API": "Supervisor API",
    "The data layer": "数据层",
    "The frontend": "前端",
    "Translations": "翻译",
    "UI text": "界面文本",
    "WebSocket API": "WebSocket API",
    "Who we design for": "我们为谁设计",
    "Writing docs": "撰写文档",
    "The hass object": "hass 对象",
    "The hass object in Python": "Python 中的 hass 对象",
    "The hass object in the frontend": "前端中的 hass 对象",
    "Integration": "集成",
    "State class": "状态类别",
    "Integration category": "集成类别",
    "Development environment": "开发环境",
    "Set up a development environment": "搭建开发环境",
    "Set up your development environment": "搭建开发环境",
    "Set up the environment": "搭建环境",
    "Debug the Supervisor": "调试 Supervisor",
    "Integration front matter": "集成 front matter",
    "Integrations": "集成",
    "Secure integrations": "集成安全",
    "Integration brands and images": "集成品牌与图片",
    "Integration categories": "集成类别",
    "OAuth 2.0": "OAuth 2.0",
    "OAuth 2.0 and application credentials": "OAuth 2.0 与应用凭证",
    "Reauth and reconfigure": "重新认证与重新配置",
    "Reauthentication and reconfiguration": "重新认证与重新配置",
    "Subentries": "子条目",
    "Config subentries": "配置子条目",
    "How an integration fits in": "集成如何融入",
    "Keeping up to date": "保持分支更新",
    "Keeping your branch up to date": "保持分支更新",
    "Your first contribution": "你的第一次贡献",
    "Android": "Android",
    "Apple": "Apple",
}

BAD_EXACT = {
    "联合国",
    "捐款",
    "船",
    "董事会",
    "采摘者",
    "你说的",
    "警卫",
    "写入文件",
    "建设一体化",
    "叉",
    "图片",
    "雌性",
    "国家",
    "芭蕉",
    "黄金",
    "铂",
    "铜",
}


def is_bad(s: object) -> bool:
    if s is None:
        return True
    text = str(s).strip()
    if not text:
        return True
    if text in BAD_EXACT:
        return True
    if len(text) > 80:
        return True
    if "的的的" in text or "支援支援" in text or "等等等等" in text or "草的草" in text or "、、" in text:
        return True
    if "踌咕" in text or "turkey荚" in text or "蓓丝" in text or "芭蕉" in text or "ppe" in text:
        return True
    if re.search(r"[ỡ鹫衲ẹớềệốạướ]", text) or "với" in text:
        return True
    if "合格后得到过" in text or "建立起的均已" in text:
        return True
    if re.search(r"[\{\}].{0,8}大家都", text):
        return True
    return False


def pick_label(zh: object, en: object) -> str:
    en_text = str(en or "").strip()
    zh_text = str(zh or "").strip()
    if en_text in LABEL_ZH:
        return LABEL_ZH[en_text]
    if zh_text and not is_bad(zh_text):
        return zh_text
    if en_text:
        return en_text
    return zh_text
