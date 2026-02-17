"""SubElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SubElementMapping(ARObject):
    """AUTOSAR SubElementMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "first_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SubElementRef,
        ),  # firstElement
        "second_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SubElementRef,
        ),  # secondElement
        "text_table": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=TextTableMapping,
        ),  # textTable
    }

    def __init__(self) -> None:
        """Initialize SubElementMapping."""
        super().__init__()
        self.first_element: Optional[SubElementRef] = None
        self.second_element: Optional[SubElementRef] = None
        self.text_table: TextTableMapping = None


class SubElementMappingBuilder:
    """Builder for SubElementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SubElementMapping = SubElementMapping()

    def build(self) -> SubElementMapping:
        """Build and return SubElementMapping object.

        Returns:
            SubElementMapping instance
        """
        # TODO: Add validation
        return self._obj
