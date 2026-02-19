"""BswInternalTriggeringPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)


class BswInternalTriggeringPoint(Identifiable):
    """AUTOSAR BswInternalTriggeringPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_impl_policy_enum: Optional[SwImplPolicyEnum]
    def __init__(self) -> None:
        """Initialize BswInternalTriggeringPoint."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInternalTriggeringPoint":
        """Deserialize XML element to BswInternalTriggeringPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswInternalTriggeringPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswInternalTriggeringPoint, cls).deserialize(element)

        # Parse sw_impl_policy_enum
        child = ARObject._find_child_element(element, "SW-IMPL-POLICY-ENUM")
        if child is not None:
            sw_impl_policy_enum_value = SwImplPolicyEnum.deserialize(child)
            obj.sw_impl_policy_enum = sw_impl_policy_enum_value

        return obj



class BswInternalTriggeringPointBuilder:
    """Builder for BswInternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInternalTriggeringPoint = BswInternalTriggeringPoint()

    def build(self) -> BswInternalTriggeringPoint:
        """Build and return BswInternalTriggeringPoint object.

        Returns:
            BswInternalTriggeringPoint instance
        """
        # TODO: Add validation
        return self._obj
