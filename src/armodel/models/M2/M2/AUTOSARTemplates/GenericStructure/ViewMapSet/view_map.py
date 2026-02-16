"""ViewMap AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)


class ViewMap(Identifiable):
    """AUTOSAR ViewMap."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "first_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AtpFeature,
        ),  # firstElements
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
        "second_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AtpFeature,
        ),  # secondElements
    }

    def __init__(self) -> None:
        """Initialize ViewMap."""
        super().__init__()
        self.first_elements: list[AtpFeature] = []
        self.role: Optional[Identifier] = None
        self.second_elements: list[AtpFeature] = []


class ViewMapBuilder:
    """Builder for ViewMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ViewMap = ViewMap()

    def build(self) -> ViewMap:
        """Build and return ViewMap object.

        Returns:
            ViewMap instance
        """
        # TODO: Add validation
        return self._obj
