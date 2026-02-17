"""BswModuleCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 77)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)


class BswModuleCallPoint(Referrable):
    """AUTOSAR BswModuleCallPoint."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "contexts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswDistinguishedPartition,
        ),  # contexts
    }

    def __init__(self) -> None:
        """Initialize BswModuleCallPoint."""
        super().__init__()
        self.contexts: list[BswDistinguishedPartition] = []


class BswModuleCallPointBuilder:
    """Builder for BswModuleCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleCallPoint = BswModuleCallPoint()

    def build(self) -> BswModuleCallPoint:
        """Build and return BswModuleCallPoint object.

        Returns:
            BswModuleCallPoint instance
        """
        # TODO: Add validation
        return self._obj
