"""InternalTriggeringPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 322)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 561)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_Trigger.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)


class InternalTriggeringPoint(AbstractAccessPoint):
    """AUTOSAR InternalTriggeringPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sw_impl_policy_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwImplPolicyEnum,
        ),  # swImplPolicyEnum
    }

    def __init__(self) -> None:
        """Initialize InternalTriggeringPoint."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None


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
