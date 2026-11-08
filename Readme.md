# Mount & Blade: Warband Module System – Python 3 移植版

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

本项目是 **《骑马与砍杀：战团》**（Mount & Blade: Warband）官方 **Module System 1171** 的完整 Python 3 移植版本。查看/下载仓库点 [这里。](https://github.com/kcolcy/mb_warband_module_system_1174_for_-python3)
原版 Module System 基于 **Python 2** 编写，用于将模组源码编译为游戏可识别的数据文件（如 `item_kinds.txt`、`troops.txt`、`party_templates.txt` 等）。  
本移植版在 **保持原版逻辑与输出完全一致** 的前提下，将整个代码库升级至 Python 3，并充分利用 Python 3 的新特性，为模组开发者提供更现代、更高效、更可靠的开发环境。

---

## 🎯 核心目标

- ✅ **完全兼容原有逻辑**：所有编译结果与原 Python 2 版本逐字节一致，确保模组行为无差异。
- ✅ **原生 Python 3 支持**：摆脱已废弃的 Python 2，完美融入现代开发工具链（IDE、CI/CD 等）。
- ✅ **性能与可维护性提升**：借助 Python 3 的性能优化和语法改进，编译速度更快，代码更易读、易维护。
- ✅ **更友好的错误诊断**：异常信息更加清晰，帮助开发者迅速定位语法问题。

---

## 🚀 为什么选择 Python 3 版本？

### 1. 更强大的语言特性
- **类型注解（Type Hints）**：核心函数和数据结构均已添加类型注解，显著提升代码可读性和 IDE 智能提示（自动补全、类型检查）。

### 2. 性能与精度优化
- **明确的除法语义**：`/` 返回浮点数，`//` 返回整数，避免因隐式类型转换造成的意外结果（*注意：这是 Python 2 与 Python 3 的重要区别，模组开发中需特别留意整数运算*）。
- **迭代器与生成器性能提升**：处理大型数据集（如兵种、物品）时编译速度明显加快。

### 3. 现代化生态支持
- **原生 Unicode 支持**：无需手动处理编码转换，多语言模组文案（中文、俄文等）可直接使用。

### 4. 长期维护与便捷性
- Python 2 已于 2020 年 1 月 1 日停止官方支持，当前主流的编辑器对python的的配置不完善。
- AI对python3的支持更完善，可以实现AI辅助设计。

---

## ✨ 额外修改

除基础迁移外，本项目针对原版进行了两项关键改进：

- **输出文件编码统一为 UTF-8**  
  所有生成的 `*.txt` 文件均以 UTF-8 编码保存，彻底解决跨平台、多语言环境下的乱码问题。

- **调整编译顺序，打破依赖死锁**  
  原版编译流程中存在严重的模块间相互依赖（例如 A 依赖 B 的中间产物 `ID_xxx.py`，B 依赖 C 的中间产物，C 依赖 D……形成链式依赖），导致 **编译过程可能永远无法完成**。  
  本版本通过重新编排 `build_module.bat` 中的编译顺序，**减小了相互依赖模块间的冲突程度**，使得第一次编译虽然仍会因缺少部分 `ID_xxx.py` 而报错，但会生成足够多的中间文件；**第二次编译时所有必需的 `ID_xxx.py` 均已存在，即可完整通过**。  
  这与原版“长时间卡死、多次编译仍无法完成”的情况形成鲜明对比。

---

## 📦 安装与使用

### 系统要求
- **Python3 即可**（推荐 Python 3.10+，任意操作系统均可）

### 快速上手

本项目与官方 Module System 编译流程完全一致。
1. 克隆/下载本代码仓库
2. 进入代码工程目录
3. 修改`module_info.py`中的输出目录为指定目录
4. 执行`build_module.bat`，开始编译
