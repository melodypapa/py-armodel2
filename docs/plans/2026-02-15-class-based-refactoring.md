# py-armodel2 Class-Based Architecture Refactoring

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transition from module-based architecture (reader/writer modules) to class-based architecture where each AUTOSAR class handles its own serialization/deserialization.

**Current Architecture:**
- `src/armodel/reader/` - Module for loading ARXML
- `src/armodel/writer/` - Module for writing ARXML
- Generated model classes in `src/armodel/models/` with serialize()/deserialize() stubs

**Proposed Architecture:**
- Keep generated model classes as-is
- Add `load_from_xml()` and `save_to_xml()` class methods to each generated class
- Remove reader/writer modules
- Update high-level API to use class methods directly

**Benefits:**
- Simpler architecture (fewer modules)
- Direct object-oriented API
- No need to pass through module boundaries
- Better aligns with AUTOSAR object-oriented design

**Implementation Tasks:**

### Task 1: Add load_from_xml() and to_xml() methods to ARObject base class
- [x] Create base test for these methods
- [ ] Implement in ARObject base class:
  - **Recursive support**: load_from_xml() must deserialize entire tree
  - **from_xml()**: Serialize object including children
  - Must preserve element tags and all attributes
- [ ] Update code generator to add these methods to all generated classes
- [ ] Regenerate all models with updated methods
- [ ] Verify tests pass
- [ ] Commit changes

### Task 2: Add save_to_xml() class method to generated classes
- [x] Create base test for save_to_xml() method
- [ ] Implement in ARObject base class - must preserve element tag and attributes
- [ ] Update code generator to add save_to_xml() to all generated classes
- [ ] Regenerate all models with new method
- [ ] Verify tests pass
- [ ] Commit changes

### Task 3: Update high-level API to use class methods
- [x] Decide on new API design:
  - Option A: `from armodel import load_arxml, save_arxml, AUTOSAR` (current)
  - Option B: `from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR`
- [ ] Document chosen API design in README
- [ ] Update imports in tests to use new API
- [ ] Verify tests pass with new API
- [ ] Commit changes

### Task 4: Remove deprecated reader/writer modules
- [ ] Add deprecation warnings to reader/writer modules
- [ ] Run full test suite to ensure no regressions
- [ ] Commit changes
- [ ] Remove reader/writer directories in next batch

### Task 5: Update code generator
- [ ] Update generate_class_code() to include load_from_xml() and save_to_xml() methods
- [ ] Regenerate all models with updated methods
- [ ] Verify tests pass
- [ ] Commit changes

### Task 6: Final cleanup and merge
- [ ] Merge feature branch to main
- [ ] Create pull request for review
- [ ] Delete feature branch
