# py-armodel2 项目指南

本文档为 AI 代理提供此 Python 项目的全面上下文信息，用于指导后续的开发和维护工作。

## 项目概述

**py-armodel2** 是一个用于处理 AUTOSAR（汽车开放系统架构）ARXML 模型的 Python 库。该项目采用代码生成架构，通过从映射文件自动生成静态 Python 类来表示 AUTOSAR 类型定义。

**项目状态**: 早期开发阶段，基础架构已就绪，正在实现核心功能。

### 核心特性

- **代码生成驱动**: 所有 AUTOSAR 模型类从 `docs/requirements/mapping.json` 自动生成
- **多版本支持**: 支持 AUTOSAR 00044、00046、00052 三个 schema 版本
- **静态类型安全**: 使用 Python 类型提示和 MyPy 类型检查
- **完整的测试覆盖**: 单元测试和集成测试
- **现代化工具链**: 使用 Ruff 进行代码格式化和 lint，Pytest 进行测试

## 技术栈

### 核心依赖
- **Python 3.8+**: 最低 Python 版本要求
- **xml.etree.ElementTree**: XML 解析（标准库，替代 lxml）
- **PyYAML 6.0+**: 配置文件解析

### 开发工具
- **pytest 7.0+**: 测试框架
- **pytest-cov 4.0+**: 代码覆盖率
- **mypy 1.0+**: 静态类型检查
- **ruff 0.1.0+**: 代码 lint 和格式化

## 项目结构

```
py-armodel2/
├── src/armodel/              # 源代码
│   ├── cfg/                 # 配置文件
│   │   └── schemas/        # Schema 版本配置
│   │       └── config.yaml # 版本映射配置
│   ├── core/               # 核心工具
│   │   ├── base.py        # ARObject 基类
│   │   └── version.py     # Schema 版本检测
│   ├── models/             # 生成的 AUTOSAR 模型类
│   │   └── M2/            # AUTOSAR M2 模型定义
│   ├── reader/             # ARXML 读取模块
│   ├── writer/             # ARXML 写入模块
│   ├── cli/                # 命令行接口
│   └── utils/              # 辅助工具
├── tests/                  # 测试套件
│   ├── unit/              # 单元测试（镜像 src 结构）
│   ├── integration/       # 集成测试
│   ├── fixtures/          # 测试数据
│   └── test_generate_models.py # 代码生成器测试
├── tools/                  # 代码生成工具
│   └── generate_models.py # 模型类生成器
├── scripts/                # 开发脚本
│   └── setup.sh           # 开发环境设置脚本
├── demos/                  # AUTOSAR schema 和示例文件
│   ├── xsd/               # XSD schema 文件
│   └── arxml/             # ARXML 示例文件
├── docs/                   # 文档
│   ├── plans/             # 实现计划
│   │   ├── CODING_RULES.md # 编码规则
│   │   └── design-rules.md # 设计规则
│   └── requirements/      # 需求文档
│       └── mapping.json   # 类型定义映射
├── pyproject.toml         # 项目配置
├── .github/workflows/     # CI/CD 配置
│   └── ci.yml            # GitHub Actions 工作流
└── .gitignore             # Git 忽略规则
```

## 构建和运行

### 安装和设置

```bash
# 使用设置脚本（推荐）
./scripts/setup.sh

# 或手动安装
pip install -e ".[dev]"
```

### 运行测试

```bash
# 设置 PYTHONPATH 并运行测试
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest

# 运行带覆盖率的测试
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest --cov=armodel --cov-report=html

# 运行特定测试文件
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/test_core/test_version.py -v
```

### 代码质量检查

```bash
# Lint 检查
ruff check src/ tools/

# 代码格式化
ruff format src/ tools/

# 类型检查
mypy src/
```

### 代码生成

```bash
# 从 mapping.json 生成所有模型类
python tools/generate_models.py docs/requirements/mapping.json src/armodel/models/
```

## 开发约定

### 编码规范

项目遵循以下编码规则（定义在 `docs/plans/CODING_RULES.md`）：

#### 命名约定
- **文件名**: 使用 snake_case（例如：`test_version.py`）
- **类名**: 使用 PascalCase（例如：`ApplicationInterface`）
- **函数/变量名**: 使用 snake_case

#### 类结构
- 所有生成的类必须继承自 `ARObject`
- 每个类必须包含 `serialize()` 和 `deserialize()` 方法
- 每个类必须包含一个 builder 类用于实例化
- Builder 类命名为 `<ClassName>Builder`

#### 序列化/反序列化
- `serialize()` 返回 `xml.etree.ElementTree.Element`
- `deserialize()` 是 `@classmethod`，接受 element 参数
- 所有子元素必须使用其 `serialize()` 方法序列化
- 所有子元素必须使用 `deserialize()` 方法反序列化

#### 包结构
- 包层次结构必须与 `mapping.json` 中的 package_path 完全匹配
- 每个类在匹配的目录中都有自己的文件
- `__init__.py` 导出包中的所有类

#### 类型安全
- 为所有类属性使用类型提示
- 对可空属性使用 `Optional[T]`
- 用文档字符串记录复杂类型

#### 验证
- 所有属性必须在 `builder.build()` 方法中验证
- 对无效的属性值引发 `ValueError`
- 验证必需属性是否存在

#### 文档
- 每个类必须有文档字符串
- 每个方法必须有文档字符串
- 用内联注释记录复杂逻辑

#### 测试
- 每个类必须有单元测试
- 测试必须覆盖 serialize/deserialize
- 测试必须验证 builder 功能

#### 代码质量
- 无硬编码值（在适当位置使用配置）
- 遵循 PEP 8 风格指南
- 最大行长 100 字符

### Git 工作流

- **主分支**: `main`
- **开发分支**: `develop`
- **功能分支**: `feature/**`
- **当前分支**: `feature/implementation-phase-2`

### CI/CD

GitHub Actions 配置（`.github/workflows/ci.yml`）包括：
- **Lint**: 使用 Ruff 检查代码
- **Type Check**: 使用 MyPy 进行类型检查
- **Test**: 在 Python 3.8-3.11 上运行测试
- **Coverage**: 上传覆盖率报告到 Codecov

## AUTOSAR Schema 版本

项目支持多个 AUTOSAR 标准版本：

### 版本映射（config.yaml）

| 版本   | Namespace                               | XSD 文件              | 特性                          |
|--------|-----------------------------------------|-----------------------|-------------------------------|
| 00044  | http://autosar.org/3.0.4               | AUTOSAR_00044.xsd     | Classic Platform 4.3.1 (2017) |
| 00046  | http://autosar.org/schema/r4.0         | AUTOSAR_00046.xsd     | CP 4.4.0 / AP 18-10 (2018)    |
| 00052  | http://autosar.org/schema/r5.0         | AUTOSAR_00052.xsd     | CP/AP 23-11 (2023)            |

**默认版本**: 00046

### Schema 变体
- **Standard**: 带有所有验证规则的完整 schema
- **COMPACT**: 性能优化版本，减少验证开销
- **STRICT_COMPACT**: 结合严格基数验证与紧凑性能

## 核心架构

### 模型生成

所有 AUTOSAR 模型类从 `docs/requirements/mapping.json` 生成：
- **1,937 个类型定义**
- 生成的类放置在 `src/armodel/models/` 中，遵循包路径
- 每个类包含 serialize/deserialize 方法
- 包含 builder 类以便于对象创建

### Reader/Writer 模块

- **Reader**: 加载 ARXML 文件，使用 deserialize 方法创建 Python 对象
- **Writer**: 使用 serialize 方法将 Python 对象序列化为 ARXML

### Schema 版本支持

通过 `cfg/schemas/config.yaml` 支持多个 AUTOSAR schema 版本：
- 版本检测从 ARXML 命名空间声明
- 版本特定的解析和验证
- 旧 ARXML 文件的向后兼容性
- 新版本的向前兼容性考虑

## 重要文件说明

### 配置文件
- `pyproject.toml`: 项目配置、依赖和工具设置
- `.github/workflows/ci.yml`: CI/CD 配置
- `src/armodel/cfg/schemas/config.yaml`: Schema 版本配置

### 代码生成
- `tools/generate_models.py`: 模型类生成器
- `docs/requirements/mapping.json`: 类型定义映射

### 核心模块
- `src/armodel/core/base.py`: ARObject 基类
- `src/armodel/core/version.py`: Schema 版本检测

### 测试
- `tests/unit/`: 单元测试（镜像 src 结构）
- `tests/integration/`: 集成测试
- `tests/fixtures/`: 测试数据（AUTOSAR ARXML 文件）

### 文档
- `docs/plans/CODING_RULES.md`: 编码规则
- `docs/plans/design-rules.md`: 设计规则
- `README.md`: 项目概览和快速开始

## 常见任务

### 添加新的 AUTOSAR 类型

1. 在 `docs/requirements/mapping.json` 中添加类型定义
2. 运行代码生成器：`python tools/generate_models.py docs/requirements/mapping.json src/armodel/models/`
3. 为新类型添加单元测试

### 修复 bug

1. 在 `tests/` 中添加或更新测试用例
2. 修复代码
3. 运行测试验证修复：`PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest`
4. 运行 lint 和类型检查：`ruff check src/ && mypy src/`

### 更新依赖

1. 在 `pyproject.toml` 中更新版本
2. 运行 `pip install -e ".[dev]"`
3. 运行测试确保兼容性

## 测试策略

### 单元测试
- 镜像 `src/` 目录结构
- 每个模块都有对应的测试文件
- 使用 pytest 框架

### 集成测试
- 测试完整的 ARXML 读取/写入流程
- 使用 `tests/fixtures/` 中的实际 AUTOSAR 文件

### 代码生成测试
- `tests/test_generate_models.py`: 测试代码生成器
- 验证生成的代码符合编码规则

## 性能考虑

- 使用 compact schema 进行验证以减少开销
- 考虑使用缓存机制处理大型 ARXML 文件
- 对频繁操作使用批处理方法

## 安全注意事项

- 验证所有用户输入的 ARXML 文件
- 使用 schema 验证防止 XML 注入
- 限制文件大小以防止 DoS 攻击

## AUTOSAR 参考资料

- 官方 AUTOSAR 规范: https://www.autosar.org
- Schema 版本编号遵循 AUTOSAR 文档标识（例如 AUTOSAR_00052）
- 每个 schema 版本对应特定的 AUTOSAR Classic Platform 和 Adaptive Platform 版本

## 联系信息

- 项目作者: Your Name (your.email@example.com)
- 许可证: MIT
