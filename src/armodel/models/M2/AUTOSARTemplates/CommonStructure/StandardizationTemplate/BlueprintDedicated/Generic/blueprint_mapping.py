"""BlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintDedicated_Generic.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint import (
    AtpBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprintable import (
    AtpBlueprintable,
)


class BlueprintMapping(ARObject):
    """AUTOSAR BlueprintMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "blueprint": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=AtpBlueprint,
        ),  # blueprint
        "derived_object": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=AtpBlueprintable,
        ),  # derivedObject
    }

    def __init__(self) -> None:
        """Initialize BlueprintMapping."""
        super().__init__()
        self.blueprint: AtpBlueprint = None
        self.derived_object: AtpBlueprintable = None


class BlueprintMappingBuilder:
    """Builder for BlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintMapping = BlueprintMapping()

    def build(self) -> BlueprintMapping:
        """Build and return BlueprintMapping object.

        Returns:
            BlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
