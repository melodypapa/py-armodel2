"""IdsMgrNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 842)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class IdsMgrNeeds(ServiceNeeds):
    """AUTOSAR IdsMgrNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "use_smart": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # useSmart
    }

    def __init__(self) -> None:
        """Initialize IdsMgrNeeds."""
        super().__init__()
        self.use_smart: Optional[Boolean] = None


class IdsMgrNeedsBuilder:
    """Builder for IdsMgrNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsMgrNeeds = IdsMgrNeeds()

    def build(self) -> IdsMgrNeeds:
        """Build and return IdsMgrNeeds object.

        Returns:
            IdsMgrNeeds instance
        """
        # TODO: Add validation
        return self._obj
