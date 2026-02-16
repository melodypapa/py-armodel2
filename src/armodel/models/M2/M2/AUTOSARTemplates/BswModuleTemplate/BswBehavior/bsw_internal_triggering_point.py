"""BswInternalTriggeringPoint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class BswInternalTriggeringPoint(Identifiable):
    """AUTOSAR BswInternalTriggeringPoint."""

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
        """Initialize BswInternalTriggeringPoint."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None


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
