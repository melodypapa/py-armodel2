"""InternalTriggeringPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 322)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 561)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_Trigger.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)


class InternalTriggeringPoint(AbstractAccessPoint):
    """AUTOSAR InternalTriggeringPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_impl_policy_enum: Optional[SwImplPolicyEnum]
    def __init__(self) -> None:
        """Initialize InternalTriggeringPoint."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalTriggeringPoint":
        """Deserialize XML element to InternalTriggeringPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InternalTriggeringPoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_impl_policy_enum
        child = ARObject._find_child_element(element, "SW-IMPL-POLICY-ENUM")
        if child is not None:
            sw_impl_policy_enum_value = child.text
            obj.sw_impl_policy_enum = sw_impl_policy_enum_value

        return obj



class InternalTriggeringPointBuilder:
    """Builder for InternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalTriggeringPoint = InternalTriggeringPoint()

    def build(self) -> InternalTriggeringPoint:
        """Build and return InternalTriggeringPoint object.

        Returns:
            InternalTriggeringPoint instance
        """
        # TODO: Add validation
        return self._obj
