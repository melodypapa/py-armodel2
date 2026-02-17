"""AUTOSAR ArrayImplPolicyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 276)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.enums.json"""

from enum import Enum


class ArrayImplPolicyEnum(Enum):
    """AUTOSAR ArrayImplPolicyEnum enumeration."""

    PAYLOADASARRAY = "payloadAsArray"
    PAYLOADASPOINTERTOARRAY = "payloadAsPointerToArray"
