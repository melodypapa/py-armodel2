# Unfixed F821 Errors - Missing Type Definitions

## Summary

After fixing the generator bugs, there are **63 remaining F821 errors** (undefined names) in the generated model code. These errors are caused by types that are referenced in the JSON metadata but not defined in any JSON file.

## Root Cause

The JSON metadata files in `docs/json/packages/` contain class definitions with attributes that reference types which don't have corresponding definitions. These types appear to be AUTOSAR schema types that were not extracted during the JSON generation process.

## Error Categories

### 1. Crypto Types (12 errors)
**File:** `src/armodel2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/crypto_key_slot.py`

| Type | Count | Context |
|------|-------|---------|
| `CryptoObjectTypeEnum` | 3 | Attribute type |
| `CryptoKeySlotAllowedModification` | 3 | Attribute type |
| `CryptoKeySlotContentAllowedUsage` | 3 | Attribute type |
| `CryptoKeySlotTypeEnum` | 3 | Attribute type |

**Source JSON:** `docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_CryptoDeployment.classes.json`

### 2. BSW Policy Types (20 errors)
**File:** `src/armodel2/models/M2/AUTOSARTemplates/BswModuleTemplate/BswBehavior/bsw_bsw_scheduler_when_entity.py`

| Type | Count | Context |
|------|-------|---------|
| `BswClientPolicy` | 4 | Attribute type |
| `BswDataSendPolicy` | 4 | Attribute type |
| `BswInternalTriggeringPointPolicy` | 4 | Attribute type |
| `BswParameterPolicy` | 4 | Attribute type |
| `BswPerInstanceMemoryPolicy` | 4 | Attribute type |
| `BswReleasedTriggerPolicy` | 4 | Attribute type |

**Source JSON:** `docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json`

### 3. Firewall Types (6 errors)
**File:** `src/armodel2/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication/Firewall/firewall_interface.py`

| Type | Count | Context |
|------|-------|---------|
| `FirewallActionEnum` | 6 | Attribute type |

**Source JSON:** `docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication_Firewall.classes.json`

### 4. XML Processing Types (6 errors)
**File:** `src/armodel2/models/M2/MSR/AsamHdo/SpecialData/sd.py`

| Type | Count | Context |
|------|-------|---------|
| `XmlSpaceEnum` | 6 | Attribute type |

**Source JSON:** `docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json`

### 5. Reference Types (6 errors)
**Files:**
- `src/armodel2/models/M2/AUTOSARTemplates/SWComponentTemplate/SwcInternalBehavior/ServiceMapping/role_based_data_type_assignment.py`
- `src/armodel2/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication/Timing/time_range_type.py`

| Type | Count | Context |
|------|-------|---------|
| `AutosarParameterRef` | 3 | Attribute type |
| `SwComponentMappingConstraints` | 2 | Attribute type |
| `TimeRangeTypeTolerance` | 3 | Attribute type |

### 6. Other Types (13 errors)

| Type | Count | File | Context |
|------|-------|------|---------|
| `V2xSupportEnum` | 3 | `ecu_instance.py` | V2X support attribute |
| `Union` | 2 | Various | Type hint import |
| `physicalDimension` | 1 | `unit.py` | Unit dimension attribute |

## Resolution Options

### Option 1: Add Missing Type Definitions
Create the missing type definitions in the appropriate JSON files:
1. Enum types should be added to `*.enums.json` files
2. Class types should be added to `*.classes.json` files
3. Regenerate models after adding definitions

### Option 2: Use `Any` Type for Missing Definitions
Modify the generator to emit `Any` type hints for types that cannot be resolved, with a runtime warning. This is a compromise that allows code to compile while losing type safety.

### Option 3: Keep F821 Ignored (Current State)
Continue ignoring F821 errors in generated code. This hides the real issues but doesn't break the build.

## Recommended Approach

1. **Investigate** why these types are missing from JSON extraction
2. **Extract** missing enum/class definitions from AUTOSAR XSD schemas
3. **Update** JSON metadata files with correct definitions
4. **Regenerate** model classes
5. **Remove** F821 from `pyproject.toml` ignores

## Files to Update

1. `docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_CryptoDeployment.enums.json` - Add crypto enums
2. `docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.enums.json` - Add BSW policy enums
3. `docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication_Firewall.enums.json` - Add firewall enum
4. `docs/json/packages/M2_MSR_AsamHdo_SpecialData.enums.json` - Add XmlSpaceEnum
5. Various class definition files for missing class types

## Progress Tracking

- [ ] Investigate XSD schemas for missing type definitions
- [ ] Add `CryptoObjectTypeEnum`, `CryptoKeySlotTypeEnum` enums
- [ ] Add `CryptoKeySlotAllowedModification`, `CryptoKeySlotContentAllowedUsage` classes
- [ ] Add BSW policy enums
- [ ] Add `FirewallActionEnum`
- [ ] Add `XmlSpaceEnum`
- [ ] Add missing reference types
- [ ] Regenerate models and verify F821 count
- [ ] Remove F821 from ruff ignores in `pyproject.toml`

## Related Issues

- Original plan: Add Quality Check for Generated Code
- Generator fixes completed: snake_attr_name bug, `any (xxx)` type handling
- Test status: All 229 unit tests pass, all 29 integration tests pass